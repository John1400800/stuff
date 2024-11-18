#include <cstdlib>
#include <cstdint>
#include <cassert>
#include <initializer_list>
// #include <utility> // for std::move
#include <iostream>

template <typename T>
class CArrWrapper {
protected:
    size_t size_{ 0 };
    T *data{ nullptr };
public:
    CArrWrapper()
        : CArrWrapper(0)
    { }

    CArrWrapper(size_t iniSize)
        : size_{ iniSize }, data{ size_>0? new T[size_] : nullptr }
    { }

    CArrWrapper(std::initializer_list<T> iniList)
        : CArrWrapper( iniList.size() )
    {
        size_t i{0};
        for (const auto& item : iniList)
            data[i++] = item;
    }

    CArrWrapper(const CArrWrapper& other)
        : CArrWrapper( other.size_ )
    {
        for (size_t i{0}; i<size_; ++i)
            data[i] = other.data[i];
    }

    CArrWrapper(CArrWrapper&& other) noexcept
        : size_{ other.size_ }, data{ other.data }
    {
        std::cout << "\nMove\n";
        other.size_ = 0;
        other.data = nullptr;
    }

    CArrWrapper& operator=(const CArrWrapper& other) {
        if (this == &other)
            return *this;
        delete[] data;
        size_ = other.size_;
        data = size_>0? new T[size_] : nullptr;
        for (size_t i{0}; i < size_; ++i)
            data[i] = other.data[i];
        return *this;
    }

    CArrWrapper& operator=(CArrWrapper&& other) noexcept {
        if (this == &other)
            return *this;
        delete[] data;
        size_ = other.size_;
        data = other.data;
        other.size_ = 0;
        other.data = nullptr;
        return *this;
    }

    ~CArrWrapper() {
        // std::cout << "Clear\n";
        delete[] data;
    }

    T& operator[](size_t idx) {
        assert(idx < size_);
        return data[idx];
    }

    const T& operator[](size_t idx) const {
        assert(idx < size_);
        return data[idx];
    }

    size_t size() const {
        return size_;
    }

    const T* begin() const {
        return data;
    }

    const T* end() const {
        return data + size_;
    }

    // split into inherited class in future and replace with operator+=
    CArrWrapper& push_back(const T& el) {
        CArrWrapper res(size_ + 1);
        size_t i{0};
        for (; i<size_; ++i)
            res[i] = data[i];
        res[size_] = el;
        return *this = std::move(res);
    }
};

class CStrWrapper : public CArrWrapper<char> {
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
    CStrWrapper(size_t iniSize)
        : CArrWrapper(iniSize+1)
    {
        data[--size_] = '\0';
    }

    CStrWrapper()
        : CStrWrapper(0ul)
    { }

    CStrWrapper(const char* str)
        : CStrWrapper(CStrLen(str))
    {
        if (str == nullptr)
            return ;
        for (size_t i{0}; i<size_; ++i)
            data[i] = str[i];
    }

    CStrWrapper& operator+=(const CStrWrapper& other) {
        CStrWrapper newStr(size_ + other.size_);
        size_t i{0};
        for (; i<size_; ++i)
            newStr.data[i] = data[i];
        for (size_t j{0}; j<other.size_; ++j, ++i)
            newStr.data[i] = other.data[j];
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
    for (const auto& ch : str)
        out << ch;
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
