#include <cstdlib>
#include <cstdint>
#include <cmath>
#include <list>
#include <string>
#include <string_view>
#include <utility>
#include <iostream>

using Term = std::pair<int32_t, int32_t>;

constexpr Term parseStrToTerm(std::string_view term) {
    int32_t cfcnt = 1, degree = 1;
    auto xPos = term.find('x');
    if (xPos != std::string_view::npos) {
        if (xPos > 0) {
            if (term[xPos - 1] == '+' || term[xPos - 1] == '-') {
                cfcnt = term[xPos - 1] == '+' ? 1 : -1;
            } else {
                cfcnt = std::stoi(std::string(term.substr(0, xPos)));
            }
        }
        auto powPos = term.find('^', xPos);
        if (powPos == std::string_view::npos) {
            degree = 1;
        } else {
            degree = std::stoi(std::string(term.substr(powPos + 1)));
        }
    } else {
        cfcnt = std::stoi(std::string(term));
        degree = 0;
    }
    return { cfcnt, degree };
}

void insertTerm(std::list<Term>& poly, const Term& term) {
    for (auto it = poly.begin(); it != poly.end(); ++it) {
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
    poly.push_back(term);
}

void parseStrToPolynomial(std::string_view str, std::list<Term>& poly) {
    size_t start = 0, len = str.size();
    while (start < len) {
        size_t next = str.find_first_of("+-", start + 1);
        if (next == std::string_view::npos) next = len;
        insertTerm(poly, parseStrToTerm(str.substr(start, next - start)));
        start = next;
    }
}

std::ostream& operator<<(std::ostream& out, const Term& term) {
    if (term.first == 0)
        return out << 0;
    if (term.first > 0) out << "+";
    else out << "-";
    if (std::abs(term.first) != 1 || term.second == 0)
        out << std::abs(term.first);
    if (term.second > 0) {
        out << 'x';
        if (term.second != 1) out << '^' << term.second;
    }
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
