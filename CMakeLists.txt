cmake_minimum_required(VERSION 3.20)
project(photon_mapping LANGUAGES CXX)

include_directories("${CMAKE_SOURCE_DIR}/src/cpp/include/")

option(BUILD_TESTS "build tests" ON)
option(BUILD_CXX_EXAMPLE "build c++ example" ON)
set(CMAKE_IGNORE_PATH "/usr/local")
# --- Build setup

find_package(TBB CONFIG REQUIRED)
find_package(Threads REQUIRED)

find_package(Boost REQUIRED)
if(NOT Boost_FOUND)
    message(WARNING "failed to find Boost")
endif()
set(Boost_USE_MULTITHREAD ON)

# OpenMP
if(APPLE)
    set(CMAKE_C_COMPILER clang)
    set(CMAKE_CXX_COMPILER clang++)

    if(CMAKE_C_COMPILER_ID MATCHES "Clang\$")
        set(OpenMP_C_FLAGS "-Xpreprocessor -fopenmp")
        set(OpenMP_C_LIB_NAMES "omp")
        set(OpenMP_omp_LIBRARY omp)
    endif()

    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang\$")
        set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp")
        set(OpenMP_CXX_LIB_NAMES "omp")
        set(OpenMP_omp_LIBRARY omp)
    endif()
endif()

find_package(OpenMP)
if(NOT OpenMP_CXX_FOUND)
    message(WARNING "failed to find OpenMP")
endif()

# Embree4
find_package(embree 3.0 REQUIRED)
if (${embree_FOUND})
  message(STATUS "Found Embree")
else()
  message(FATAL_ERROR "Could not find Embree")
endif()

# externals
add_subdirectory("externals")

add_subdirectory("src/cpp/include")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++20 -DLINUX -fsigned-char -fexceptions -fopenmp -O3")

# pm(photon_mapping)
add_library(pm INTERFACE src/python/ext_photonmapping.cpp)
target_include_directories(pm INTERFACE "src/cpp/include")

target_compile_features(pm INTERFACE cxx_std_20)
set_target_properties(pm PROPERTIES CXX_EXTENSIONS OFF)

set_target_properties(pm
        PROPERTIES
        CXX_STANDARD 20
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS OFF
        )

target_link_libraries(pm INTERFACE OpenMP::OpenMP_CXX)
target_link_libraries(pm INTERFACE tinyobjloader)
target_link_libraries(pm INTERFACE embree)
target_link_libraries(pm INTERFACE ${Boost_LIBRARIES})
target_link_libraries(pm INTERFACE photon_map primitive triangle image)

# examples
if(BUILD_CXX_EXAMPLE)
    add_subdirectory("examples")
endif ()

# wrapper
add_subdirectory("src/python/")

# tests
if(BUILD_TESTS)
    add_subdirectory("src/cpp/test")
endif()

# building lib
find_package(Python COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

install(TARGETS photonmap_core
        COMPONENT python
        LIBRARY DESTINATION "${CMAKE_SOURCE_DIR}/photonmap/")
