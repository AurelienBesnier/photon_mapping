#ifndef _SHAPE_H
#define _SHAPE_H
#include "core.h"
#include "sampler.h"

/**
 * @brief Class representing a triangle in the scene.
 * @class Triangle
 */
class Triangle {
public:
  float *vertices; ///< The vertices of the triangle.
  unsigned *indices; ///< The indices of the triangle.
  float *normals; ///< The normals of the triangle.

  uint32_t faceID; ///< The faceID of the triangle.
  Vec3f geometricNormal; ///< The geometric normal of the triangle.
  float surfaceArea;  ///< The surface area of the triangle.

  Triangle(float *vertices, unsigned int *indices, float *normals,
           uint32_t faceID);

  // return vertex position
  Vec3f getVertexPosition(uint32_t vertexID) const;

  // return vertex normal
  Vec3f getVertexNormal(uint32_t vertexID) const;

  // return vertex indices
  Vec3ui getIndices() const;

  // return geometric normal
  Vec3f getGeometricNormal() const;

  // compute shading normal at given position
  Vec3f computeShadingNormal(Vec2f &barycentric) const;

  // sample point on the triangle
  SurfaceInfo samplePoint(Sampler &sampler, float &pdf) const;
};

#endif
