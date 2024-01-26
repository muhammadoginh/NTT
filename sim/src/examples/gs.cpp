#include <iostream>

int main() {
    int N = 4;
    std::cout << "mulai" << std::endl;

    int t = 1;
    for (int m = N; m > 1; m = m/2) {
        int j1 = 0;
        int h = m/2;
        for (int i = 0; i < h; i++) {
            int j2 = j1 + t - 1;
            for (int j = j1; j <= j2; j++) {
                std::cout << j << std::endl;
                std::cout << j + t << std::endl;
            }
            j1 = j1 + 2 * t;
        }
        t = 2 * t;
    }

    return 0;
}