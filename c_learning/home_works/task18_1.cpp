#include <cmath>
#include <chrono>
#include <random>
#include <type_traits>
#include <vector>
#include <iostream>

class Randgen {
    static std::mt19937 helpInitMt() {
        std::random_device rd{};
        std::seed_seq seedSeq {
            static_cast<std::seed_seq::result_type>(
                std::chrono::steady_clock::now().time_since_epoch().count(), 
                rd(), rd(), rd(), rd(), rd(), rd(), rd()) };
        return std::mt19937{ seedSeq };
    }
    inline static std::mt19937 state{ helpInitMt() };
public:
    template <typename T>
    using RandomFunc = T(*)(const T&, const T&);

    template <typename T>
    static T get(const T& min, const T& max) {
        if constexpr (std::is_integral<T>::value) {
            return std::uniform_int_distribution<T>(min, max)(state);
        } else if constexpr (std::is_floating_point<T>::value) {
            return std::uniform_real_distribution<T>(min, max)(state);
        } else {
            static_assert(std::is_arithmetic<T>::value, "Unsupported type for Randgen::get");
        }
    }
};

template <typename T>
constexpr T abs(T n) {
    return n<0 ? -n : n;
}

template <typename T>
void swap(T& a, T& b) {
    T temp{a};
    a = b;
    b = temp;
}

template <typename T>
std::ostream& operator<<(std::ostream& out, const std::vector<T>& vec) {
    bool isFirst{true};
    for (double el : vec) {
        out << (isFirst?"":", ") /*<< std::setprecision(3)*/ << el;
        isFirst = false;
    }
    return out;
}

template <typename T>
void initVecWithRandomNum(std::vector<T>& vec, Randgen::RandomFunc<T> func=Randgen::get<T>) {
    for (double& el : vec) {
        el = func(0., 2.)>1 ? func(-100., 100) : 0;
        el = trunc(el * 100) / 100;
    }
}

template <typename T>
const T& findAbsMax(const std::vector<T>& vec) {
    const T *absMax{&vec[0]};
    for (size_t i{1}; i<vec.size(); ++i)
        if (abs(vec[i]) > abs(*absMax))
            absMax = &vec[i];
    return *absMax;
}

template <typename T>
void moveZerosToTheEnd(std::vector<T>& vec) {
    size_t lnz{ vec.size() - 1};
    for (size_t i = 0; i < lnz; ++i) {
        if (vec[i] == 0) {
            while (lnz > i && vec[lnz] == 0)
                --lnz;
            std::swap(vec[i], vec[lnz]);
        }
    }
}

int main(int32_t, const char**) {
    std::cout << "Enter number of elements in arr: ";
    size_t size;
    std::cin >> size;
    std::vector<double> vec(size);
    initVecWithRandomNum(vec);
    std::cout << vec << '\n' << findAbsMax(vec) << '\n';
    moveZerosToTheEnd(vec);
    std::cout << vec << '\n';
    return EXIT_SUCCESS;
}
