#include <iostream>

int main() {
    int N = 4;
    std::cout << "mulai" << std::endl;

    for (int i = 1; i < N; i = 2*i) {
        // std::cout << i << std::endl;
        for (int j = 0; j < i; j++) {
            // std::cout << j << std::endl;
            for (int k = j*N/i; k < (2*j+1)*N/(2*i); k++) {
                std::cout << k << std::endl;
                std::cout << k + N/(2*i) << std::endl;
            }
        }
    }
    
    return 0;
}