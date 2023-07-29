#define __OUTPUT__

#include <pybind11/pybind11.h>
#include <pybind11/stl_bind.h>
#include <pybind11/operators.h>
#include <boost/shared_ptr.hpp>
#include "../cpp/include/camera.h"
#include "../cpp/include/image.h"
#include "../cpp/include/photon_map.h"
#include "../cpp/include/material.h"
#include "../cpp/include/integrator.h"

namespace py = pybind11;

PYBIND11_MAKE_OPAQUE(std::vector<float>)
PYBIND11_MAKE_OPAQUE(std::vector<uint32_t>)
PYBIND11_MAKE_OPAQUE(std::vector<int>)
PYBIND11_MAKE_OPAQUE(std::vector<Triangle>)
PYBIND11_MAKE_OPAQUE(std::vector<Primitive>)
PYBIND11_MAKE_OPAQUE(std::vector<Vec3f>)

void visualizePhotonMap(const Scene &scene, Image &image, const int &width, const int &height, const Camera &camera, const int & n_photons, const int &max_depth, const std::string_view &filename)
{
    // photon tracing and build photon map
    PhotonMapping integrator(n_photons, 1, 0, 0, 0, max_depth);
    UniformSampler sampler;
    integrator.build(scene, sampler);

    // visualize photon map
    const PhotonMap photon_map = integrator.getPhotonMapGlobal();
#pragma omp parallel for collapse(2) schedule(dynamic, 1)
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
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

    image.writePPM(filename.data());
}


