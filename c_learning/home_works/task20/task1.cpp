#include <iostream>
#include "max.hpp"

int main(int32_t, const char **) {
    std::cout << "Поочережно введитке a b: ";
    uint32_t a, b;
    std::cin >> a >> b;
    std::cout << "большее: " << max(a, b) << '\n';
    return EXIT_SUCCESS;
}
