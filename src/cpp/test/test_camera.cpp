#include "camera.h"
#include "image.h"

int main() {
  const unsigned width = 512;
  const unsigned height = 512;
    float aspect_ratio = 16.0 / 9.0;
    Vec3f lookfrom(0,0,0);
    Vec3f lookat(0,0,0);
    Vec3f vup(0,1,0);
    float dist_to_focus = 10.0;
    float aperture = 0.1;
    Camera camera(lookfrom, lookat, vup, 20, aspect_ratio, aperture, dist_to_focus);

  Image image(width, height);
  for (unsigned i = 0; i < height; ++i) {
    for (unsigned j = 0; j < width; ++j) {
      const float u = (2.0f * j - width) / height;
      const float v = (2.0f * i - height) / height;

      Ray ray;
      float pdf;
      if (camera.sampleRay(Vec2f(u, v), ray, pdf)) {
        image.setPixel(i, j, 0.5f * (ray.direction + 1.0f));
      } else {
        image.setPixel(i, j,Vec3fZero);
      }
    }
  }

  image.writePPM("output.ppm");

  return 0;
}