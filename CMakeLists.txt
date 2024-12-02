cmake_minimum_required(VERSION 3.20)
project(photon_mapping LANGUAGES CXX)

include_directories("${CMAKE_SOURCE_DIR}/src/cpp/include/")

option(BUILD_TESTS "build c++ tests" OFF)
option(BUILD_CXX_EXAMPLE "build c++ example" OFF)
set(CMAKE_IGNORE_PATH "/usr/local")


# --- Build setup

find_package(TBB CONFIG REQUIRED)
find_package(Threads REQUIRED)


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

if(WIN32)
	message(STATUS "Compiling on windows")
    set(CMAKE_C_COMPILER gcc)
    set(CMAKE_CXX_COMPILER g++)
endif()

find_package(OpenMP)
if(NOT OpenMP_CXX_FOUND)
    message(WARNING "failed to find OpenMP")
endif()

# Embree3
find_package(embree 4.0 REQUIRED)
if (${embree_FOUND})
  message(STATUS "Found Embree")
  set("EMBREE_MAX_ISA" ON)
else()
  message(FATAL_ERROR "Could not find Embree")
endif()

# externals
add_subdirectory("externals")

add_subdirectory("src/cpp/include")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++2b -fsigned-char -fexceptions -fopenmp -march=native")

# pm(photon_mapping)
add_library(pm INTERFACE src/python/ext_photonmapping.cpp)
target_include_directories(pm INTERFACE "src/cpp/include")

target_compile_features(pm INTERFACE cxx_std_23)
set_target_properties(pm
        PROPERTIES
        CXX_STANDARD 23
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS NO
        )


target_link_libraries(pm INTERFACE OpenMP::OpenMP_CXX tinyobjloader embree)
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
        LIBRARY DESTINATION "${CMAKE_SOURCE_DIR}/src/openalea/photonmap/")
