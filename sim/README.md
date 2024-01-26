# FFT
FFT and IFFT implementation in C++ using Cooley Tukey algorithm
> Based on: https://github.com/AndaOuyang/FFT

## Directory Structure
The below trees describes the structure of this repostitory.
```
.
├── build
|   └── bin
|       └── example
|
├── src
|   ├── example
|   ├── include
|   └── lib
|
└── third-party
    └── cereal
```

## The descriptions of library components
| Directory   | Description      |
|:------------|:-----------------|
| build       | Binaries and build scripts (this folder is created by the user).  |
| src         | this folder contain three folders, example is ```main``` function, you can locate header file in include folder, and implementation of header file in lib folder |
| third-party | this folder contain external library which include as submodule.  |


#### Instuction for build the project
* clone this repo
* Create a directory where the binaries will be built. The typical choice is a subfolder “build”. In this case, the commands are:  
  * ```mkdir build```
  * ```cd build```
  * ```cmake ..```
  * ```make```