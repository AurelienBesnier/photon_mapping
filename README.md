[![doc](https://github.com/AurelienBesnier/photon_mapping/actions/workflows/build-docs-upload.yml/badge.svg)](https://aurelienbesnier.github.io/photon_mapping/build/html/index.html)
![package](https://github.com/AurelienBesnier/photon_mapping/actions/workflows/conda-build.yml/badge.svg)

# openalea.spice

minimal but extensible header only implementation of photon mapping in C++.

# How to compile:
*Install Miniforge*: https://github.com/conda-forge/miniforge

Follow installation instructions. Use default installation settings.

Execute next commands in anaconda prompt.

create and activate the conda environment:
```bash
mamba env create -f environment.yml -n photonmap
mamba activate photonmap
```
To install as a Python library:
```bash
python -m pip install ./
```

To compile the source code without installing (useful for debugging):
```bash
mkdir ./build && cd ./build
cmake -DCMAKE_BUILD_TYPE=Debug ../
make -j
```

### Examples
A set of examples can be found in the [`./examples/python`](./examples/python) directory.

## Requirements

* C++ (20>=)
* CMake (3.20>=)
* OpenMP
* [Embree](https://github.com/embree/embree) (>=4)

## Externals

* [Embree](https://github.com/embree/embree)
* [tinyobjloader](https://github.com/tinyobjloader/tinyobjloader)

## Authors
This project was originally developed by [YumcyaWiz](https://github.com/yumcyaWiz/) (Kenta Eto). Main extension were developed by Aurélien Besnier and Nguyen Tuan Minh with contribution of J. Bertheloot, F. Boudon, T. Arsouze, E. Faure.
This work was funded by INRAe Metaprogramme DIGIT-BIO (Digital biology to explore and predict living organisms in their environment). 

## Use case 
This project is used in the coupling of [MorphoNet](https://morphonet.org) and [L-Py](https://github.com/openalea/lpy) for the project Physioscope.

## References

original git: [https://github.com/yumcyaWiz/photon_mapping](https://github.com/yumcyaWiz/photon_mapping)

* Jensen, Henrik Wann. Realistic image synthesis using photon mapping. AK Peters/crc Press, 2001.
* https://pbr-book.org/3ed-2018/Light_Transport_III_Bidirectional_Methods/Stochastic_Progressive_Photon_Mapping# 
* http://www.cs.cmu.edu/afs/cs/academic/class/15462-s12/www/lec_slides/lec18.pdf
* [memoRANDOM](https://rayspace.xyz/)
* [McGuire Computer Graphics Archive](http://casual-effects.com/data/)
* [Rendering Resources | Benedikt Bitterli's Portfolio](https://benedikt-bitterli.me/resources/)
* [Jensen, Henrik Wann. "Global illumination using photon maps." Eurographics workshop on Rendering techniques. Springer, Vienna, 1996.](https://link.springer.com/chapter/10.1007/978-3-7091-7484-5_3)
* Veach, Eric. Robust Monte Carlo methods for light transport simulation. Stanford University, 1998.
* [Christensen, Per H. "Faster photon map global illumination." Journal of graphics tools 4.3 (1999): 1-10.](https://doi.org/10.1080/10867651.1999.10487505)
* [Hachisuka, Toshiya, Jacopo Pantaleoni, and Henrik Wann Jensen. "A path space extension for robust light transport simulation." ACM Transactions on Graphics (TOG) 31.6 (2012): 1-10.](https://dl.acm.org/doi/10.1145/2366145.2366210)
