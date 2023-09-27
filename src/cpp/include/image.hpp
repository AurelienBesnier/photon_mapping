#ifndef IMAGE_H
#define IMAGE_H

#include <boost/algorithm/clamp.hpp>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "core.hpp"

/**
 * @brief Class representing an Image.
 * @class Image
 * @author Aurelien Besnier
 */
class Image {
private:
    unsigned width; ///< The width of the image in pixels.
    unsigned height; ///< The height of the image in pixels.
    std::vector<float> pixels; ///< The pixels of the image (RowMajor order).


    unsigned getIndex(unsigned i, unsigned j) const;

public:

    /**
     * @brief Constructor
     * Allocate the memory necessary for the image.
     * @param width
     * @param height
     */
    Image(unsigned width, unsigned height);

    /**
     * @fn Vec3f getPixel(unsigned i, unsigned j) const
     * @brief Returns the color of the pixel of the given coordinates.
     * @param i
     * @param j
     * @return
     */
    Vec3f getPixel(unsigned i, unsigned j) const;

    /**
     * @fn void addPixel(unsigned i, unsigned j, const Vec3f &rgb)
    * @brief Adds the given color to the pixel of the given coordinates.
    * @param i
    * @param j
    * @return
    */
    void addPixel(unsigned i, unsigned j, const Vec3f &rgb);

    /**
    * @fn void setPixel(unsigned i, unsigned j, const Vec3f &rgb)
    * @brief Sets the pixel pixel of the given coordinates at a certain color.
    * @param i
    * @param j
    * @return
    */
    void setPixel(unsigned i, unsigned j, const Vec3f &rgb);

    /**
     * @fn void divide(const float &k);
     * @brief Divide every pixels by a number.
     * @param k the divider
     */
    void divide(const float &k);

    /**
     * Sets every pixels to zero.
     */
    void clear();

    void gammaCorrection(const float &gamma);

    /**
     * @fn void writePPM(const std::string &filename) const
     * @brief Write the image to the given filename to the .ppm format.
     * https://fr.wikipedia.org/wiki/Portable_pixmap
     * @param filename
     */
    void writePPM(const std::string &filename) const;
};

#endif