void visualizePhotonMaps(const Scene &scene, Image &image, const int &width, const int &height, const Camera &camera, const int & n_photons, const int &max_depth, const std::string &filename)
{
    // photon tracing and build photon map
    PhotonMapping integrator(n_photons, 1, 0, 0, 0, max_depth);
    UniformSampler sampler;
    integrator.build(scene, sampler);

    // visualize photon map
    const std::vector<PhotonMap> photon_maps = integrator.getLightsPhotonMap();
    int cpt = 0;
    for(const PhotonMap& photon_map: photon_maps) {
#pragma omp parallel for collapse(2) schedule(dynamic, 1)
        for (int i = 0; i < height; ++i) {
            for (int j = 0; j < width; ++j) {
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
                            const Photon &photon = photon_map.getIthPhoton(photon_idx);
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
        cpt++;
        image.writePPM(filename+"_"+std::to_string(cpt)+".ppm");
        image.clear();
    }

}

void Render(UniformSampler& sampler, Image& image, const int &height, int width, int n_samples, Camera& camera, PhotonMapping& integrator, Scene& scene, std::string_view& filename)
{
#pragma omp parallel for collapse(2) schedule(dynamic, 1)
    for (int i = 0; i < height; ++i) {
        for (int j = 0; j < width; ++j) {
            // init sampler
            sampler = UniformSampler(j + width * i);

            for (int k = 0; k < n_samples; ++k) {
                const float u = (2.0f * (j + sampler.getNext1D()) - width) / height;
                const float v = (2.0f * (i + sampler.getNext1D()) - height) / height;

                Ray ray;
                float pdf;
                if (camera.sampleRay(Vec2f(u, v), ray, pdf)) {
                    const Vec3f radiance =
                            integrator.integrate(ray, scene, sampler) / pdf;

#ifndef __OUTPUT__
                    if (std::isnan(radiance[0]) || std::isnan(radiance[1]) ||
                        std::isnan(radiance[2])) {
                        std::cerr << "radiance is NaN" << std::endl;
                        continue;
                    } else if (radiance[0] < 0 || radiance[1] < 0 || radiance[2] < 0) {
                        std::cerr << "radiance is minus" << std::endl;
                        continue;
                    }
#endif
                    image.addPixel(i, j, radiance);
                } else {
                    image.setPixel(i, j, Vec3fZero);
                }
            }
        }
    }
    image.divide(n_samples);
    image.writePPM(filename.data());
}

PYBIND11_MODULE(libphotonmap_core, m) {
    m.doc() = "pybind11 module for photon mapping";

    py::bind_vector<std::vector<float>>(m, "VectorFloat", py::module_local(false));
    py::bind_vector<std::vector<unsigned int>>(m, "VectorUint", py::module_local(false));
    py::bind_vector<std::vector<long>>(m, "VectorInt", py::module_local(false));
    py::bind_vector<std::vector<unsigned char>>(m, "VectorUchar", py::module_local(false));
    py::bind_vector<std::vector<Triangle>>(m, "VectorTriangle", py::module_local(false));

    py::class_<Material>(m, "Material")
            .def(py::init<>())
            .def_readwrite("diffuse", &Material::diffuse)
            .def_readwrite("specular", &Material::specular)
            .def_readwrite("ambient", &Material::ambient)
            .def_readwrite("transparency", &Material::transparency)
            .def_readwrite("illum", &Material::illum)
            .def_readwrite("shininess", &Material::shininess)
            .def_readwrite("ior", &Material::ior);

    //Photonmap
    py::class_<Photon>(m, "Photon")
            .def(py::init<>())
            .def(py::init<Vec3<float>&, Vec3<float>&, Vec3<float>&, unsigned int>())
            .def_readwrite("throughput", &Photon::throughput)
            .def_readwrite("position", &Photon::position)
            .def_readonly("triId", &Photon::triId)
            .def_readwrite("wi", &Photon::wi);

    py::class_<KdTree<Photon>>(m, "KdTree")
            .def(py::init<>())
            .def("buildTree", &KdTree<Photon>::buildTree)
            .def("setPoints", &KdTree<Photon>::setPoints, "Sets the points of the kdtree", py::arg("points"), py::arg("nPoints"));

    py::class_<PhotonMap>(m, "PhotonMap")
            .def(py::init<>())
            .def("getIthPhoton", &PhotonMap::getIthPhoton, "Returns the ith photon of the photon map", py::arg("i"))
            .def("setPhotons", &PhotonMap::setPhotons, "Sets the photons of the photon map", py::arg("photons"))
            .def("nPhotons", &PhotonMap::nPhotons, "Returns the size of the photonmap")
            .def("build", &PhotonMap::build, "Builds the photon map")
            .def("queryKNearestPhotons", &PhotonMap::queryKNearestPhotons, "Returns the k nearest photons of the photon p", py::arg("p"), py::arg("k"), py::arg("max_dist2"));


    //Image
    py::class_<Image>(m, "Image")
            .def(py::init<unsigned int, unsigned int>())
            .def_readwrite("pixels", &Image::pixels)
            .def("addPixel", &Image::addPixel, "adds the rgb value to the pixel of coord i j", py::arg("i"), py::arg("j"), py::arg("rgb"))
            .def("getPixel", &Image::getPixel, py::arg("i"), py::arg("j"))
            .def("setPixel", &Image::setPixel, py::arg("i"), py::arg("j"), py::arg("rgb"))
            .def("divide", &Image::divide, "Divide all the pixel of the image by k", py::arg("k"))
            .def("gammaCorrection", &Image::gammaCorrection, py::arg("gamma"))
            .def("writePPM", &Image::writePPM, "Write the image to the filename (.ppm file)", py::arg("filename"));

    //Camera
    py::class_<Camera>(m, "Camera")
            .def(py::init<Vec3<float>, Vec3<float>, float>())
            .def("sampleRay", &Camera::sampleRay, py::arg("uv"), py::arg("ray"), py::arg("pdf"));

    //Integrator
    //PhotonMapping class
    py::class_<PhotonMapping>(m, "PhotonMapping")
            .def(py::init<int, int, float, int, int, int>())
            .def("build", &PhotonMapping::build, py::arg("scene"), py::arg("sampler"))
            .def("integrate", &PhotonMapping::integrate, py::arg("ray_in"), py::arg("scene"), py::arg("sampler"))
            .def("getPhotonMap", &PhotonMapping::getPhotonMapGlobal, "Returns the photon map", py::return_value_policy::reference)
            .def("getPhotonMapC", &PhotonMapping::getPhotonMapCaustics, "Returns the caustics photon map",py::return_value_policy::reference);

    //Lights
    py::enum_<LightType>(m, "LightType")
            .value("Area", Area)
            .value("PointL", PointL)
            .export_values();

    //Area light
    py::class_<AreaLight>(m, "AreaLight")
            .def(py::init<Vec3f,  Triangle*>())
            .def("Le", &AreaLight::Le)
            .def("samplePoint", &AreaLight::samplePoint)
            .def("sampleDirection", &AreaLight::sampleDirection);



    //Triangle
/*    py::class_<Triangle>(m, "Triangle")
            .def(py::init<float*, uint32_t*, float*, uint32_t>());*/


    py::class_<Primitive>(m, "Primitive")
            .def(py::init<Triangle*, boost::shared_ptr<BxDF>&, const boost::shared_ptr<Light>&>())
            .def("hasAreaLight", &Primitive::hasAreaLight)
            .def("Le", &Primitive::Le, py::arg("surfInfo"), py::arg("dir"))
            .def("getBxDFType", &Primitive::getBxDFType)
            .def("evaluateBxDF", &Primitive::evaluateBxDF, py::arg("wo"), py::arg("wi"), py::arg("surfInfo"), py::arg("mode"))
            .def("sampleBxDF", &Primitive::sampleBxDF, py::arg("wo"), py::arg("surfInfo"), py::arg("mode"), py::arg("sampler"), py::arg("wi")
            , py::arg("pdf"))
            .def("sampleAllBxDF", &Primitive::sampleAllBxDF, py::arg("wo"), py::arg("surfInfo"), py::arg("mode"));


    //Sampler
    py::class_<Sampler>(m, "Sampler");

    py::class_<UniformSampler, Sampler>(m, "UniformSampler")
            .def(py::init<>())
            .def(py::init<uint64_t>())
            .def("clone", &UniformSampler::clone, "Function to clone the sampler")
            .def("getNext1D", &UniformSampler::getNext1D, py::return_value_policy::reference)
            .def("getNext2D", &UniformSampler::getNext2D, py::return_value_policy::reference);

    m.def("sampleCosineHemisphere", &sampleCosineHemisphere, py::arg("uv"), py::arg("pdf"));

    //Core
    //Constants
    m.attr("PI") = py::float_(PI);
    m.attr("PI_MUL_2") = py::float_(PI_MUL_2);
    m.attr("PI_MUL_4") = py::float_(PI_MUL_4);
    m.attr("PI_INV") = py::float_(PI_INV);
    m.attr("RAY_EPS") = py::float_(RAY_EPS);

    //Vec2
    py::class_<Vec2<float>>(m, "Vec2", py::dynamic_attr())
            .def(py::init<>())
            .def(py::init<float>())
            .def(py::init<float,float>())
            .def(py::self + py::self)
            .def(py::self + float())
            .def(py::self += py::self)
            .def(py::self *= float())
            .def(float() * py::self)
            .def(py::self * float())
            .def(-py::self)
            .def("__setitem__", [](Vec2<float> &self, int index, float val)
            { self[index] = val; })
            .def("__getitem__", [](Vec2<float> &self, int index)
            { return self[index]; });

    //Vec3
    py::class_<Vec3<float>>(m, "Vec3", py::dynamic_attr())
            .def(py::init<>())
            .def(py::init<float>())
            .def(py::init<float,float,float>())
            .def(py::self + py::self)
            .def(py::self + float())
            .def(py::self += py::self)
            .def(py::self *= float())
            .def(float() * py::self)
            .def(py::self * float())
            .def("__setitem__", [](Vec3<float> &self, int index, float val)
            { self[index] = val; })
            .def("__getitem__", [](Vec3<float> &self, int index)
            { return self[index]; });

    //Vec3
    py::class_<Vec3<uint32_t>>(m, "Vec3Ui")
            .def(py::init<>())
            .def(py::init<uint32_t>())
            .def(py::init<uint32_t,uint32_t,uint32_t>())
            .def(py::self + py::self)
            .def(py::self += py::self)
            .def(py::self *= float())
            .def(float() * py::self)
            .def(py::self * float())
            .def("__setitem__", [](Vec3<uint32_t> &self, int index, uint32_t val)
            { self[index] = val; })
            .def("__getitem__", [](Vec3<uint32_t> &self, int index)
            { return self[index]; });

    py::class_<Ray>(m, "Ray")
            .def(py::init<>())
            .def(py::init<Vec3<float>, Vec3<float>>())
            .def_readwrite("direction", &Ray::direction);

    //SurfaceInfo
    py::class_<SurfaceInfo>(m, "SurfaceInfo")
            .def_readwrite("position", &SurfaceInfo::position)
            .def_readwrite("geometricNormal", &SurfaceInfo::geometricNormal)
            .def_readwrite("shadingNormal", &SurfaceInfo::shadingNormal)
            .def_readwrite("dpdu", &SurfaceInfo::dpdu)
            .def_readwrite("dpdv", &SurfaceInfo::dpdv)
            .def_readwrite("texcoords", &SurfaceInfo::texcoords)
            .def_readwrite("barycentric", &SurfaceInfo::barycentric);

    //Scene
    py::class_<Scene>(m, "Scene")
            .def(py::init<>())
            .def_readwrite("triangles", &Scene::triangles)
            .def_readwrite("vertices", &Scene::vertices)
            .def_readwrite("normals", &Scene::normals)
            .def("loadModel", &Scene::loadModel, "Function to load a model in the scene, must be an .obj file path"
                    , py::arg("filepath"))
            .def("setupTriangles", &Scene::setupTriangles)
            .def("addFaceInfosMat", &Scene::addFaceInfosMat,
                 py::arg("vertices"), py::arg("indices"), py::arg("normals"), py::arg("material"))
            .def("addFaceInfos", &Scene::addFaceInfos, py::arg("vertices"), py::arg("indices"),
                 py::arg("normals"), py::arg("colors"), py::arg("ambient"), py::arg("specular"), py::arg("shininess"), py::arg("transparency"), py::arg("illum"),
                 py::arg("ior"), py::arg("reflectance"),py::arg("transmittance"))
            .def("addLight", &Scene::addLight, py::arg("vertices"), py::arg("indices"), py::arg("normals"), py::arg("intensity"), py::arg("color"))
            .def("build", &Scene::build)
            .def("getTriangles", &Scene::getTriangles, "Returns an array with the triangles of the scene")
            .def("intersect", &Scene::intersect, py::arg("ray"), py::arg("info"))
            .def("sampleLight", py::overload_cast<Sampler&, float&>(&Scene::sampleLight, py::const_), py::arg("sampler"), py::arg("pdf"))
            .def("sampleLight", py::overload_cast<float&, int>(&Scene::sampleLight, py::const_), py::arg("pdf"), py::arg("idx"))
            .def("nVertices", &Scene::nVertices , "Function that returns the number of vertices in the scene" )
            .def("nFaces", &Scene::nFaces, "Function that returns the number of faces in the scene");

    //IntersectInfo
    py::class_<IntersectInfo>(m, "IntersectInfo")
            .def(py::init<>())
            .def_readonly("t", &IntersectInfo::t)
            .def_readonly("surfaceInfo", &IntersectInfo::surfaceInfo);

    m.def("Render",&Render, "Function to render the scene to an image from the camera perspective", py::arg("sampler"), py::arg("image"), py::arg("height"),
          py::arg("width"), py::arg("n_samples"), py::arg("camera"), py::arg("integrator"),
          py::arg("scene"), py::arg("filename"));
    m.def("visualizePhotonMap", &visualizePhotonMap, "Function to visualize the photonmap as a .ppm image", py::arg("Scene"), py::arg("image"), py::arg("width"),
          py::arg("height"), py::arg("camera"), py::arg("n_photons"), py::arg("max_depth"), py::arg("filename"));
    m.def("visualizePhotonMaps", &visualizePhotonMaps, "Function to visualize the photonmap of each light source as a .ppm image", py::arg("Scene"), py::arg("image"), py::arg("width"),
          py::arg("height"), py::arg("camera"), py::arg("n_photons"), py::arg("max_depth"), py::arg("filename"));
}
