#ifndef _SCENE_H
#define _SCENE_H

#include <embree3/rtcore.h>

#include <boost/filesystem.hpp>
#include <boost/make_shared.hpp>
#include <boost/optional.hpp>
#include <memory>
#include <vector>

#include "../../../externals/tinyobjloader/tiny_obj_loader.h"
#include "core.hpp"
#include "primitive.hpp"

// create default BxDF
boost::shared_ptr<BxDF> createDefaultBxDF() {
    return boost::make_shared<Lambert>(Vec3f(0.9f));
}

// create BxDF from tinyobj material
boost::shared_ptr<BxDF> createBxDF(tinyobj::material_t &material,
                                   float reflectance = 0.0f,
                                   float transmittance = 0.0f, float roughness = 0.0f) {
    const Vec3f kd =
            Vec3f(material.diffuse[0], material.diffuse[1], material.diffuse[2]);
    const Vec3f ks =
            Vec3f(material.specular[0], material.specular[1], material.specular[2]);

    if (material.illum == 2 && (ks == Vec3fZero)) {
        material.illum = 1;
    }

    switch (material.illum) {
        case 2:
            return boost::make_shared<Mirror>(ks);
        case 5:
            // mirror
            return boost::make_shared<Mirror>(Vec3f(1.0f));
        case 6:
            // leaf
            material.ior = 1.425f; // Source:
            // https://opg.optica.org/ao/abstract.cfm?uri=ao-13-1-109
            return boost::make_shared<Leaf>(kd, material.ior, roughness);
        case 7:
            // Transparent
            return boost::make_shared<Transparent>(kd, material.ior);
        case 9:
            return boost::make_shared<SimpleLeaf>(kd, reflectance, transmittance, roughness);
        default:
            // lambert
            return boost::make_shared<Lambert>(kd);
    }
}

// create AreaLight from tinyobj material
boost::shared_ptr<AreaLight> createAreaLight(tinyobj::material_t &material,
                                             Triangle *tri) {
    if (material.emission[0] > 0 || material.emission[1] > 0 ||
        material.emission[2] > 0) {
        Vec3f le =
                Vec3f(material.emission[0], material.emission[1], material.emission[2]);
        return boost::make_shared<AreaLight>(le, tri);
    } else {
        return nullptr;
    }
}

// create PointLight
boost::shared_ptr<PointLight> createPointLight(Vec3f emission, Vec3f position) {
    if (emission[0] > 0 || emission[1] > 0 ||
        emission[2] > 0) {
        Vec3f le =
                Vec3f(emission[0], emission[1], emission[2]);
        return boost::make_shared<PointLight>(le, position);
    } else {
        return nullptr;
    }
}

boost::shared_ptr<SpotLight> createSpotLight(Vec3f emission, Vec3f position, Vec3f direction, float angle) {
    if (emission[0] > 0 || emission[1] > 0 ||
        emission[2] > 0) {
        Vec3f le = Vec3f(emission[0], emission[1], emission[2]);
        return boost::make_shared<SpotLight>(le, position, direction, angle);
    } else {
        return nullptr;
    }
}

boost::shared_ptr<TubeLight> createTubeLight(Vec3f emission, Triangle *tri, Vec3f direction, float angle) {
    if (emission[0] > 0 || emission[1] > 0 ||
        emission[2] > 0) {
        Vec3f le = Vec3f(emission[0], emission[1], emission[2]);
        return boost::make_shared<TubeLight>(le, tri, direction, angle);
    } else {
        return nullptr;
    }
}

class Scene {
private:
    // embree
    RTCDevice device{};
    RTCScene scene{};

    [[nodiscard]] bool hasLight(uint32_t faceID) const { return lights[faceID] != nullptr; }

    void clear() {
        vertices.clear();
        indices.clear();
        normals.clear();
        bxdfs.clear();

        triangles.clear();
        bxdfs.clear();
        lights.clear();
        primitives.clear();
    }

public:
    // mesh data
    // NOTE: assuming size of normals, texcoords == size of vertices
    std::vector<float> vertices;
    std::vector<uint32_t> indices;
    std::vector<float> normals;

    std::vector<boost::optional<tinyobj::material_t>> materials;

    // triangles
    // NOTE: per face
    std::vector<Triangle> triangles;

    // BxDFs
    // NOTE: per face
    std::vector<boost::shared_ptr<BxDF>> bxdfs;

