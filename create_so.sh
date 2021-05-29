#!/bin/sh
rm -rf ./lib
mkdir ./lib
cythonize -i ./source/discrimination.pyx lib/
cythonize -i ./source/mapping.pyx lib/
cythonize -i ./source/input_data.pyx lib/
cythonize -i ./source/create_new_mesh.pyx lib/
cythonize -i ./source/input_v.pyx lib/

cythonize -i ./source/solver.pyx lib/

mkdir ./lib
cp ./source/*.c ./lib/
cp ./source/*.so ./lib/
rm ./source/*.c
rm ./source/*.so