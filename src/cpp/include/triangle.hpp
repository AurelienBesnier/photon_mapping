#ifndef SHAPE_H
#define SHAPE_H

#include "core.hpp"
#include "sampler.hpp"

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

    /**
     * @brief Parameterized constructor
     * @param vertices
     * @param indices
     * @param normals
     * @param faceID
     */
    Triangle(float *vertices, unsigned int *indices, float *normals,
             uint32_t faceID);

    /**
     * @brief Returns a vertex's position.
     * @param vertexID The id of the vertex to get.
     * @return The 3D position of the vertex.
     */
    Vec3f getVertexPosition(uint32_t vertexID) const;

    /**
     * @brief Returns a vertex's normal.
     * @param vertexID The id of the vertex to get.
     * @return The normal of the vertex.
     */
    Vec3f getVertexNormal(uint32_t vertexID) const;

    /**
     * @brief Get the indices of the triangle.
     * @return The indices of the Triangle.
     */
    Vec3ui getIndices() const;

    /**
     * @brief Get the geometric normal of the triangle.
     * @return The geometric normal of the Triangle.
     */
    Vec3f getGeometricNormal() const;

    /**
     * Computes the shading normal at a given position.
     * @param barycentric barycentric coordinates to get the normal of.
     * @return The shading normal of the Triangle of the position.
     */
    Vec3f computeShadingNormal(Vec2f &barycentric) const;

    /**
     * @brief Sample a point on the triangle.
     * @param sampler
     * @param pdf
     * @return
     */
    SurfaceInfo samplePoint(Sampler &sampler, float &pdf) const;
};

#endif
