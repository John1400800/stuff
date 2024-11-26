#include <sstream>
#include <fstream>
#include "func.hpp"

std::istream& operator>>(std::istream& is, PublicationType& type) {
    std::string str; 
    is >> str;
    if (str == "Газета") 
        type = PublicationType::Newspaper;
    else if (str == "Журнал") 
        type = PublicationType::Magazine;
    else {
        std::cerr << "Ошибка: Неверный тип публикации: " << str << '\n';
        return is;
    }
    return is;
}

std::ostream& operator<<(std::ostream& out, PublicationType type) {
    return out << (type == PublicationType::Newspaper ? "Газета" : "Журнал");
}

std::ostream& operator<<(std::ostream& out, const std::list<Publication>& pubs) {
    if (pubs.empty()) {
        out << "Список пуст.\n";
        return out;
    }
    for (const auto& pub : pubs) {
        out << std::get<0>(pub) << ": " << std::get<1>(pub) 
            << ", Цена: " << std::get<2>(pub) << " монеты.\n";
    }
    return out;
}

void addPublication(std::list<Publication>& pubs, const Publication& pub) {
    if (std::get<0>(pub) == PublicationType::Magazine)
        pubs.push_front(pub);
    else
        pubs.push_back(pub);
}

bool loadPublications(std::list<Publication>& pubs, const std::string& filename) {
    std::ifstream file{filename};
    if (!file.is_open()) {
        std::cerr << "Ошибка: Не удалось открыть файл " << filename << '\n';
        return false;
    }

    std::string line, pubType, name;
    double price;
    while (std::getline(file >> std::ws, line)) {
        std::istringstream iss{line};
        std::getline(iss >> std::ws, pubType, ',');
        std::getline(iss >> std::ws, name, ',');
        if (!(iss >> price)) {
            std::cerr << "Ошибка: Некорректный формат строки: " << line << '\n';
            return false;
        }
        PublicationType type = pubType == "Журнал" ? PublicationType::Magazine : PublicationType::Newspaper;
        addPublication(pubs, {type, name, price});
    }
    return true;
}

bool savePublications(const std::list<Publication>& pubs, const std::string& filename) {
    std::ofstream file{filename};
    if (!file.is_open()) {
        std::cerr << "Ошибка: Не удалось открыть файл для записи: " << filename << '\n';
        return false;
    }

    for (const auto& pub : pubs) {
        file << (std::get<0>(pub) == PublicationType::Newspaper ? "Газета" : "Журнал")
             << ", " << std::get<1>(pub) << ", " << std::get<2>(pub) << '\n';
    }
    return true;
}

