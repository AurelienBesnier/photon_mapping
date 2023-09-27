#ifndef _PRIMITIVE_H
#define _PRIMITIVE_H

#include <cmath>
#include <memory>
#include <boost/shared_ptr.hpp>
#include <vector>

#include "light.hpp"
#include "material.hpp"
#include "triangle.hpp"

// primitive provides an abstraction layer of the object's shape(triangle),
// material, area light
class Primitive {
public:
    Triangle *triangle;
    boost::shared_ptr<BxDF> bxdf;
    boost::shared_ptr<Light> areaLight;

    Primitive(Triangle *triangle, boost::shared_ptr<BxDF> &bxdf,
              const boost::shared_ptr<Light> &areaLight = nullptr)
            : triangle(triangle), bxdf(bxdf), areaLight(areaLight) {}

    bool hasAreaLight() const;

    // return emission
    Vec3f Le(SurfaceInfo &surfInfo, const Vec3f &dir) const;

    BxDFType getBxDFType() const;

    Vec3f evaluateBxDF(const Vec3f &wo, Vec3f wi,
                       SurfaceInfo &surfInfo,
                       TransportDirection mode) const;

    // sample direction by BxDF
    // its pdf is proportional to the shape od BxDF
    Vec3f sampleBxDF(const Vec3f &wo, SurfaceInfo &surfInfo,
                     TransportDirection mode, Sampler &sampler, Vec3f &wi,
                     float &pdf) const;

    // get all samplable direction
    std::vector<DirectionPair> sampleAllBxDF(
            const Vec3f &wo, SurfaceInfo &surfInfo,
            TransportDirection mode) const;
};

#endif
