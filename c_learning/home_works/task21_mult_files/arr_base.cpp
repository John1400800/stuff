#include "arr_base.hpp"
#include "str.hpp"

template <typename T>
CArrBase<T>::CArrBase(size_t size, T* data)
    : size_{ size }, data{ data }
{ }

template <typename T>
CArrBase<T>::CArrBase(size_t size)
    : CArrBase( size, size > 0? new T[size] : nullptr)
{ }

template <typename T>
CArrBase<T>::~CArrBase() {
    delete[] data;
}

template <typename T>
CArrBase<T>& CArrBase<T>::operator=(CArrBase&& other) noexcept {
    if (this == &other)
        return *this;
    delete[] data;
    size_ = other.size_;
    data = other.data;
    other.size_ = 0;
    other.data = nullptr;
    return *this;
}

template <typename T>
const T& CArrBase<T>::operator[](size_t idx) const {
    assert(idx < size_);
    return data[idx];
}

template <typename T>
T& CArrBase<T>::operator[](size_t idx) {
    assert(idx < size_);
    return data[idx];
}

template <typename T>
size_t CArrBase<T>::size() const {
    return size_;
}

template <typename T>
const T *CArrBase<T>::begin() const {
    return data;
}

template <typename T>
const T *CArrBase<T>::end() const {
    return data+size_;
}

template class CArrBase<char>;
template class CArrBase<CStrWrapper>;
