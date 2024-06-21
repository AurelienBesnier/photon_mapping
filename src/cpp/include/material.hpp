#ifndef MATERIAL_H
#define MATERIAL_H

#include <memory>
#include <cmath>
#include "core.hpp"
#include "sampler.hpp"

struct Material {
    Vec3f diffuse = Vec3f(0.9f);
    Vec3f ambient = Vec3fZero;
    Vec3f specular = Vec3fZero;

    int illum = 1;
    float shininess = 0.2f;
    float transparency = 0.0f;
    float roughness = 0.2f;
    float ior = 1.0f;
    float transmittance = 0.0f;
    float reflectance = 0.0f;
};

/**
 * @enum The type of BxDF of a surface.
 */
enum class BxDFType {
    DIFFUSE, ///< Diffuse surface
    SPECULAR, ///< Specular surface
    CAPTOR, ///< Captor surface
    PHONGCAPTOR
};

/**
 * @enum The Direction of provenance of the Ray (Photon or actual ray for ray tracing)
 */
enum class TransportDirection {
    FROM_LIGHT, ///< The ray comes from a light source (Photon)
    FROM_CAMERA ///< The ray comes from the camera.
};

using DirectionPair = std::pair<Vec3f, Vec3f>;

static auto pow5 = [](float x) { return x * x * x * x * x; };

/**
 * @brief Represents BRDF or BTDF.
 * @class BxDF
 * direction vectors are in tangent space(x: tangent, y: normal, z: bi-tangent)
 */
class BxDF {
private:
    BxDFType type; ///< The type of BxDF.

public:
    explicit BxDF(const BxDFType &type) : type(type) {}

    static float cosTheta(const Vec3f &v) { return v[1]; }

    static float absCosTheta(const Vec3f &v) { return std::abs(cosTheta(v)); }

    // compute reflection direction
    static Vec3f reflect(Vec3f &v, const Vec3f &n) {
        return -v + 2.0f * dot(v, n) * n;
    }

    // compute refracted direction
    static bool refract(const Vec3f &v, const Vec3f &n, float iorI, float iorT,
                        Vec3f &t) {
        const Vec3f t_h = -iorI / iorT * (v - dot(v, n) * n);
        float length2th = length2(t_h);
        // total reflection
        if (length2th > 1.0f) {
            return false;
        }
        const Vec3f t_p = -std::sqrt(std::max(1.0f - length2th, 0.0f)) * n;
        t = t_h + t_p;
        return true;
    }

    static bool refract(const Vec3f &v, const Vec3f &n, Vec3f &t, float transmittance) {
        Vec3f t_h = (v - dot(v, n) * n);
        float len = length(t_h);
        // total reflection
        if (len > transmittance) {
            return false;
        }
        const Vec3f t_p = -std::sqrt(std::max(1.0f - len, 0.0f)) * n;
        t = t_h + t_p;
        return true;
    }

    // schlick approximation of fresnel reflectance
    static float fresnelR(float cosThetaI, float iorI, float iorT) {
        const float f0 =
                (iorI - iorT) * (iorI - iorT) / ((iorI + iorT) * (iorI + iorT));
        return f0 + (1.0f - f0) * pow5(std::max(1.0f - std::abs(cosThetaI), 0.0f));
    }

    // get BxDF type
    BxDFType getType() const { return type; }

    // evaluate BxDF
    virtual Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                           TransportDirection &transport_dir) const = 0;

    // sample direction by BxDF.
    // its pdf is proportional to the shape of BxDF
    virtual Vec3f sampleDirection(Vec3f &wo,
                                  TransportDirection &transport_dir,
                                  Sampler &sampler, Vec3f &wi,
                                  float &pdf) const = 0;

    // get all samplable direction
    // NOTE: for specular only
    // NOTE: used for drawing fresnel reflection nicely at low number of samples
    virtual std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const = 0;
};

/**
 * Class representing a Lambert material.
 * @class Lambert
 */
