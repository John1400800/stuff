#include <cstdlib>
#include <cstdint>
#include <iostream>

#include "arr.hpp"
#include "str.hpp"


int main(int32_t, const char**) {
    std::cout <<
        mergeUnique(zip( CArrWrapper<CStrWrapper>{ "Hello", "World", "All" }, { "Foo", "Bar" } ),
                    {"All", "WorldBar", "Foo", "All"}) << '\n';
    return EXIT_SUCCESS;
}
