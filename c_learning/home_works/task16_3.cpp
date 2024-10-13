#include <cstdlib>
#include <cstdint>
#include <cmath>
#include <list>
#include <string>
#include <string_view>
#include <utility>
#include <iostream>

// #define DEBUG

#define cfcnt   first
#define degree second

using Term = std::pair<int32_t, int32_t>;

Term parseStrToTerm(std::string term) {
    Term res( 0, 0 );
    if (term.empty())
        return res;
    size_t xPos{ term.find('x') };
    if (xPos == std::string::npos) {
        res.cfcnt = std::stoi(term);
        return res;
    }
    std::string cfcntStr{ term.substr(0, xPos) };
    if (cfcntStr.empty() || cfcntStr == "+")
        res.cfcnt = +1;
    else if (cfcntStr == "-")
        res.cfcnt = -1;
    else
        res.cfcnt = std::stoi(cfcntStr);
    size_t powPos{ term.find('^') };
    if (powPos == std::string::npos)
        res.degree = 1;
    else
        res.degree = std::stoi(term.substr(powPos+1));
    return res;
}

void parseStrToPolynomial(const std::string& str, std::list<Term>& res) {
    size_t start{ 0 };
    size_t pos  { start };
    while (pos != std::string::npos) {
        pos = str.find_first_of("+-", start + 1);
        Term term = parseStrToTerm(str.substr(start, pos - start));
        auto it{ res.begin() }; // separate this VVV
        bool insrtd{ false };
        while (!insrtd && it != res.end()) {
            if (term.degree == it->degree) {
                it->cfcnt += term.cfcnt;
                if (it->cfcnt == 0)
                    it = res.erase(it);
                insrtd = true;
            } else if (it->degree < term.degree) {
                res.insert(it, term);
                insrtd = true;
            }
            ++it;
        }
        if (!insrtd)
            res.push_back(term);
        start = pos;
    }
}

std::ostream& operator<<(std::ostream& out, Term term) {
#ifdef DEBUG
    return out << "{ " << term.cfcnt << ", " << term.degree << " }";
#else
    if (term.cfcnt < 0) {
        out << '-';
        term.cfcnt = -term.cfcnt;
    } else
        out << '+';
    if (term.cfcnt != 0) {
        if (term.degree == 0)
            out << term.cfcnt;
        else {
            if (term.cfcnt != 1)
                out << term.cfcnt;
            out << 'x';
            if (term.degree != 1)
                out << '^' << term.degree;
        }
    } else
        out << 0;
    return out;
#endif
}

int main() {
    std::list<Term> polynomial{};
    parseStrToPolynomial("2x^3-1+3x^4-0+x^4", polynomial);
    for (const Term& term : polynomial)
        std::cout << term << '\n';
    std::cout << '\n';
    return EXIT_SUCCESS;
}