    // lights
    // NOTE: per face
    std::vector<boost::shared_ptr<Light>> lights;

    // primitives
    // NOTE: per face
    std::vector<Primitive> primitives;

    Scene() = default;

    ~Scene() {
        clear();
        rtcReleaseScene(scene);
        rtcReleaseDevice(device);
    }

    void addFaceInfosMat(std::vector<float> vertices,
                         std::vector<uint32_t> indices,
                         std::vector<float> normals, Material mat) {
        for (uint32_t &i: indices) {
            i += nVertices();
        }
        this->vertices.insert(std::end(this->vertices), std::begin(vertices),
                              std::end(vertices));
        this->indices.insert(std::end(this->indices), std::begin(indices),
                             std::end(indices));
        this->normals.insert(std::end(this->normals), std::begin(normals),
                             std::end(normals));

        // populate materials
        for (size_t faceID = nFaces() - (indices.size() / 3); faceID < nFaces();
             ++faceID) {
            tinyobj::material_t m;

            m.diffuse[0] = mat.diffuse[0];
            m.diffuse[1] = mat.diffuse[1];
            m.diffuse[2] = mat.diffuse[2];
            m.ambient[0] = mat.ambient[0];
            m.ambient[1] = mat.ambient[1];
            m.ambient[2] = mat.ambient[2];
            m.emission[0] = 0.00;
            m.emission[1] = 0.00;
            m.emission[2] = 0.00;
            m.specular[0] = mat.specular[0];
            m.specular[1] = mat.specular[1];
            m.specular[2] = mat.specular[2];
            m.shininess = mat.shininess;
            m.dissolve = 1.0f - mat.transparency;
            m.ior = mat.ior;
            if (mat.transparency > 0)
                m.illum = 7;
            else
                m.illum = mat.illum;
            this->materials.emplace_back(m);
            // populate BxDF
            const auto material = this->materials[faceID];
            if (material) {
                tinyobj::material_t m = material.value();
                this->bxdfs.push_back(
                        createBxDF(m, mat.reflectance, mat.transmittance, mat.roughness));
            }
                // default material
            else {
                this->bxdfs.push_back(createDefaultBxDF());
            }
        }
    }

    void addFaceInfos(std::vector<float> &vertices,
                      std::vector<uint32_t> &indices, std::vector<float> &normals,
                      Vec3f &colors, Vec3f &ambient, Vec3f &specular,
                      float &shininess, float &transparency, int &illum,
                      float ior = 0.0f, float reflectance = 0.0f,
                      float transmittance = 0.0f, float roughness = 0.0f) {
        for (uint32_t &i: indices) {
            i += nVertices();
        }

        this->vertices.insert(std::end(this->vertices), std::begin(vertices),
                              std::end(vertices));
        this->indices.insert(std::end(this->indices), std::begin(indices),
                             std::end(indices));
        this->normals.insert(std::end(this->normals), std::begin(normals),
                             std::end(normals));

        // populate materials
        for (size_t faceID = nFaces() - (indices.size() / 3); faceID < nFaces();
             ++faceID) {
            tinyobj::material_t m;

            m.diffuse[0] = colors[0];
            m.diffuse[1] = colors[1];
            m.diffuse[2] = colors[2];
            m.ambient[0] = ambient[0];
            m.ambient[1] = ambient[1];
            m.ambient[2] = ambient[2];
            m.emission[0] = 0.00;
            m.emission[1] = 0.00;
            m.emission[2] = 0.00;
            m.specular[0] = specular[0];
            m.specular[1] = specular[1];
            m.specular[2] = specular[2];
            m.shininess = shininess;
            m.dissolve = 1 - transparency;
            m.ior = ior;
            if (transparency > 0)
                m.illum = 7;
            else
                m.illum = illum;
            this->materials.emplace_back(m);

            // populate BxDF
            const auto material = this->materials[faceID];
            if (material) {
                tinyobj::material_t m = material.value();
                this->bxdfs.push_back(createBxDF(m, reflectance, transmittance, roughness));
            }
                // default material
            else {
                this->bxdfs.push_back(createDefaultBxDF());
            }
        }
    }

