

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

add_library(spice_core MODULE ext_photonmapping.cpp)
target_link_libraries(spice_core PUBLIC pybind11::module pybind11::opt_size pybind11::thin_lto pybind11::windows_extras
    tinyobjloader embree omp pm)
pybind11_strip(spice_core)
