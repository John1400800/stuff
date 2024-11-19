#include "str.hpp"

CStrWrapper::CStrWrapper(size_t iniSize)
    : CArrBase(iniSize+1)
{
    data[--size_] = '\0';
}

CStrWrapper::CStrWrapper(const CStrWrapper& other)
    : CStrWrapper(other.size_)
{
    for (size_t i{0}; i<size_; ++i)
        (*this)[i] = other[i];
}

CStrWrapper& CStrWrapper::operator=(const CStrWrapper& other) {
    delete[] data;
    size_ = other.size_;
    data = new char[size_+1];
    data[size_] = '\0';
    size_t i{0};
    for (char ch : other)
        (*this)[i++] = ch;
    return *this;
}

CStrWrapper::CStrWrapper(const char* str)
    : CStrWrapper(CStrLen(str))
{
    if (str == nullptr)
        return ;
    for (size_t i{0}; i<size_; ++i)
        (*this)[i] = str[i];
}

CStrWrapper& CStrWrapper::operator+=(const CStrWrapper& other) {
    CStrWrapper newStr{size_ + other.size_};
    size_t i{0};
    for (; i<size_; ++i)
        newStr[i] = (*this)[i];
    for (size_t j{0}; j<other.size_; ++j, ++i)
        newStr[i] = other[j];
    return *this = std::move(newStr);
}


std::ostream& operator<<(std::ostream& out, const CStrWrapper& str) {
    for (char ch : str)
        std::cout << ch;
    return out;
}

CStrWrapper operator+(const CStrWrapper& str1, const CStrWrapper& str2) {
    return CStrWrapper{str1} += str2;
}

bool operator==(const CStrWrapper& str1, const CStrWrapper& str2) {
    if (str1.size() != str2.size())
        return false;
    for (size_t i{0}; i<str1.size(); ++i)
        if (str1[i] != str2[i])
            return false;
    return true;
}
