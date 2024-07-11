# Install script for directory: /home/tmnguyen/Bureau/photon_mapping

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/home/tmnguyen/anaconda3/envs/photonmap/bin/x86_64-conda-linux-gnu-objdump")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/tmnguyen/Bureau/photon_mapping/build/temp.linux-x86_64-cpython-312/photonmap/libphotonmap_core/externals/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/tmnguyen/Bureau/photon_mapping/build/temp.linux-x86_64-cpython-312/photonmap/libphotonmap_core/src/cpp/include/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/tmnguyen/Bureau/photon_mapping/build/temp.linux-x86_64-cpython-312/photonmap/libphotonmap_core/examples/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/tmnguyen/Bureau/photon_mapping/build/temp.linux-x86_64-cpython-312/photonmap/libphotonmap_core/src/python/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/home/tmnguyen/Bureau/photon_mapping/build/temp.linux-x86_64-cpython-312/photonmap/libphotonmap_core/src/cpp/test/cmake_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "python" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/tmnguyen/Bureau/photon_mapping/photonmap" TYPE MODULE FILES "/home/tmnguyen/Bureau/photon_mapping/build/lib.linux-x86_64-cpython-312/photonmap/libphotonmap_core.so")
  if(EXISTS "$ENV{DESTDIR}/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/home/tmnguyen/anaconda3/envs/photonmap/bin/x86_64-conda-linux-gnu-strip" "$ENV{DESTDIR}/home/tmnguyen/Bureau/photon_mapping/photonmap/libphotonmap_core.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
  file(WRITE "/home/tmnguyen/Bureau/photon_mapping/build/temp.linux-x86_64-cpython-312/photonmap/libphotonmap_core/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
