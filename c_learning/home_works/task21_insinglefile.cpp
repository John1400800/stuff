#include <cstdlib>
#include <cstdint>
#include <cassert>
#include <initializer_list>
#include <iostream>

template <typename T>
class CArrBase {
protected:
    size_t size_{ 0 };
    T* data { nullptr };

    CArrBase(size_t size, T* data)
        : size_{ size }, data{ data }
    { }
public:
    CArrBase() = default;

    CArrBase(size_t size)
        : CArrBase( size, size > 0? new T[size] : nullptr)
    { }

    ~CArrBase() {
        delete[] data;
    }

    CArrBase& operator=(CArrBase&& other) noexcept {
        if (this == &other)
            return *this;
        delete[] data;
        size_ = other.size_;
        data = other.data;
        other.size_ = 0;
        other.data = nullptr;
        return *this;
    }

    const T& operator[](size_t idx) const {
        assert(idx < size_);
        return data[idx];
    }

    T& operator[](size_t idx) {
        assert(idx < size_);
        return data[idx];
    }

    size_t size() const { // maybe unused
        return size_;
    }

    const T *begin() const {
        return data;
    }

    const T *end() const {
        return data+size_;
    }
};

template <typename T>
class CArrWrapper : public CArrBase<T> {
protected:
    // почему в унаследованном от шаблонного класса нужно писать this->member а не member
    using CArrBase<T>::size_;
    using CArrBase<T>::data;
public:
    // почему в унаследованном от шаблонного класса нужно писать this->member а не member
    // что означает using в этом контексте ?
    using CArrBase<T>::CArrBase;

    CArrWrapper(std::initializer_list<T> iniList)
        : CArrBase<T>( iniList.size() )
    {
        size_t i{0};
        for (const auto& item : iniList)
            (*this)[i++] = item;
    }

    CArrWrapper(const CArrWrapper& other)
        : CArrBase<T>( other.size_ )
    {
        for (size_t i{0}; i<size_; ++i)
            (*this)[i] = other[i];
    }

    CArrWrapper(CArrWrapper&& other) noexcept
        : CArrBase<T>( other.size_,  other.data )
    {
        other.size_ = 0;
        other.data = nullptr;
    }

    CArrWrapper& operator=(const CArrWrapper& other) {
        //// explain why it won't work
        // CArrWrapper newArr{other};
        // return *this = std::move(newArr);
        delete[] data;
        size_ = other.size_;
        data = new T[size_];
        size_t i{0};
        for (const T& el : other)
            (*this)[i++] = el;
        return *this;
    }

    CArrWrapper& push_back(const T& el) {
        CArrWrapper res(size_ + 1);
        size_t i{0};
        for (; i<size_; ++i)
            res[i] = (*this)[i];
        res[size_] = el;
        return *this = std::move(res);
    }
};

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

    CStrWrapper(size_t iniSize)
        : CArrBase(iniSize+1)
    {
        data[--size_] = '\0';
    }

    CStrWrapper(const CStrWrapper& other) // maybe unused
        : CStrWrapper(other.size_)
    {
        for (size_t i{0}; i<size_; ++i)
            (*this)[i] = other[i];
    }

    CStrWrapper& operator=(const CStrWrapper& other) { // maybe unused
        //// explain why it won't work
        // CStrWrapper newStr{ other };
        // return *this = std::move(newStr);
        delete[] data;
        size_ = other.size_;
        data = new char[size_+1];
        data[size_] = '\0';
        size_t i{0};
        for (char ch : other)
            (*this)[i++] = ch;
        return *this;
    }

    CStrWrapper(const char* str)
        : CStrWrapper(CStrLen(str))
    {
        if (str == nullptr)
            return ;
        for (size_t i{0}; i<size_; ++i)
            (*this)[i] = str[i];
    }

    CStrWrapper& operator+=(const CStrWrapper& other) {
        CStrWrapper newStr{size_ + other.size_};
        size_t i{0};
        for (; i<size_; ++i) // copy *this
            newStr[i] = (*this)[i];
        for (size_t j{0}; j<other.size_; ++j, ++i) // copy other
            newStr[i] = other[j];
        return *this = std::move(newStr);
    }
};

template <typename T>
std::ostream& operator<<(std::ostream& out, const CArrWrapper<T>& arr) {
    bool isFirst{ true };
    for (const T& item : arr) {
        out << (!isFirst ? ", " : "") << item;
        isFirst = false;
    }
    return out;
}

std::ostream& operator<<(std::ostream& out, const CStrWrapper& str) {
    for (char ch : str)
        std::cout << ch;
    return out;
}

CStrWrapper operator+(const CStrWrapper& str1, const CStrWrapper& str2) {
    return CStrWrapper{str1} += str2;
}

template <typename T>
constexpr T max(T a, T b) {
    return a > b ? a : b;
}

template <typename T>
constexpr T min(T a, T b) {
    return a < b ? a : b;
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

bool operator==(const CStrWrapper& str1, const CStrWrapper& str2) {
    if (str1.size() != str2.size())
        return false;
    for (size_t i{0}; i<str1.size(); ++i)
        if (str1[i] != str2[i])
            return false;
    return true;
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
            res.push_back(elCopy);
    }
    return res;
}

int main(int32_t, const char**) {
    std::cout << mergeUnique(zip(CArrWrapper<CStrWrapper>{ "Hello", "World", "All" }, { "Foo", "Bar" }), {"All", "WorldBar", "Foo", "All"}) << '\n';
    return EXIT_SUCCESS;
}
