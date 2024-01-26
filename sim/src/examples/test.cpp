#include <iostream>

// ini input 2
int ntt(int a, int b) {
    return a + b;
}

// ini input 3
int ntt(int a, int b, int c) {
    return a + b + c;
}

int main() {
    int p = ntt(2, 3);
    int q = ntt(2, 3, 4);
    std::cout << "ini untuk dua input: " << p << std::endl;
    std::cout << "ini untuk tiga input: " << q << std::endl;
    return 0;
}