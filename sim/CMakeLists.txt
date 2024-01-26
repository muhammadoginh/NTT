#
# CMakeLists.txt for root directory
#

## This CMakeLists file was intended to set any global configurations.

cmake_minimum_required(VERSION 3.16.3)

project(FFT C CXX)

# Include the CMakeLists.txt in the src directory
add_subdirectory(src)


#--------------------------------------------------------------------
# Include third-party library
#--------------------------------------------------------------------

# Include cereal
add_subdirectory(third-party/cereal)