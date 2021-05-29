#!/bin/sh
rm -rf ./lib
cythonize -i ./source/discrimination.pyx
cythonize -i ./source/mapping.pyx
cythonize -i ./source/input_data.pyx
cythonize -i ./source/create_new_mesh.pyx
cythonize -i ./source/input_v.pyx

cythonize -i ./source/solver.pyx

mkdir ./lib
cp ./source/*.c ./lib/
cp ./source/*.so ./lib/
rm ./source/*.c
rm ./source/*.so