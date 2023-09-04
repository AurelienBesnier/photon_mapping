#include "image.h"

Image::Image(unsigned int width, unsigned int height)
            : width(width), height(height) {
        pixels.resize(3 * width * height);
    }

unsigned int Image::getIndex(unsigned int i, unsigned int j) const {
    return 3 * j + 3 * width * i;
}

Vec3f Image::getPixel(unsigned int i, unsigned int j) const {
    const unsigned int idx = getIndex(i, j);
    return {pixels[idx], pixels[idx + 1], pixels[idx + 2]};
}

void Image::addPixel(unsigned int i, unsigned int j, const Vec3f &rgb) {
    const unsigned int idx = getIndex(i, j);
    pixels[idx] += rgb[0];
    pixels[idx + 1] += rgb[1];
    pixels[idx + 2] += rgb[2];
}

void Image::setPixel(unsigned int i, unsigned int j, const Vec3f &rgb) {
    const unsigned int idx = getIndex(i, j);
    pixels[idx] = rgb[0];
    pixels[idx + 1] = rgb[1];
    pixels[idx + 2] = rgb[2];
}

void Image::divide(const float k) {
    for (unsigned int i = 0; i < height; ++i) {
        for (unsigned int j = 0; j < width; ++j) {
            const Vec3f c = getPixel(i, j) / k;
            setPixel(i, j, c);
        }
    }
}

void Image::clear() {
    for (unsigned int i = 0; i < height; ++i) {
        for (unsigned int j = 0; j < width; ++j) {
            setPixel(i, j, 0);
        }
    }
}

void Image::gammaCorrection(const float gamma) {
    for (unsigned int i = 0; i < height; ++i) {
        for (unsigned int j = 0; j < width; ++j) {
            Vec3f c = getPixel(i, j);

            c[0] = std::pow(c[0], 1.0f / gamma);
            c[1] = std::pow(c[1], 1.0f / gamma);
            c[2] = std::pow(c[2], 1.0f / gamma);

            setPixel(i, j, c);
        }
    }
}

void Image::writePPM(const std::string &filename) const {
    std::ofstream file(filename);

    file << "P3" << std::endl;
    file << width << " " << height << std::endl;
    file << "255" << std::endl;

    for (unsigned int i = 0; i < height; ++i) {
        for (unsigned int j = 0; j < width; ++j) {
            const Vec3f rgb = getPixel(i, j);
            const unsigned int R =
                    boost::algorithm::clamp(static_cast<unsigned int>(255.0f * rgb[0]), 0u, 255u);
            const unsigned int G =
                    boost::algorithm::clamp(static_cast<unsigned int>(255.0f * rgb[1]), 0u, 255u);
            const unsigned int B =
                    boost::algorithm::clamp(static_cast<unsigned int>(255.0f * rgb[2]), 0u, 255u);
            file << R << " " << G << " " << B << std::endl;
        }
    }
#ifdef __OUTPUT__
    std::cout<<"[image] wrote to "<<filename<<std::endl;
#endif
    file.close();
}
