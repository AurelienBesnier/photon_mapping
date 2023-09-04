#!/usr/bin/bash

conda activate photonmap
python -m pip install .
cd examples/python
python ./main.py
cd ../../