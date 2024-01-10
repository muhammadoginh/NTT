#!/bin/bash

# Create a build directory if it doesn't exist
mkdir -p ../sim/build

# Change to the build directory
cd ../sim/build

# Run CMake to generate build files
cmake ..

# Build the simulation executable
make

# Run the simulation executable
./simulation