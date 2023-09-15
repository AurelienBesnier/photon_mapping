// #define __OUTPUT__
#include "camera.h"
#include "image.h"
#include "integrator.h"
#include "scene.h"
#include <chrono>

void Render(UniformSampler &sampler, Image &image, const int &height,
            const int &width, const int &n_samples, const Camera &camera,
            PhotonMapping &integrator, const Scene &scene) {
  const float height_div = 1.0 / height;
#pragma omp parallel for collapse(2) schedule(dynamic, 1)
  for (unsigned i = 0; i < height; ++i) {
    for (unsigned j = 0; j < width; ++j) {
      // init sampler
      sampler = UniformSampler(j + width * i);

      for (unsigned k = 0; k < n_samples; ++k) {
        const float u = (2.0f * (j + sampler.getNext1D()) - width) * height_div;
        const float v =
            (2.0f * (i + sampler.getNext1D()) - height) * height_div;

        Ray ray;
        float pdf;
        if (camera.sampleRay(Vec2f(u, v), ray, pdf)) {
          const Vec3f radiance =
              integrator.integrate(ray, scene, sampler) / pdf;

          if (std::isnan(radiance[0]) || std::isnan(radiance[1]) ||
              std::isnan(radiance[2])) {
            //std::cout<<"radiance is NaN"<<std::endl;
            continue;
          } else if (radiance[0] < 0 || radiance[1] < 0 || radiance[2] < 0) {
              //std::cout<<"radiance is minus"<<std::endl;
            continue;
          }

          image.addPixel(i, j, radiance);
        } else {
          image.setPixel(i, j, Vec3fZero);
        }
      }
    }
  }
}

int main() {
  const unsigned width = 512;
  const unsigned height = 512;
  const unsigned n_samples = 128;
  const unsigned n_photons = 100000;
  const unsigned n_estimation_global = 100;
  const float n_photons_caustics_multiplier = 50;
  const unsigned n_estimation_caustics = 50;
  const unsigned final_gathering_depth = 0;
  const unsigned max_depth = 100;
  Image image(width, height);


    float aspect_ratio = 16.0 / 9.0;
    Vec3f lookfrom(0,5,-7);
    Vec3f lookat(0,0,0);
    Vec3f vup(0,1,0);
    float dist_to_focus = 10.0;
    float aperture = 0.1;
    Camera camera(lookfrom, lookat, vup, 20, aspect_ratio, aperture, dist_to_focus);
  Scene scene;
  scene.loadModel("mesh.obj");
  scene.build();

  // photon tracing and build photon map
  PhotonMapping integrator(n_photons, n_estimation_global,
                           n_photons_caustics_multiplier, n_estimation_caustics,
                           final_gathering_depth, max_depth);
  UniformSampler sampler;

  std::cout<<"[main] building photon map..."<<std::endl;
  auto start = std::chrono::steady_clock::now();
  integrator.build(scene, sampler);
  auto end = std::chrono::steady_clock::now();

  std::chrono::duration<double> elapsed_seconds = end - start;

    std::cout<<"Photonmap building time: "<< elapsed_seconds.count()<<"seconds"<<std::endl;

    std::cout<<"[main] tracing rays from camera..."<<std::endl;

  start = std::chrono::steady_clock::now();
  Render(sampler, image, height, width, n_samples, camera, integrator, scene);
  end = std::chrono::steady_clock::now();

  elapsed_seconds = end - start;

    std::cout<<"Render time: "<< elapsed_seconds.count()<<"seconds"<<std::endl;
  // take average
  image.divide(n_samples);

  image.gammaCorrection(2.2f);
  image.writePPM("output.ppm");
    std::cout<<"[main] wrote to file output.ppm"<<std::endl;
}