class Lambert : public BxDF {
private:
    Vec3f rho;

public:
    explicit Lambert(const Vec3f &rho) : BxDF(BxDFType::DIFFUSE), rho(rho) {}

    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        // when wo, wi is under the surface, return 0
        const float cosThetaO = cosTheta(wo);
        const float cosThetaI = cosTheta(wi);

        if (cosThetaO < 0 || cosThetaI < 0) return {0};

        return rho / PI;
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        // cosine weighted hemisphere sampling
        wi = sampleCosineHemisphere(sampler.getNext2D(), pdf);
        
        return evaluate(wo, wi, transport_dir);
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;
        return ret;
    }
};

class Phong : public BxDF {
private:
    Vec3f rho; //diffuse
    Vec3f specular; 
    float roughness;
    float transmittance;
    
public:
    explicit Phong(const Vec3f &rho, const Vec3f &specular, float roughness, float transmittance) : BxDF(BxDFType::DIFFUSE), 
        rho(rho), specular(specular), roughness(roughness), transmittance(transmittance) {}

    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        // when wo, wi is under the surface, return 0
        const float cosThetaO = cosTheta(wo);
        const float cosThetaI = cosTheta(wi);

        Vec3f normal = Vec3f(0,1,0);
        if(cosTheta(wo) < 0) {
            normal = normal * (-1);
        }
        
        Vec3f refl = reflect(wo, normal);
        float lobeSpecular = dot(refl, wi);
        
        if(lobeSpecular > 0) {
            lobeSpecular = std::pow(lobeSpecular, roughness);
        } else {
            lobeSpecular = 0;
        }

        
        return rho * dot(normal, wo) + lobeSpecular * specular;
    }
    
    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {

        // cosine weighted hemisphere sampling
        wi = sampleCosineHemisphere(sampler.getNext2D(), pdf);
        
        Vec3f normal = Vec3f(0,1,0);
        if(cosTheta(wo) < 0) {
            normal = normal * (-1);
            wi = wi * (-1);
        }

        float prob = sampler.getNext1D();   
        float spec = specular[0];
        float diff = rho[0];
        
        //diffuse
        if(prob < diff) {
            return evaluate(wo, wi, transport_dir);
        
        //specular
        } else if(prob < diff + spec) {
            wi = reflect(wo, normal);
            pdf = 1.0;
            return evaluate(wo, wi, transport_dir);

        //transmit
        } else if(prob < diff + spec + transmittance) {
            wi = wi * (-1);

            return evaluate(wo, wi, transport_dir);
        
        //absorb
        } else {
            return Vec3f(0,0,0);
        }
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;
        return ret;
    }
};

class PhongPlant : public BxDF {
private:
    Vec3f rho; //diffuse
    Vec3f specular; 
    float roughness;
    float transmittance;
    
public:
    explicit PhongPlant(const Vec3f &rho, const Vec3f &specular, float roughness, float transmittance) : BxDF(BxDFType::PHONGCAPTOR), 
        rho(rho), specular(specular), roughness(roughness), transmittance(transmittance) {}

    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        // when wo, wi is under the surface, return 0
        const float cosThetaO = cosTheta(wo);
        const float cosThetaI = cosTheta(wi);

        Vec3f normal = Vec3f(0,1,0);
        if(cosTheta(wo) < 0) {
            normal = normal * (-1);
        }
        
        Vec3f refl = reflect(wo, normal);
        float lobeSpecular = dot(refl, wi);
        
        if(lobeSpecular > 0) {
            lobeSpecular = std::pow(lobeSpecular, roughness);
        } else {
            lobeSpecular = 0;
        }

        
        return rho * dot(normal, wo) + lobeSpecular * specular;
    }
    
    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {

        // cosine weighted hemisphere sampling
        wi = sampleCosineHemisphere(sampler.getNext2D(), pdf);
        
        Vec3f normal = Vec3f(0,1,0);
        if(cosTheta(wo) < 0) {
            normal = normal * (-1);
            wi = wi * (-1);
        }

        float prob = sampler.getNext1D();   
        float spec = specular[0];
        float diff = rho[0];
        
        //diffuse
        if(prob < diff) {
            return evaluate(wo, wi, transport_dir);
        
        //specular
        } else if(prob < diff + spec) {
            wi = reflect(wo, normal);
            pdf = 1.0;
            return evaluate(wo, wi, transport_dir);

        //transmit
        } else if(prob < diff + spec + transmittance) {
            wi = wi * (-1);

            return evaluate(wo, wi, transport_dir);
        
        //absorb
        } else {
            return Vec3f(0,0,0);
        }
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;
        return ret;
    }
};

