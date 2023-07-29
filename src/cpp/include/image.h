#ifndef _IMAGE_H
#define _IMAGE_H

#include <boost/algorithm/clamp.hpp>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "core.h"

class Image {
private:
    unsigned width;
    unsigned height;

    unsigned getIndex(unsigned i, unsigned j) const;

public:
    std::vector<float> pixels;

    Image(unsigned width, unsigned height);

    Vec3f getPixel(unsigned i, unsigned j) const;

    void addPixel(unsigned i, unsigned j, const Vec3f &rgb);

    void setPixel(unsigned i, unsigned j, const Vec3f &rgb);

    void divide(const float k);

    void clear();

    void gammaCorrection(const float gamma);
    void writePPM(const std::string &filename) const;
};

#endif
