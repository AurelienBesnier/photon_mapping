#include <omp.h>

#include "camera.h"
#include "image.h"
#include "integrator.h"
#include "photon_map.h"
#include "scene.h"

int main() {
  const int width = 512;
  const int height = 512;
  const int n_photons = 1000000;
  const int max_depth = 100;

  Image image(width, height);
  Camera camera(Vec3f(0, 1, 7), Vec3f(0, 0, -1), 0.25 * PI);

  Scene scene;
  scene.loadModel("cornell_box.obj");
  scene.build();

  // photon tracing and build photon map
  PhotonMapping integrator(n_photons, 1, 0, 0, 0, max_depth);
  UniformSampler sampler;
  integrator.build(scene, sampler);

  // visualize photon map
  std::cout<<"[main] visualizing photon map"<<std::endl;

  const PhotonMap photon_map = integrator.getPhotonMapGlobal();

#pragma omp parallel for collapse(2)
  for (size_t i = 0; i < height; ++i) {
    for (size_t j = 0; j < width; ++j) {
      const float u = (2.0f * j - width) / height;
      const float v = (2.0f * i - height) / height;
      Ray ray;
      float pdf;
      if (camera.sampleRay(Vec2f(u, v), ray, pdf)) {
        IntersectInfo info;
        if (scene.intersect(ray, info)) {
          // query photon map
          float r2;
          const std::vector<int> photon_indices =
              photon_map.queryKNearestPhotons(info.surfaceInfo.position, 1,
                                               r2);
          const int photon_idx = photon_indices[0];

          // if distance to the photon is small enough, write photon's
          // throughput to the image
          if (r2 < 0.001f) {
            const Photon& photon = photon_map.getIthPhoton(photon_idx);
            image.setPixel(i, j, photon.throughput);
          }
        } else {
          image.setPixel(i, j, Vec3fZero);
        }
      } else {
        image.setPixel(i, j, Vec3fZero);
      }
    }
  }

  image.writePPM("output.ppm");

  return 0;
}
