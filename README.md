[![doc](https://github.com/AurelienBesnier/photon_mapping/actions/workflows/build-docs-upload.yml/badge.svg)](https://minhlucky9.github.io/photon_mapping/build/html/index.html)
![package](https://github.com/AurelienBesnier/photon_mapping/actions/workflows/python-package-conda.yml/badge.svg)

# photon_mapping

minimal but extensible header only implementation of photon mapping in C++.

# How to compile:
create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate photonmap
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

# How to run example:

```bash
conda activate photonmap
cd examples/python/plantgl-rad-scene
python planglRadScene.py
```

* The result of the simulation is in the folder: [./results/](https://github.com/minhlucky9/photon_mapping/tree/main/examples/python/plantgl-rad-scene/results)
* Tools to evalutate result: [.examples/python/Evaluation Simulation SEC2/](https://github.com/minhlucky9/photon_mapping/tree/main/examples/python/Evaluation%20Simulation%20SEC2)


![](img/cornellbox-water_pm.png)

# How to run the jupyter notebook

```bash
    conda activate photonmap
    pip install pgljupyter

    cd examples/python/plantgl-rad-scene
    jupyter notebook
```
## Features

* Direct illumination with explicit light sampling
* Indirect illumination with final gathering
* Caustics photon map
* Load obj model

## Requirements

* C++ (20>=)
* CMake (3.20>=)
* OpenMP
* [Embree](https://github.com/embree/embree) (>=3)

## Externals

* [Embree](https://github.com/embree/embree)
* [tinyobjloader](https://github.com/tinyobjloader/tinyobjloader)

## Authors
This project was originaly developed by [YumcyaWiz](https://github.com/yumcyaWiz/) (Kenta Eto). Main extension were developed by Aurélien Besnier and Nguyen Tuan Minh with contribution of J. Bertheloot, F. Boudon, T. Arsouze, E. Faure.
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
