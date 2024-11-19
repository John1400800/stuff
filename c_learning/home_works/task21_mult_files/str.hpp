#pragma once
#include <cstdlib>
#include <iostream>

#include "arr_base.hpp"

class CStrWrapper : public CArrBase<char> {
protected:
    static constexpr size_t CStrLen(const char* str) {
        if (str==nullptr)
            return 0;
        size_t i{0};
        for (; str[i]!='\0'; ++i)
            ;
        return i;
    }
public:
    using CArrBase<char>::CArrBase;
    CStrWrapper(size_t iniSize);
    CStrWrapper(const CStrWrapper& other);
    CStrWrapper& operator=(const CStrWrapper& other);
    CStrWrapper(const char* str);
    CStrWrapper& operator+=(const CStrWrapper& other);
};

std::ostream& operator<<(std::ostream& out, const CStrWrapper& str);
CStrWrapper operator+(const CStrWrapper& str1, const CStrWrapper& str2);
bool operator==(const CStrWrapper& str1, const CStrWrapper& str2);