/**
 * Class representing a mirror material.
 * @class Mirror
 */
class Mirror : public BxDF {
private:
    Vec3f rho;

public:
    explicit Mirror(const Vec3f &rho) : BxDF(BxDFType::SPECULAR), rho(rho) {}

    // NOTE: delta function
    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        return {0};
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        wi = reflect(wo, Vec3f(0, 1, 0));
        pdf = 1.0f;

        return rho / absCosTheta(wi);
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;
        const Vec3f wi = reflect(wo, Vec3f(0, 1, 0));
        ret.emplace_back(wi, rho / absCosTheta(wi));
        return ret;
    }
};

// NOTE: due to the asymmetry of BSDF, we need to use a different scaling factor
// for photon tracing
// https://pbr-book.org/3ed-2018/Light_Transport_III_Bidirectional_Methods/The_Path-Space_Measurement_Equation#Non-symmetricScattering
class [[maybe_unused]] Glass : public BxDF {
private:
    Vec3f rho;
    float ior;

public:
    Glass(const Vec3f &rho, float ior)
            : BxDF(BxDFType::SPECULAR), rho(rho), ior(ior) {}

    // NOTE: delta function
    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        return {0};
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        // set appropriate ior, normal
        float iorO, iorI;
        Vec3f n;
        if (wo[1] > 0) {
            iorO = 1.0f;
            iorI = ior;
            n = Vec3f(0, 1, 0);
        } else {
            iorO = ior;
            iorI = 1.0f;
            n = Vec3f(0, -1, 0);
        }

        // fresnel reflectance
        const float fr = fresnelR(dot(wo, n), iorO, iorI);

        // reflection
        if (sampler.getNext1D() < fr) {
            wi = reflect(wo, n);
            pdf = 1.0f;
            return rho / absCosTheta(wi);
        }
            // refraction
        else {
            Vec3f tr;
            if (refract(wo, n, iorO, iorI, tr)) {
                wi = tr;
                pdf = 1.0f;

                float scaling = 1.0f;
                if (transport_dir == TransportDirection::FROM_CAMERA) {
                    scaling = (iorO * iorO) / (iorI * iorI);
                }

                return scaling * rho / absCosTheta(wi);
            }
                // total reflection
            else {
                wi = reflect(wo, n);
                pdf = 1.0f;
                return rho / absCosTheta(wi);
            }
        }
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;

        // set appropriate ior, normal
        float iorO, iorI;
        Vec3f n;
        if (wo[1] > 0) {
            iorO = 1.0f;
            iorI = ior;
            n = Vec3f(0, 1, 0);
        } else {
            iorO = ior;
            iorI = 1.0f;
            n = Vec3f(0, -1, 0);
        }

        // fresnel reflectance
        const float fr = fresnelR(dot(wo, n), iorO, iorI);

        // reflection
        const Vec3f wr = reflect(wo, n);
        ret.emplace_back(wr, fr * rho / absCosTheta(wr));

        // refraction
        Vec3f tr;
        if (refract(wo, n, iorO, iorI, tr)) {
            float scaling = 1.0f;
            if (transport_dir == TransportDirection::FROM_CAMERA) {
                scaling = (iorO * iorO) / (iorI * iorI);
            }

            ret.emplace_back(tr, (1.0f - fr) * scaling * rho / absCosTheta(tr));
        } else {
            ret[0].second = rho / absCosTheta(wr);
        }
        return ret;
    }
};

