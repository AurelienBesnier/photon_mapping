set(Boost_USE_STATIC_LIBS OFF)
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME OFF)
set(Boost_USE_RELEASE_LIBS ON)
find_package(Boost REQUIRED)
if (NOT Boost_FOUND)
    message(WARNING "failed to find Boost")
endif ()


find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

add_library(photonmap_core MODULE ext_photonmapping.cpp)
target_link_libraries(photonmap_core PUBLIC pybind11::module pybind11::opt_size pybind11::thin_lto pybind11::windows_extras
        Boost::boost Boost::dynamic_linking tinyobjloader embree omp pm)
pybind11_strip(photonmap_core)
