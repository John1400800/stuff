#include <cstdlib>
#include <cstdint>
#include <cassert>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>

constexpr bool IS_RELEASE_VERSION{ true };
constexpr const char *FILENAME{ "input.txt" };
constexpr char SEARCH_SYMBOL{ 't' };

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
    for (size_t i{ 0 }; i<str.length(); ++i, ++strLen) {
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


int main(int32_t, const char**) {
    std::string fileContent{ readFile(FILENAME) };
    strWrap(fileContent, 30);
    std::cout << "Source text from file" << FILENAME << ":\n"
        << fileContent << '\n'
        << "The character " << SEARCH_SYMBOL << " appears " << countOccurrences(fileContent, SEARCH_SYMBOL) << " times.\n";
    return EXIT_SUCCESS;
}


