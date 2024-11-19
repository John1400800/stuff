#pragma once
#include <cstdlib>
#include <cassert>

template <typename T>
class CArrBase {
protected:
    size_t size_{ 0 };
    T* data { nullptr };

    CArrBase(size_t size, T* data);
public:
    CArrBase() = default;
    CArrBase(size_t size);
    ~CArrBase();
    CArrBase& operator=(CArrBase&& other) noexcept;
    const T& operator[](size_t idx) const;
    T& operator[](size_t idx);
    size_t size() const;
    const T *begin() const;
    const T *end() const;
};
