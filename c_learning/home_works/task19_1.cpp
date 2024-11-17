#include <cstdlib>
#include <cstdint>
#include <cctype>
#include <set>
#include <limits>
#include <iostream>

int main(int32_t argc, const char** argv) {
    std::string inputStr{};
    if (argc > 1)
        for (size_t i{1}; i<argc; ++i)
            inputStr += argv[i];
    else {
        std::cout << "Введите строку: ";
        std::getline(std::cin >> std::ws, inputStr, '.');
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    std::cout << "Уникальные символы в строке: ";
    for (char chr : std::set<char>(inputStr.begin(), inputStr.end()))
        if (!isspace(chr))
            std::cout << chr << ' ';
    std::cout << '\n';
    return EXIT_SUCCESS;
}
