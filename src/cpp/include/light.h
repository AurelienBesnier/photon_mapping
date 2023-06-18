#ifndef _LIGHT_H
#define _LIGHT_H

#include "core.h"
#include "sampler.h"
#include "triangle.h"

enum LightType{
    Area, PointL
};
// light interface
class Light {
 public:
    virtual ~Light() = default;
  virtual Vec3f Le(const SurfaceInfo& info, const Vec3f& dir) = 0;
  virtual SurfaceInfo samplePoint(Sampler& sampler, float& pdf) = 0;
  virtual Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler& sampler,
                                float& pdf) = 0;
};

class PointLight : public Light {
private:
    Vec3f le;  // emission
    Vec3f position;

public:
    PointLight(Vec3f& le, Vec3f position)
            : le(le), position(position) {}

    Vec3f Le(const SurfaceInfo& info, const Vec3f& dir) override{
        return le;
    }

    SurfaceInfo samplePoint(Sampler& sampler, float& pdf) override{
        SurfaceInfo surfInfo;
        surfInfo.position = position;

        return surfInfo;
    }

    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler& sampler,
                                  float& pdf) override {
        Vec3f dir = sampleCosineHemisphere(sampler.getNext2D(), pdf);

        // transform direction from local to world
        return localToWorld(dir, surfInfo.dpdu, surfInfo.shadingNormal,
                            surfInfo.dpdv);
    }
};

class AreaLight : public Light {
 private:
  Vec3f le;  // emission
  Triangle* triangle;

 public:
  AreaLight(const Vec3f& le, Triangle* triangle)
      : le(le), triangle(triangle) {
  }

  // return emission
  Vec3f Le(const SurfaceInfo& info, const Vec3f& dir) override {
    return le;
  }

  // sample point on the light
  SurfaceInfo samplePoint(Sampler& sampler, float& pdf) override {
    return triangle->samplePoint(sampler, pdf);
  }

  // sample direction from the light
  Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler& sampler,
                        float& pdf) override {
      Vec3f dir = sampleCosineHemisphere(sampler.getNext2D(), pdf);
      Vec3f wo = localToWorld(dir, surfInfo.dpdu, surfInfo.shadingNormal,
                              surfInfo.dpdv);

    // transform direction from local to world
    return wo;
  }
};

#endif