#ifndef PRIMITIVE_H
#define PRIMITIVE_H

#include <cmath>
#include <memory>
#include <vector>

#include "light.hpp"
#include "material.hpp"
#include "triangle.hpp"
#include <string>

/**
 * Primitive provides an abstraction layer of the object's shape(triangle),
 * material, area light
 * @class
 */
class Primitive
{
      public:
        Triangle* triangle;         ///< The triangles of the primitive.
        std::shared_ptr<BxDF> bxdf; ///< A pointer of the bxdf of the primitive.
        std::shared_ptr<Light>
          areaLight; ///< a pointer towards the Light source of the primitive
                     ///< (nullptr if not a light)
        std::string name;

        Primitive(Triangle* triangle,
                  std::shared_ptr<BxDF>& bxdf,
                  std::string name,
                  const std::shared_ptr<Light>& areaLight = nullptr)
          : triangle(triangle)
          , bxdf(bxdf)
          , areaLight(areaLight)
          , name(name)
        {
        }

        /**
         * @brief Gets whether the primitive has an area light or not.
         */
        bool hasAreaLight() const;

        /**
         * @brief Returns the emission of the surface of the primitive.
         * @param surfInfo The surface info of the primitive.
         * @param dir The direction of light emission.
         * @return The light emission in RGB (Vec3).
         */
        Vec3f Le(SurfaceInfo& surfInfo, const Vec3f& dir) const;

        /**
         * @brief Get the type of bxdf of the primitive.
         * @return The type of bxdf of the primitive
         */
        BxDFType getBxDFType() const;

        Vec3f evaluateBxDF(const Vec3f& wo,
                           Vec3f wi,
                           SurfaceInfo& surfInfo,
                           TransportDirection mode) const;

        /**
         * @brief sample direction by BxDF. its pdf is proportional to the shape
         * of BxDF
         * @param wo
         * @param surfInfo
         * @param mode
         * @param sampler
         * @param wi
         * @param pdf
         * @return the direction result.
         */
        Vec3f sampleBxDF(const Vec3f& wo,
                         SurfaceInfo& surfInfo,
                         TransportDirection mode,
                         Sampler& sampler,
                         Vec3f& wi,
                         float& pdf) const;

        /**
         * @brief Get all samplable directions.
         * @param wo
         * @param surfInfo
         * @param mode
         * @return a vector of DirectionPair.
         */
        std::vector<DirectionPair> sampleAllBxDF(const Vec3f& wo,
                                                 SurfaceInfo& surfInfo,
                                                 TransportDirection mode) const;
};

#endif
