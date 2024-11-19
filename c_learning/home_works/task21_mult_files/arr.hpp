#pragma once
#include <cstdlib>
#include <iostream>
#include <initializer_list>

#include "arr_base.hpp"
#include "str.hpp"

template <typename T>
class CArrWrapper : public CArrBase<T> {
protected:
    using CArrBase<T>::size_;
    using CArrBase<T>::data;
public:
    using CArrBase<T>::CArrBase;

    CArrWrapper(std::initializer_list<T> iniList);
    CArrWrapper(const CArrWrapper& other);
    CArrWrapper(CArrWrapper&& other) noexcept;
    CArrWrapper& operator=(const CArrWrapper& other);
    CArrWrapper& operator+=(const T& el);
};

template <typename T>
constexpr T max(T a, T b) {
    return a > b ? a : b;
}

template <typename T>
constexpr T min(T a, T b) {
    return a < b ? a : b;
}

template <typename T>
std::ostream& operator<<(std::ostream& out, const CArrWrapper<T>& arr);

CArrWrapper<CStrWrapper> zip(const CArrWrapper<CStrWrapper>& arr1, const CArrWrapper<CStrWrapper>& arr2);

CArrWrapper<CStrWrapper> mergeUnique(const CArrWrapper<CStrWrapper>& arr1, const CArrWrapper<CStrWrapper>& arr2);

