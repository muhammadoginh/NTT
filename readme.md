# Key Switching

In this project we implement keyswicthing based on OpenFHE data io

## Barrett reduction

- This Modular reduction uses the [barrett reduction](https://ieeexplore.ieee.org/document/10177902)

## How to run the code type

Example to run the code in terminal:

1. ```iverilog -o Half_Adder_tb.vvp Half_Adder_tb.v```
2. ```vvp Half_Adder_tb.vvp```

## Directory Structure

The below trees describes the structure of this repostitory.
```
.
│
├── rtl/
│
├── scripts/
│   └── run_simulation.sh
│
├── sim/
│   ├── CMakeLists.txt
│   └── build/
│
├── testbenches/
│
├── tests/
│
├── CMakeLists.txt
└── README.md
```

## The descriptions of directory components
| Directory   | Description      |
|:------------|:-----------------|
| rtl         | This directory typically contains your Verilog/SystemVerilog RTL (Register-Transfer Level) code, which represents the hardware description of your digital design.  |
| scripts     | This directory may contain scripts related to your project. Scripts are often used for automation tasks, such as compiling and running simulations. You can store Python scripts related to simulation setup, testing, or verification. |
| sim         | This directory is dedicated to simulation-related files.  |
| testbenches | This directory contains testbench files that you use to simulate and verify the functionality of your RTL code. Testbenches are used to apply inputs to your design and observe the outputs.  |
| tests       | This directory is dedicated for unit tests. If you have Python scripts containing unit tests for your Verilog code, you can placing them here. Each Verilog module or a set of related modules can have its own Python test file. |