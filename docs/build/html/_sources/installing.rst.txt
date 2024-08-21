Installing Photon Mapping tools
##############

Installing from sources
=======================

Before starting to install the Photon Mapping tools, you should first install all dependencies in a conda environment. The simplest way to do this is to call

.. code-block:: bash
    
    conda env create -f environment.yml

You have to activate the conda environment before installing

.. code-block:: bash
    
    conda activate photonmap

To install as a Python library:

.. code-block:: bash
    
    python -m pip install ./

To run test
========================

The main example is located in the folder ./examples/python/plantgl-rad-scene

.. code-block:: bash
    
    conda activate photonmap
    cd examples/python/plantgl-rad-scene

Command to run the example

.. code-block:: bash
    
    python planglRadScene.py

To run the Jupyter Notebook
===========================

We have to install the dependencies first. Here is ``pgljupyter``

.. code-block:: bash
    
    conda activate photonmap
    pip install pgljupyter

Here is the command to run the Jupyter notebook

.. code-block:: bash
    
    cd examples/python/plantgl-rad-scene
    jupyter notebook