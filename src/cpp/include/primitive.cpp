#include "primitive.hpp"

bool Primitive::hasAreaLight() const { return areaLight != nullptr; }

// return emission
Vec3f Primitive::Le(SurfaceInfo &surfInfo, const Vec3f &dir) const {
    return areaLight->Le();
}

BxDFType Primitive::getBxDFType() const { return bxdf->getType(); }

Vec3f Primitive::evaluateBxDF(const Vec3f &wo, Vec3f wi,
                              SurfaceInfo &surfInfo,
                              TransportDirection mode) const {
// world to local transform
    Vec3f wo_l =
            worldToLocal(wo, surfInfo.dpdu, surfInfo.shadingNormal, surfInfo.dpdv);
    Vec3f wi_l =
            worldToLocal(wi, surfInfo.dpdu, surfInfo.shadingNormal, surfInfo.dpdv);

    return bxdf->evaluate(wo_l, wi_l, mode);
}

// sample direction by BxDF
// its pdf is proportional to the shape od BxDF
Vec3f Primitive::sampleBxDF(const Vec3f &wo, SurfaceInfo &surfInfo,
                            TransportDirection mode, Sampler &sampler, Vec3f &wi,
                            float &pdf) const {
    // world to local transform
    Vec3f wo_l =
            worldToLocal(wo, surfInfo.dpdu, surfInfo.shadingNormal, surfInfo.dpdv);

// sample direction in tangent space
    Vec3f wi_l;
    Vec3f f = bxdf->sampleDirection(wo_l, mode, sampler, wi_l, pdf);

// local to world transform
    wi = localToWorld(wi_l, surfInfo.dpdu, surfInfo.shadingNormal,
                      surfInfo.dpdv);

    return f;
}

// get all samplable direction
std::vector<DirectionPair> Primitive::sampleAllBxDF(
        const Vec3f &wo, SurfaceInfo &surfInfo,
        TransportDirection mode) const {
// world to local transform
    Vec3f wo_l =
            worldToLocal(wo, surfInfo.dpdu, surfInfo.shadingNormal, surfInfo.dpdv);

// sample all direction in tangent space
    std::vector<DirectionPair> dir_pairs = bxdf->sampleAllDirection(wo_l, mode);

// local to world transform
    for (DirectionPair &dp: dir_pairs)
        dp.first = localToWorld(dp.first, surfInfo.dpdu, surfInfo.shadingNormal,
                                surfInfo.dpdv);


    return dir_pairs;
}
