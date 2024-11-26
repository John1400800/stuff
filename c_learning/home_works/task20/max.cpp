#include <cstdint>

template <typename T>
T max(T a, T b) {
    return a > b ? a : b;
}

template uint32_t max(uint32_t, uint32_t);