    void setupTriangles() {
        // populate  triangles
        for (size_t faceID = 0; faceID < nFaces(); ++faceID) {
            // add triangle
            this->triangles.emplace_back(this->vertices.data(), this->indices.data(),
                                         this->normals.data(), faceID);
        }

        // populate lights, primitives
        for (size_t faceID = 0; faceID < nFaces(); ++faceID) {
            // add light
            boost::shared_ptr<Light> light = nullptr;
            const auto material = this->materials[faceID];
            if (material) {
                tinyobj::material_t m = material.value();
                light = createAreaLight(m, &this->triangles[faceID]);
                if (light != nullptr) {
                    lights.push_back(light);
                }
            }
            // add primitive
            primitives.emplace_back(&this->triangles[faceID], this->bxdfs[faceID],
                                    light);
        }

#ifdef __OUTPUT__
        std::cout << "[Scene] vertices: " << nVertices() << std::endl;
        std::cout << "[Scene] faces: " << nFaces() << std::endl;
        std::cout << "[Scene] lights: " << lights.size() << std::endl;
#endif
    }

    void addLight(std::vector<float> newVertices,
                  std::vector<uint32_t> newIndices, std::vector<float> newNormals,
                  float intensity, Vec3f color) {
        for (uint32_t &i: newIndices) {
            i += nVertices();
        }
        this->vertices.insert(std::end(this->vertices), std::begin(newVertices),
                              std::end(newVertices));
        this->indices.insert(std::end(this->indices), std::begin(newIndices),
                             std::end(newIndices));
        this->normals.insert(std::end(this->normals), std::begin(newNormals),
                             std::end(newNormals));

        // populate  triangles
        for (size_t faceID = nFaces() - (newIndices.size() / 3); faceID < nFaces();
             ++faceID) {
            tinyobj::material_t m;

            m.diffuse[0] = color[0];
            m.diffuse[1] = color[1];
            m.diffuse[2] = color[2];
            m.ambient[0] = 0;
            m.ambient[1] = 0;
            m.ambient[2] = 0;
            m.emission[0] = color[0] * (intensity);
            m.emission[1] = color[1] * (intensity);
            m.emission[2] = color[2] * (intensity);
            m.specular[0] = 0.00;
            m.specular[1] = 0.00;
            m.specular[2] = 0.00;
            m.dissolve = 1.0;
            m.illum = 1;

            this->materials.emplace_back(m);

            // populate BxDF
            const auto material = this->materials[faceID];
            if (material) {
                tinyobj::material_t m = material.value();
                this->bxdfs.push_back(createBxDF(m));
            }
                // default material
            else {
                this->bxdfs.push_back(createDefaultBxDF());
            }
        }
    }

    void addCaptor(std::vector<float> newVertices,
                   std::vector<uint32_t> newIndices, std::vector<float> newNormals) {
        for (uint32_t &i: newIndices) {
            i += nVertices();
        }
        this->vertices.insert(std::end(this->vertices), std::begin(newVertices),
                              std::end(newVertices));
        this->indices.insert(std::end(this->indices), std::begin(newIndices),
                             std::end(newIndices));
        this->normals.insert(std::end(this->normals), std::begin(newNormals),
                             std::end(newNormals));
        for (size_t faceID = nFaces() - (newIndices.size() / 3); faceID < nFaces();
             ++faceID) {
            this->bxdfs.emplace_back(boost::make_shared<Captor>(Vec3f(1, 0, 1)));
        }
    }

    void addPointLight(Vec3f position, float intensity, Vec3f color) {
        boost::shared_ptr<Light> light;
        light = createPointLight(color * intensity, position);
        if (light != nullptr) {
            lights.push_back(light);
        }
    }

    void addSpotLight(Vec3f position, float intensity, Vec3f color, Vec3f direction, float angle) {
        boost::shared_ptr<Light> light;
        light = createSpotLight(color * intensity, position, direction, angle);
        if (light != nullptr) {
            lights.push_back(light);
        }
    }

    void addTubeLight(Triangle *tri, float intensity, Vec3f color, Vec3f direction, float angle) {
        boost::shared_ptr<Light> light;
        light = createTubeLight(color * intensity, tri, direction, angle);
        if (light != nullptr) {
            lights.push_back(light);
        }
    }

