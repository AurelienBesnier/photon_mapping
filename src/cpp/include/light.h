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
            : le(le), position(position) {

        std::cout<<"Point light at: "<<position<<std::endl;
    }

    Vec3f Le(const SurfaceInfo& info, const Vec3f& dir) override{
        return le;
    }

    SurfaceInfo samplePoint(Sampler& sampler, float& pdf) override{
        SurfaceInfo surfInfo;
        surfInfo.position = position;
        surfInfo.point = true;

        return surfInfo;
    }

    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler& sampler,
                                  float& pdf) override {
        float y = randomInterval(-1.0f,1.0f);
        float angle = randomInterval(0.0, PI_MUL_2);
        float r = sqrtf(1.0f-y*y);
        float x = r*sinf(angle);
        float z = r*cos(angle);

        return {x,y,z};
    }
};


class SpotLight : public Light {
private:
    Vec3f le;  // emission
    Vec3f position;
    Vec3f direction;
    float angle;

public:
    SpotLight(Vec3f& le, Vec3f position, Vec3f direction, float angle)
            : le(le), position(position), direction(direction), angle(angle) {

        std::cout<<"Spot light at: "<<position<<std::endl;
    }

    Vec3f Le(const SurfaceInfo& info, const Vec3f& dir) override{
        return le;
    }

    SurfaceInfo samplePoint(Sampler& sampler, float& pdf) override{
        SurfaceInfo surfInfo;
        surfInfo.position = position;
        surfInfo.point = true;

        return surfInfo;
    }

    Vec3f sampleDirection(const SurfaceInfo &surfInfo, Sampler& sampler,
                          float& pdf) override {

        float theta = randomInterval(deg2rad(angle), deg2rad(angle - PI_MUL_2));
        std::cout<<"theta"<<theta<<std::endl;
        direction += theta;

        return direction;
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
