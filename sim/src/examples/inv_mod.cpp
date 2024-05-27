#include <iostream>

int mod_inv(int x, int p) {
    int b = p;
    int a = 0, r = 1;
    // if (p == 1) return 1;
    while (x > 1) {
        int q = x / p;
        int temp = x;
        x = p;
        p = temp % p;

        int prev_a = a;
        a = r - q * a;
        r = prev_a;
    }
    if (r < 0) r += b;
    return r;
}

int main() {
    int x;
    int p;

    std::cout << "Masukkan nilai x: ";
    std::cin >> x;
    std::cout << "Masukkan nilai p: ";
    std::cin >> p;
    std::cout << mod_inv(x,p) << std::endl;
    
}