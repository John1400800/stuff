#include <cassert>
#include <fstream>
#include <sstream>
#include <string>
#include <stdexcept>
#include <iostream>

constexpr bool IS_RELEASE_VERSION{ true };

enum exitState : bool {
    FAILURE = false,
    SUCCESS = true
};

std::string readFile(const char *filename) {
    std::ifstream file(filename);
    if (!file) {
        if constexpr (IS_RELEASE_VERSION)
            assert("Could not open file");
        throw std::runtime_error("Could not open file");
    }
    std::ostringstream oss;
    oss << file.rdbuf();
    return oss.str();
}

void strWrap(std::string& str, size_t maxStrLen) {
    size_t strLen{ 1 };
    size_t lastWhitespaceIdx{ 0 };
    for (size_t i{ 0 }; i < str.length(); ++i, ++strLen) {
        if (str[i] == ' ')
            lastWhitespaceIdx = i;
        if (strLen > maxStrLen && lastWhitespaceIdx) {
            str[lastWhitespaceIdx] = '\n';
            strLen = i - lastWhitespaceIdx;
        } else if (str[i] == '\n')
            str[i] = ' ';
    }
}

size_t countOccurrences(const std::string& str, char search) {
    size_t count{ 0 };
    for (char ch : str)
        if (ch == search)
            ++count;
    return count;
}

int main() {
    std::string filename;
    std::cout << "Enter the name of the file to read: ";
    std::getline(std::cin, filename);

    char searchSymbol;
    std::cout << "Enter the character to search for: ";
    std::cin >> searchSymbol;

    try {
        std::string fileContent{ readFile(filename.c_str()) };

        strWrap(fileContent, 30);

        std::cout << "Source text from file " << filename << ":\n"
                  << fileContent << '\n'
                  << "The character '" << searchSymbol << "' appears "
                  << countOccurrences(fileContent, searchSymbol) << " times.\n";
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
