#include "image.h"

int main() {
  const unsigned width = 512;
  const unsigned height = 512;

  Image image(width, height);
  for (unsigned i = 0; i < height; ++i) {
    const float u = static_cast<float>(i) / height;
    for (unsigned j = 0; j < width; ++j) {
      const float v = static_cast<float>(j) / height;
      image.setPixel(i, j, Vec3f(u, v, 1.0f));
    }
  }

  image.writePPM("output.ppm");

  return 0;
}