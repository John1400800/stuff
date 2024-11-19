#include "arr.hpp"
#include "str.hpp"

template <typename T>
CArrWrapper<T>::CArrWrapper(std::initializer_list<T> iniList)
    : CArrBase<T>( iniList.size() )
{
    size_t i{0};
    for (const auto& item : iniList)
        (*this)[i++] = item;
}

template <typename T>
CArrWrapper<T>::CArrWrapper(const CArrWrapper& other)
    : CArrBase<T>( other.size_ )
{
    for (size_t i{0}; i<size_; ++i)
        (*this)[i] = other[i];
}

template <typename T>
CArrWrapper<T>::CArrWrapper(CArrWrapper&& other) noexcept
    : CArrBase<T>( other.size_,  other.data )
{
    other.size_ = 0;
    other.data = nullptr;
}

template <typename T>
CArrWrapper<T>& CArrWrapper<T>::operator=(const CArrWrapper& other) {
    delete[] data;
    size_ = other.size_;
    data = new T[size_];
    size_t i{0};
    for (const T& el : other)
        (*this)[i++] = el;
    return *this;
}

template <typename T>
CArrWrapper<T>& CArrWrapper<T>::operator+=(const T& el) {
    CArrWrapper res(size_ + 1);
    size_t i{0};
    for (; i<size_; ++i)
        res[i] = (*this)[i];
    res[size_] = el;
    return *this = std::move(res);
}

template <typename T>
std::ostream& operator<<(std::ostream& out, const CArrWrapper<T>& arr) {
    bool isFirst{ true };
    for (const T& item : arr) {
        out << (!isFirst ? ", " : "") << item;
        isFirst = false;
    }
    return out;
}

CArrWrapper<CStrWrapper> zip(const CArrWrapper<CStrWrapper>& arr1, const CArrWrapper<CStrWrapper>& arr2) {
    CArrWrapper<CStrWrapper> res;
    const CArrWrapper<CStrWrapper> *add;
    if (arr1.size() == arr2.size()) {
        res =  arr1;
        add = &arr2;
    } else {
        res  = max(arr1.size(), arr2.size()) == arr1.size() ? arr1 : arr2;
        add = ((min(arr1.size(), arr2.size()) == arr1.size()) ? &arr1 : &arr2);
    }
    for (size_t i{0}; i < add->size(); ++i)
        res[i] += (*add)[i];
    return res;
}

CArrWrapper<CStrWrapper> mergeUnique(const CArrWrapper<CStrWrapper>& arr1, const CArrWrapper<CStrWrapper>& arr2) {
    CArrWrapper<CStrWrapper> res{arr1};
    for (const auto& elCopy : arr2) {
        bool unique{ true };
        for (const auto& elRes : res)
            if (elCopy == elRes) {
                unique = false;
                break;
            }
        if (unique)
            res += elCopy;
    }
    return res;
}

template class CArrWrapper<CStrWrapper>;
template std::ostream& operator<<(std::ostream& out, const CArrWrapper<CStrWrapper>& arr);
