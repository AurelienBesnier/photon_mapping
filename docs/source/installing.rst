Installation
###############################

Installing from sources
=======================

Before starting to install the library, you should first install all dependencies in a conda environment. The simplest way to do this is to call

.. code-block:: bash
    
    mamba env create -f environment.yml -n spice

You have to activate the conda environment before installing

.. code-block:: bash
    
    mamba activate spice

To install as a Python library:

.. code-block:: bash
    
    pip install ./

To run test
===========

The main example is located in the folder ./examples/python/plantgl-rad-scene

.. code-block:: bash
    
    mamba activate spice
    cd examples/python/plantgl-rad-scene

Command to run the example

.. code-block:: bash
    
    python planglRadScene.py

To run the Jupyter Notebook
===========================
Here is the command to run the Jupyter notebook

.. code-block:: bash
    
    cd docs/examples/python/plantgl-rad-scene
    jupyter notebook