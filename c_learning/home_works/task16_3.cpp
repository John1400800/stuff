#include <cstdlib>      // for EXIT_SUCCESS, abs
#include <cstdint>      // for int32_t
#include <list>         // std::list
#include <string>       // std::string
#include <string_view>  // std::string_view
#include <utility>      // for std::pair
#include <iostream>     // std::cout, std::cin

// #define DEBUG_PRINT

using Term = std::pair<int32_t, int32_t>;

Term parseStrToTerm(std::string_view term) {
    int32_t cfcnt { 1 },
            degree{ 1 };
    size_t xPos{ term.find('x') };
    if (xPos == std::string_view::npos) { // if x not exist
        cfcnt = std::stoi(std::string(term));
        degree = 0;
    } else { 
        if (xPos > 0)
            switch (term[xPos-1]) {
            case '-':
                cfcnt = -1;
                break;
            case '+':
                cfcnt = +1;
                break;
            default:
                cfcnt = std::stoi(std::string(term.substr(0, xPos)));
            }
        size_t powPos{ term.find('^', xPos) };
        if (powPos == std::string_view::npos)
            degree = 1;
        else
            degree = std::stoi(std::string(term.substr(powPos + 1)));
    }
    return { cfcnt, degree };
}

void insertTerm(std::list<Term>& poly, const Term& term) {
    for (auto it{ poly.begin() }; it != poly.end(); ++it) {
        if (it->second == term.second) {
            it->first += term.first;
            if (it->first == 0)
                poly.erase(it);
            return;
        } else if (it->second < term.second) {
            poly.insert(it, term);
            return;
        }
    }
    poly.push_back(term); // if term has the lowest degree put to the end
}

void parseStrToPolynomial(std::string_view str, std::list<Term>& poly) {
    size_t start {0},
           len   { str.size() };
    while (start < len) {
        size_t next{ str.find_first_of("+-", start + 1) };
        if (next == std::string_view::npos)
            next = len;
        insertTerm(poly, parseStrToTerm(str.substr(start, next - start)));
        start = next;
    }
}

std::ostream& operator<<(std::ostream& out, const Term& term) {
#ifndef DEBUG_PRINT
    if (term.first == 0)
        return out << 0;
    out << (term.first < 0? '-' : '+');
    if (std::abs(term.first) != 1 || term.second == 0)
        out << std::abs(term.first);
    if (term.second > 0) {
        out << 'x';
        if (term.second != 1)
            out << '^' << term.second;
    }
#else
    out << "{ " << term.first << ", " << term.second << " }";
#endif
    return out;
}

int main() {
    std::list<Term> polynomial;
    std::string input;
    while (true) {
        std::cout << "Введите полином (или '0' для выхода): ";
        std::getline(std::cin >> std::ws, input);
        if (input == "0")
            break;
        parseStrToPolynomial(input, polynomial);
    }
    std::cout << "Полином:\n";
    for (const auto& term : polynomial)
        std::cout << term << " ";
    std::cout << '\n';
    return EXIT_SUCCESS;
}
