#include "fft.hpp"
#include <iostream>

// using namespace fft::helper;

int main() {
    int n_bits = fft::helper::upper_log2(4);

    std::cout << n_bits << '\n';
    
    return 0;
}