    // load obj file
    // TODO: remove vertex duplication
    void loadModel(const std::string &filename) {
        boost::filesystem::path filepath(filename);
        clear();

        // spdlog::info("[Scene] loading: {}", filepath.generic_string());

        tinyobj::ObjReaderConfig reader_config;
        reader_config.mtl_search_path = "./";
        reader_config.triangulate = true;

        tinyobj::ObjReader reader;
        if (!reader.ParseFromFile(filepath.generic_string(), reader_config)) {
            if (!reader.Error().empty()) {
                std::cout << "[Scene] failed to load " << filepath.generic_string()
                          << ": " << reader.Error();
            }
            return;
        }

        if (!reader.Warning().empty()) {
            std::cout << "[Scene] " << reader.Warning() << std::endl;
        }

        const auto &attrib = reader.GetAttrib();
        const auto &shapes = reader.GetShapes();
        const auto &materials = reader.GetMaterials();

        // loop over shapes
        for (const auto &shape: shapes) {
            size_t index_offset = 0;
            // loop over faces
            for (size_t f = 0; f < shape.mesh.num_face_vertices.size(); ++f) {
                const size_t fv = static_cast<size_t>(shape.mesh.num_face_vertices[f]);

                std::vector<Vec3f> vertices;
                std::vector<Vec3f> normals;

                // loop over vertices
                // get vertices, normals, texcoords of a triangle
                for (size_t v = 0; v < fv; ++v) {
                    const tinyobj::index_t idx = shape.mesh.indices[index_offset + v];

                    const tinyobj::real_t vx =
                            attrib.vertices[3 * static_cast<size_t>(idx.vertex_index) + 0];
                    const tinyobj::real_t vy =
                            attrib.vertices[3 * static_cast<size_t>(idx.vertex_index) + 1];
                    const tinyobj::real_t vz =
                            attrib.vertices[3 * static_cast<size_t>(idx.vertex_index) + 2];
                    vertices.push_back(Vec3f(vx, vy, vz));

                    if (idx.normal_index >= 0) {
                        const tinyobj::real_t nx =
                                attrib.normals[3 * static_cast<size_t>(idx.normal_index) + 0];
                        const tinyobj::real_t ny =
                                attrib.normals[3 * static_cast<size_t>(idx.normal_index) + 1];
                        const tinyobj::real_t nz =
                                attrib.normals[3 * static_cast<size_t>(idx.normal_index) + 2];
                        normals.push_back(Vec3f(nx, ny, nz));
                    }
                }

                // if normals is empty, add geometric normal
                if (normals.empty()) {
                    const Vec3f v1 = normalize(vertices[1] - vertices[0]);
                    const Vec3f v2 = normalize(vertices[2] - vertices[0]);
                    const Vec3f n = normalize(cross(v1, v2));
                    normals.push_back(n);
                    normals.push_back(n);
                    normals.push_back(n);
                }

                // populate vertices, indices, normals, texcoords
                for (int i = 0; i < 3; ++i) {
                    this->vertices.push_back(vertices[i][0]);
                    this->vertices.push_back(vertices[i][1]);
                    this->vertices.push_back(vertices[i][2]);

                    this->normals.push_back(normals[i][0]);
                    this->normals.push_back(normals[i][1]);
                    this->normals.push_back(normals[i][2]);

                    this->indices.push_back(this->indices.size());
                }

                // populate materials
                const int materialID = shape.mesh.material_ids[f];
                boost::optional<tinyobj::material_t> material = boost::none;
                if (materialID != -1) {
                    material = materials[materialID];
                }
                this->materials.push_back(material);

                index_offset += fv;
            }
        }

        // populate  triangles
        for (size_t faceID = 0; faceID < nFaces(); ++faceID) {
            // add triangle
            this->triangles.emplace_back(vertices.data(), indices.data(),
                                         normals.data(), faceID);
        }

        // populate bxdfs
        for (size_t faceID = 0; faceID < nFaces(); ++faceID) {
            // add bxdf
            // TODO: remove duplicate
            const auto material = this->materials[faceID];
            if (material) {
                tinyobj::material_t m = material.value();
                if (m.dissolve != 0.0f)
                    this->bxdfs.push_back(createBxDF(m, m.dissolve, 1 - m.dissolve, 0.5f));
                else
                    this->bxdfs.push_back(createBxDF(m));
            }
                // default material
            else {
                this->bxdfs.push_back(createDefaultBxDF());
            }
        }

        // populate lights, primitives
        for (size_t faceID = 0; faceID < nFaces(); ++faceID) {
            // add light
            boost::shared_ptr<Light> light = nullptr;
            const auto material = this->materials[faceID];
            if (material) {
                tinyobj::material_t m = material.value();
                light = createAreaLight(m, &this->triangles[faceID]);
                if (light != nullptr) {
                    lights.push_back(light);
                }
            }

            // add primitive
            primitives.emplace_back(&this->triangles[faceID], this->bxdfs[faceID],
                                    light);
        }
    }

