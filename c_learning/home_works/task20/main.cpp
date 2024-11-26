#include <cstdlib>
#include <cstdint>
#include <iostream>

#include "max.hpp"

int main(int32_t, const char **) {
    std::cout << "Поочережно введитке a и b: ";
    uint32_t a, b;
    std::cin >> a >> b;
    std::cout << "болбшее из a и b: " << max(a, b) << '\n';
    return EXIT_SUCCESS;
}
