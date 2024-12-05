#include <cstdlib>      // for EXIT_SUCCESS, abs
#include <cstdint>      // for int32_t
#include <limits>
#include <list>         // std::list
#include <string>       // std::string
#include <string_view>  // std::string_view
#include <utility>      // for std::pair
#include <iostream>     // std::cout, std::cin

namespace {
    constexpr auto DEBUG_PRINT{ false };
}

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
        if (powPos == std::string_view::npos || cfcnt == 0)
            degree = 1;
        else
            degree = std::stoi(std::string(term.substr(powPos + 1)));
    }
    return { cfcnt, degree };
}

void insertTerm(std::list<Term>& poly, const Term& term) {
    for (auto it{ poly.begin() }; it != poly.end(); ++it) {
        if (term.second == it->second) {
            it->first += term.first;
            if (it->first == 0)
                poly.erase(it);
            return;
        } else if (term.second > it->second) {
            poly.insert(it, term);
            return;
        }
    }
    poly.push_back(term); // if term has the lowest degree put to the end
}

void removeTermByDegree(std::list<Term>& poly, int32_t degree) {
    for (auto it{ poly.begin() }; it != poly.end(); ++it)
        if (it->second == degree) {
            poly.erase(it);
            return;
        }
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
if constexpr (! DEBUG_PRINT) {
    out << (term.first < 0? '-' : '+');
    if (term.first == 0)
        return out << 0;
    if (std::abs(term.first) != 1 || term.second == 0)
        out << std::abs(term.first);
    if (term.second > 0) {
        out << 'x';
        if (term.second != 1)
            out << '^' << term.second;
    }
}
else {
    out << "{ " << term.first << ", " << term.second << " }";
}
    return out;
}

int main() {
    std::list<Term> polynomial;
    std::string input;
    uint32_t choice;
    do {
        std::cout << "\nМеню:\n"
            "1. Ввести новый член полинома\n"
            "2. Удалить член по указанной степени\n"
            "3. Вывести полином\n"
            "0. Выйти\n"
            "Выбирите: ";
        if (!(std::cin >> choice)) {
            std::cerr << "Ошибка: Некорректный ввод. Ожидается число.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }
        switch(choice) {
            case 1:
                std::cout << "Введите многочлен или одночлен: ";
                std::getline(std::cin >> std::ws, input);
                parseStrToPolynomial(input, polynomial);
                break;
            case 2:
                std::cout << "Введите стеаень члена который хотите удалить: ";
                int32_t degree;
                std::cin >> degree;
                removeTermByDegree(polynomial, degree);
                break;
            case 3:
                if (polynomial.empty())
                    std::cout << "Полином пуст\n";
                else {
                    std::cout << "Полином:\n";
                    for (const auto& term : polynomial)
                        std::cout << term << " ";
                    std::cout << '\n';
                }
                break;
            case 0:
                std::cout << "Выход\n";
                break;
            default:
                std::cout << "Неизвестный ввод, Выберете из доступных: 1, 2, 3, 0\n";
                break;
        }
    } while(choice);
    return EXIT_SUCCESS;
}