class Captor : public BxDF {
private:
    Vec3f rho;
    float ior;

public:
    Captor(const Vec3f &rho)
            : BxDF(BxDFType::CAPTOR), rho(rho), ior(1) {}

    // NOTE: delta function
    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        return {0};
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        // set appropriate ior, normal
        wi = -wo;
        return 0;
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;
        return ret;
    }
};

class Transparent : public BxDF {
private:
    Vec3f rho;
    float ior;

public:
    Transparent(const Vec3f &rho, float ior)
            : BxDF(BxDFType::DIFFUSE), rho(rho), ior(ior) {}

    // NOTE: delta function
    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        const float cosThetaO = cosTheta(wo);
        const float cosThetaI = cosTheta(wi);
        if (cosThetaO < 0 || cosThetaI < 0) return {0};

        return rho / PI;
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        // set appropriate ior, normal
        float iorO, iorI;
        Vec3f n;
        if (wo[1] > 0) {
            iorO = 1.0f;
            iorI = ior;
            n = Vec3f(0, 1, 0);
        } else {
            iorO = ior;
            iorI = 1.0f;
            n = Vec3f(0, -1, 0);
        }

        // fresnel reflectance
        const float fr = fresnelR(dot(wo, n), iorO, iorI);

        // reflection
        if (sampler.getNext1D() < fr) {
            wi = reflect(wo, n);
            pdf = 1.0f;
            return rho / absCosTheta(wi);
        }
            // refraction
        else {
            Vec3f tr;
            if (refract(wo, n, iorO, iorI, tr)) {
                wi = tr;
                pdf = 1.0f;

                float scaling = 1.0f;
                if (transport_dir == TransportDirection::FROM_CAMERA) {
                    scaling = (iorO * iorO) / (iorI * iorI);
                }

                return scaling * rho / absCosTheta(wi);
            }
                // total reflection
            else {
                wi = reflect(wo, n);
                pdf = 1.0f;
                return rho / absCosTheta(wi);
            }
        }
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;

        // set appropriate ior, normal
        float iorO, iorI;
        Vec3f n;
        if (wo[1] > 0) {
            iorO = 1.0f;
            iorI = ior;
            n = Vec3f(0, 1, 0);
        } else {
            iorO = ior;
            iorI = 1.0f;
            n = Vec3f(0, -1, 0);
        }

        // fresnel reflectance
        const float fr = fresnelR(dot(wo, n), iorO, iorI);

        // reflection
        const Vec3f wr = reflect(wo, n);
        ret.emplace_back(wr, fr * rho / absCosTheta(wr));

        // refraction
        Vec3f tr;
        if (refract(wo, n, iorO, iorI, tr)) {
            float scaling = 1.0f;
            if (transport_dir == TransportDirection::FROM_CAMERA) {
                scaling = (iorO * iorO) / (iorI * iorI);
            }

            ret.emplace_back(tr, (1.0f - fr) * scaling * rho / absCosTheta(tr));
        } else {
            ret[0].second = rho / absCosTheta(wr);
        }
        return ret;
    }
};

class Refltr : public BxDF {
private:
    Vec3f rho;
    float reflectance;
    float transmittance;
    float roughness;

public:
    Refltr(const Vec3f &rho, float reflectance, float transmittance, float roughness)
            : BxDF(BxDFType::DIFFUSE), rho(rho), reflectance(reflectance), transmittance(transmittance),
              roughness(roughness) {}

    // NOTE: delta function
    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        // when wo, wi is under the surface, return 0
        const float cosThetaO = cosTheta(wo);
        const float cosThetaI = cosTheta(wi);
        if (cosThetaO < 0 || cosThetaI < 0) return {0};

        return rho / PI;
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        Vec3f n;
        if (wo[1] > 0) { // Are we inside or outside the medium ?
            n = Vec3f(0, 1, 0);
        } else {
            n = Vec3f(0, -1, 0);
        }
        