    uint32_t nVertices() const { return vertices.size() / 3; }

    uint32_t nFaces() const { return indices.size() / 3; }

    std::vector<Triangle> getTriangles() const { return triangles; }

    void build() {
#ifdef __OUTPUT__
        std::cout << "[Scene] building scene..." << std::endl;
#endif

        // setup embree
        device = rtcNewDevice(nullptr);
        scene = rtcNewScene(device);

        rtcSetSceneBuildQuality(scene, RTC_BUILD_QUALITY_MEDIUM);
        rtcSetSceneFlags(scene, RTC_SCENE_FLAG_ROBUST);

        RTCGeometry geom = rtcNewGeometry(device, RTC_GEOMETRY_TYPE_TRIANGLE);

        // set vertices
        float *vb = (float *) rtcSetNewGeometryBuffer(
                geom, RTC_BUFFER_TYPE_VERTEX, 0, RTC_FORMAT_FLOAT3, 3 * sizeof(float),
                nVertices());
        for (size_t i = 0; i < vertices.size(); ++i) {
            vb[i] = vertices[i];
        }

        // set indices
        uint32_t *ib = (uint32_t *) rtcSetNewGeometryBuffer(
                geom, RTC_BUFFER_TYPE_INDEX, 0, RTC_FORMAT_UINT3, 3 * sizeof(uint32_t),
                nFaces());
        for (size_t i = 0; i < indices.size(); ++i) {
            ib[i] = indices[i];
        }

        rtcCommitGeometry(geom);
        rtcAttachGeometry(scene, geom);
        rtcReleaseGeometry(geom);
        rtcCommitScene(scene);
    }

    // ray-scene intersection
    bool intersect(const Ray &ray, IntersectInfo &info) const {
        RTCRayHit rayhit{};
        rayhit.ray.org_x = ray.origin[0];
        rayhit.ray.org_y = ray.origin[1];
        rayhit.ray.org_z = ray.origin[2];
        rayhit.ray.dir_x = ray.direction[0];
        rayhit.ray.dir_y = ray.direction[1];
        rayhit.ray.dir_z = ray.direction[2];
        rayhit.ray.tnear = Ray::tmin;
        rayhit.ray.tfar = ray.tmax;
        rayhit.hit.geomID = RTC_INVALID_GEOMETRY_ID;

        RTCIntersectContext context{};
        rtcInitIntersectContext(&context);

        rtcIntersect1(scene, &context, &rayhit);

        if (rayhit.hit.geomID != RTC_INVALID_GEOMETRY_ID) {
            info.t = rayhit.ray.tfar;

            // get triangle shape
            const Triangle &tri = this->triangles[rayhit.hit.primID];

            // set surface info
            info.surfaceInfo.position = ray(info.t);
            info.surfaceInfo.barycentric = Vec2f(rayhit.hit.u, rayhit.hit.v);
            info.surfaceInfo.geometricNormal = tri.getGeometricNormal();
            info.surfaceInfo.shadingNormal =
                    tri.computeShadingNormal(info.surfaceInfo.barycentric);
            orthonormalBasis(info.surfaceInfo.shadingNormal, info.surfaceInfo.dpdu,
                             info.surfaceInfo.dpdv);

            // set primitive
            info.hitPrimitive = &this->primitives[rayhit.hit.primID];

            return true;
        } else {
            return false;
        }
    }

    size_t nLights() const { return lights.size(); }

    boost::shared_ptr<Light> sampleLight(Sampler &sampler, float &pdf) const {
        uint32_t lightIdx = lights.size() * sampler.getNext1D();
        if (lightIdx == lights.size())
            lightIdx--;
        pdf = 1.0f / (lights.size());
        return lights[lightIdx];
    }

    boost::shared_ptr<Light> sampleLight(float &pdf, unsigned int idx) const {
        if (idx == lights.size())
            idx--;
        pdf = 1.0f / (lights.size());
        return lights[idx];
    }
};

#endif
