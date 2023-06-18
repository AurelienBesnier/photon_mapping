find_package(Boost REQUIRED)
if(NOT Boost_FOUND)
    message(WARNING "failed to find Boost")
endif()
set(Boost_USE_MULTITHREAD ON)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++20 -DLINUX -fsigned-char -fexceptions")

find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

add_library(photonmap_core MODULE ext_photonmapping.cpp)
target_link_libraries(photonmap_core PUBLIC pybind11::module pybind11::opt_size ${Boost_LIBRARIES} tinyobjloader embree omp)
pybind11_strip(photonmap_core)