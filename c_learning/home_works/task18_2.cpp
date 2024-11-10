#include <cstdlib>
#include <chrono>
#include <random>
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

template <typename T, size_t N>
using Vector = T*[N];

using Vec100PtrtoFloat = Vector<float, 100>;

// for T*[N]
template <typename T, size_t N>
void del(Vector<T, N>& vec) {
    for (size_t i{0}; i<N; ++i)
        if (vec[i])
            for (size_t j{i+1}; j<N; ++j)
                if (vec[j] && *vec[i] == *vec[j])
                    vec[j] = nullptr;
}

template <typename T, size_t N>
std::ostream& operator<<(std::ostream& out, const Vector<T, N>& vec) {
    for (size_t i{0}; i<N; ++i)
        if (vec[i])
        out << (i>0 ? ", ": "") << *vec[i];
    return out;
}

template <typename T, size_t N>
std::istream& operator>>(std::istream& in, Vector<T, N>& vec) {
    for (size_t i{0}; i<N; ++i) {
        T val;
        in >> val;
        vec[i] = new T{val};
    }
    return in;
}

constexpr auto min{-100};
constexpr auto max{ 100};

template <typename T, size_t N>
void fillRandom(Vector<T, N>& vec, Randgen::RandomFunc<T> func=Randgen::get<T>) {
    for (size_t i{0}; i<N; ++i)
        vec[i] = new T{func(min, max)};
}

template <typename T, size_t N>
void fillOneToNine(Vector<T, N>& vec) {
    for (size_t i{0}; i<100; ++i)
        vec[i] = new float{(float)(i % 10)};
}

// std::vector
template <typename T>
void del(std::vector<T>& vec) {
    size_t N = vec.size();
    for (size_t i{0}; i<N; ++i)
        if (vec[i])
            for (size_t j{i+1}; j<N; ++j)
                if (vec[j] && *vec[i] == *vec[j])
                    vec[j] = nullptr;
}

template <typename T>
std::ostream& operator<<(std::ostream& out, const std::vector<T>& vec) {
    size_t N = vec.size();
    for (size_t i{0}; i<N; ++i)
        if (vec[i])
        out << (i>0 ? ", ": "") << *vec[i];
    return out;
}

template <typename T>
std::istream& operator>>(std::istream& in, std::vector<T>& vec) {
    size_t N = vec.size();
    for (size_t i{0}; i<N; ++i) {
        T val;
        in >> val;
        vec[i] = new T{val};
    }
    return in;
}

template <typename T>
void fillRandom(std::vector<T>& vec, Randgen::RandomFunc<T> func=Randgen::get<T>) {
    size_t N = vec.size();
    for (size_t i{0}; i<N; ++i)
        vec[i] = new T{func(min, max)};
}

template <typename T>
void fillOneToNine(std::vector<T>& vec) {
    size_t N = vec.size();
    for (size_t i{0}; i<100; ++i)
        vec[i] = new float{(float)(i % 10)};
}


int main() {
    Vec100PtrtoFloat vec1{};
    fillOneToNine(vec1);
    std::cout << vec1 << '\n';
    del(vec1);
    std::cout << vec1 << '\n';

    std::vector<float*> vec2(100);
    fillOneToNine(vec2);
    std::cout << vec2 << '\n';
    del(vec2);
    std::cout << vec2 << '\n';
    return EXIT_SUCCESS;
}
