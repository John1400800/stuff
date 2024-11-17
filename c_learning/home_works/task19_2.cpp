#include <cstdlib>
#include <cstdint>
#include <set>
#include <sstream>
#include <algorithm>
#include <iostream>

std::istream& operator>>(std::istream& in, std::set<uint32_t>& set) {
    std::string inputStr;
    while (true) {
        std::getline(in, inputStr);
        std::stringstream sstream(inputStr);
        if (uint32_t num; sstream >> num)
            set.insert(num);
        else if (!inputStr.empty())
            std::cout << "Wrong input, try again\n";
        else
            break;
    }
    return in;
}

template <typename T>
std::ostream& operator<<(std::ostream& out, const std::set<T>& set) {
    for (const T& el : set)
        out << el << ' ';
    return out;
}

template <typename T>
std::set<T> operator-(const std::set<T>& a, const std::set<T>& b) {
    std::set<T> res;
    std::set_difference(a.begin(), a.end(), b.begin(), b.end(), std::inserter(res, res.end()));
    return res;
}

template <typename T>
std::set<T> operator&(const std::set<T>& a, const std::set<T>& b) {
    std::set<T> res;
    std::set_intersection(a.begin(), a.end(), b.begin(), b.end(), std::inserter(res, res.end()));
    return res;
}

int main() {
    std::set<uint32_t> setA, setB;
    std::cout << "Enter set A: ";
    std::cin >> setA;
    std::cout << "Enter set B: ";
    std::cin >> setB;

    std::cout << "A - B: " << (setA - setB) << '\n'
        << "A & B: " << (setA & setB) << '\n'
        << "(A \\ B) & (A & B)=={}: "
        << std::boolalpha << (((setA - setB) & (setA & setB)) == std::set<uint32_t>{}) << '\n';
    return EXIT_SUCCESS;
}
