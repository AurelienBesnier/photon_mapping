#ifndef LIGHT_H
#define LIGHT_H

#include "core.hpp"
#include "sampler.hpp"
#include "triangle.hpp"

/**
 * @enum  Represent the type of a light object.
 */
enum LightType {
    Area, ///< Area light source
    PointL, ///< Point light source
    SpotL, ///< Spot light source
    TubeL, ///< Tube light source
    Directional ///< Directional light source (Sun)
};

/**
 * @brief Abstract class representing a light source.
 * @class Light
 */
class Light {
public:
    virtual ~Light() = default;

    /**
    * @fn Vec3f Le() override
    * Get the light emission of the light source.
    * @returns the le attribute.
    */
    virtual Vec3f Le() = 0;

    virtual SurfaceInfo samplePoint(Sampler &sampler, float &pdf) = 0;

    virtual Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler &sampler, float &pdf) = 0;
};

/**
 * @brief Class representing a Point Light.
 * @class PointLight
 * This light source does not have a physical presence.
 */
class PointLight : public Light {
private:
    Vec3f le;  // emission
    Vec3f position;

public:
    PointLight(Vec3f &le, Vec3f position) : le(le), position(position) {
    }

    /**
    * @fn Vec3f Le() override
    * Get the light emission of the light source.
    * @return the le attribute.
    */
    Vec3f Le() override {
        return le;
    }

    SurfaceInfo samplePoint(Sampler &sampler, float &pdf) override {
        SurfaceInfo surfInfo;
        surfInfo.position = position;
        surfInfo.point = true;

        return surfInfo;
    }

    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler &sampler, float &pdf) override {
        float y = randomInterval(-1.0f, 1.0f);
        float angle = randomInterval(0.0, PI_MUL_2);
        float r = sqrtf(1.0f - y * y);
        float x = r * sinf(angle);
        float z = r * cosf(angle);

        return {x, y, z};
    }
};

/**
 * @brief Class representing a Spot Light.
 * @class SpotLight
 * This light source does not have a physical presence.
 */
class SpotLight : public Light {
private:
    Vec3f le;  // emission
    Vec3f position;
    Vec3f direction;
    float angle;

public:
    SpotLight(Vec3f &le, Vec3f position, Vec3f direction, float angle) : le(le), position(position),
                                                                         direction(direction), angle(angle) {
    }

    /**
    * @fn Vec3f Le() override
    * Get the light emission of the light source.
    * @returns the le attribute.
    */
    Vec3f Le() override {
        return le;
    }

    SurfaceInfo samplePoint(Sampler &sampler, float &pdf) override {
        SurfaceInfo surfInfo;
        surfInfo.position = position;
        surfInfo.point = true;

        return surfInfo;
    }


    /**
     * Get the direction vector a new photon.
      * @param surfInfo
      * @param sampler
      * @param pdf
      * @return
      */
    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler &sampler, float &pdf) override {
        float rad = deg2rad(angle);
        float y = randomInterval(-rad, rad);
        float theta = randomInterval(0.0, rad * 2);
        float r = sqrtf(1.0f - y * y);
        float x = r * sinf(theta);
        float z = r * cosf(theta);

        Vec3f dir(x, y, z);
        dir += direction;
        return dir;
    }
};

/**
 * @brief Class representing a Tube Light.
 * @class TubeLight
 * This light source has a physical presence in the scene.
 */
class TubeLight : public Light {
private:
    Vec3f le;  // emission
    Triangle *triangle;
    Vec3f direction;
    float angle;

public:
    TubeLight(const Vec3f &le, Triangle *triangle, Vec3f direction, float angle) : le(le), triangle(triangle),
                                                                                   direction(direction), angle(angle) {
    }

    /**
    * @fn Vec3f Le() override
    * Get the light emission of the light source.
    * @returns the le attribute.
    */
    Vec3f Le() override {
        return le;
    }

    /**
    * @fn SurfaceInfo samplePoint(Sampler& sampler, float& pdf) override
    * Samples a point on the mesh of the light source.
    * @param sampler
    * @param pdf
    * @return
    */
    SurfaceInfo samplePoint(Sampler &sampler, float &pdf) override {
        return triangle->samplePoint(sampler, pdf);
    }

    /**
     * Get the direction vector a new photon.
     * @param surfInfo
     * @param sampler
     * @param pdf
     * @return
     */
    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler &sampler, float &pdf) override {
        float rad = deg2rad(angle);
        float y = randomInterval(-rad, rad);
        float theta = randomInterval(0.0, rad * 2);
        float r = sqrtf(1.0f - y * y);
        float x = r * sinf(theta);
        float z = r * cosf(theta);

        Vec3f dir(x, y, z);
        dir += direction;
        return dir;
    }
};

/**
 * @brief Class representing an Area Light.
 * @class AreaLight
 * This light source has a physical presence in the scene.
 */
class AreaLight : public Light {
private:
    Vec3f le;  // emission
    Triangle *triangle;

public:
    AreaLight(const Vec3f &le, Triangle *triangle) : le(le), triangle(triangle) {
    }

    /**
    * @fn Vec3f Le() override
    * Get the light emission of the light source.
    * @returns the le attribute.
    */
    Vec3f Le() override {
        return le;
    }


    /**
     * @fn SurfaceInfo samplePoint(Sampler& sampler, float& pdf) override
     * Samples a point on the mesh of the light source.
     * @param sampler
     * @param pdf
     * @return
     */
    SurfaceInfo samplePoint(Sampler &sampler, float &pdf) override {
        return triangle->samplePoint(sampler, pdf);
    }

    /**
     * Get the direction vector a new photon.
     * @param sampler
     * @param pdf
     * @return
     */
    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler &sampler, float &pdf) override {
        Vec3f dir = sampleCosineHemisphere(sampler.getNext2D(), pdf);
        Vec3f wo = localToWorld(dir, surfInfo.dpdu, surfInfo.shadingNormal, surfInfo.dpdv);

        // transform direction from local to world
        return wo;
    }
};

#endif