        // reflection
        if (sampler.getNext1D() < reflectance) {
            wi = reflect(wo, n);
            pdf = 1.0f;
            return rho / absCosTheta(wi) + randomInterval(-roughness, roughness);
        }
            // refraction
        else {
            Vec3f tr;
            if (refract(wo, n, tr, transmittance)) {
                wi = tr;
                pdf = 1.0f;
                float scaling = 1.0f;

                return scaling * rho / absCosTheta(wi) + randomInterval(-roughness, roughness);
            }
                // total reflection
            else {
                wi = reflect(wo, n);
                pdf = 1.0f;
                return rho / absCosTheta(wi) + randomInterval(-roughness, roughness);
            }
        }
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        //Unused
        return {};
    };
};

class Leaf : public BxDF {
private:
    Vec3f rho;
    float ior;
    float roughness;

public:
    Leaf(const Vec3f &rho, float ior, float roughness)
            : BxDF(BxDFType::DIFFUSE), rho(rho), ior(ior), roughness(roughness) {}

    // NOTE: delta function
    Vec3f evaluate(Vec3f &wo, Vec3f &wi,
                   TransportDirection &transport_dir) const override {
        // when wo, wi is under the surface, return 0
        const float cosThetaO = cosTheta(wo);
        const float cosThetaI = cosTheta(wi);
        if (cosThetaO < 0 || cosThetaI < 0) return {0};

        return rho / PI;
    }

    Vec3f sampleDirection(Vec3f &wo,
                          TransportDirection &transport_dir,
                          Sampler &sampler, Vec3f &wi,
                          float &pdf) const override {
        // set appropriate ior, normal
        float iorO, iorI;
        Vec3f n;
        if (wo[1] > 0) { // Are we inside or outside the medium ?
            iorO = 1.0f;
            iorI = ior;
            n = Vec3f(0, 1, 0);
        } else {
            iorO = ior;
            iorI = 1.0f;
            n = Vec3f(0, -1, 0);
        }

        // fresnel reflectance
        const float fr = fresnelR(dot(wo, n), iorO, iorI);
        
        
        // reflection
        if (sampler.getNext1D() < fr) {
            wi = reflect(wo, n);
            pdf = 1.0f;
            return rho / absCosTheta(wi) + randomInterval(-roughness, roughness);
        }
            // refraction
        else {
            Vec3f tr;
            if (refract(wo, n, iorO, iorI, tr)) {
                wi = tr;
                pdf = 1.0f;

                float scaling = 1.0f;
                if (transport_dir == TransportDirection::FROM_CAMERA) {
                    scaling = (iorO * iorO) / (iorI * iorI);
                }

                return scaling * rho / absCosTheta(wi) + randomInterval(-roughness, roughness);
            }
                // total reflection
            else {
                wi = reflect(wo, n);
                pdf = 1.0f;
                return rho / absCosTheta(wi) + randomInterval(-roughness, roughness);
            }
        }
    }

    std::vector<DirectionPair> sampleAllDirection(
            Vec3f &wo, TransportDirection &transport_dir) const override {
        std::vector<DirectionPair> ret;

        // set appropriate ior, normal
        float iorO, iorI;
        Vec3f n;
        if (wo[1] > 0) {
            iorO = 1.0f;
            iorI = ior;
            n = Vec3f(0, 1, 0);
        } else {
            iorO = ior;
            iorI = 1.0f;
            n = Vec3f(0, -1, 0);
        }

        // fresnel reflectance
        const float fr = fresnelR(dot(wo, n), iorO, iorI);

        // reflection
        const Vec3f wr = reflect(wo, n);
        ret.emplace_back(wr, fr * rho / absCosTheta(wr));

        // refraction
        Vec3f tr;
        if (refract(wo, n, iorO, iorI, tr)) {
            float scaling = 1.0f;
            if (transport_dir == TransportDirection::FROM_CAMERA) {
                scaling = (iorO * iorO) / (iorI * iorI);
            }

            ret.emplace_back(tr, (1.0f - fr) * scaling * rho / absCosTheta(tr));
        } else {
            ret[0].second = rho / absCosTheta(wr);
        }

        return ret;
    }
};

#endif
