#include <cstdlib>
#include <cstdint>
#include <limits>
#include <list>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdexcept>

enum class PublicationType { Newspaper, Magazine };

using Publication = std::tuple<PublicationType, std::string, double>;

std::istream& operator>>(std::istream& is, PublicationType& type) {
    std::string str; 
    is >> str;
    if (str == "Газета") 
        type = PublicationType::Newspaper;
    else if (str == "Журнал") 
        type = PublicationType::Magazine;
    else 
        throw std::invalid_argument("Неверный тип публикации: " + str);
    return is;
}

std::ostream& operator<<(std::ostream& out, PublicationType type) {
    return out << (type == PublicationType::Newspaper ? "Газета" : "Журнал");
}

std::ostream& operator<<(std::ostream& out, const std::list<Publication>& pubs) {
    for (const auto& pub : pubs)
        out << std::get<0>(pub) << ": " << std::get<1>(pub) << ", Цена: " << std::get<2>(pub) << " монеты.\n";
    if (pubs.empty()) 
        out << "Список пуст.\n";
    return out;
}

void addPublication(std::list<Publication>& pubs, const Publication& pub) {
    if (std::get<0>(pub) == PublicationType::Magazine)
        pubs.push_front(pub);
    else
        pubs.push_back(pub);
}

void loadPublications(std::list<Publication>& pubs, const std::string& filename) {
    try {
        std::ifstream file{filename};
        if (!file.is_open()) 
            throw std::runtime_error("Ошибка открытия файла: " + filename);

        std::string line, pubType, name; 
        double price;
        while (std::getline(file >> std::ws, line)) {
            std::istringstream iss{line}; 
            std::getline(iss >> std::ws, pubType, ',');
            std::getline(iss >> std::ws, name, ','); 
            iss >> price;
            addPublication(pubs, {pubType == "Журнал" ? PublicationType::Magazine : PublicationType::Newspaper,
                                  name, price});
        }
    } catch (const std::exception& e) {
        std::cerr << "Произошла ошибка при загрузке: " << e.what() << '\n';
    }
}

void savePublications(const std::list<Publication>& pubs, const std::string& filename) {
    try {
        std::ofstream file{filename};
        if (!file) 
            throw std::runtime_error("Ошибка записи в файл: " + filename);
        for (const auto& pub : pubs)
            file << (std::get<0>(pub) == PublicationType::Newspaper ? "Газета" : "Журнал")
                 << ", " << std::get<1>(pub) << ", " << std::get<2>(pub) << '\n';
    } catch (const std::exception& e) {
        std::cerr << "Произошла ошибка при сохранении: " << e.what() << '\n';
    }
}

int main() {
    std::setlocale(LC_ALL, "ru_RU.UTF-8");
    std::list<Publication> pubs; 
    uint32_t choice; 
    PublicationType type; 
    std::string name; 
    double price;

    do {
        try {
            std::cout << "Меню:\n1. Добавить\n2. Показать\n3. Загрузить из файла\n4. Сохранить в файл\n5. Выход\nВыберите: ";
            if (!(std::cin >> choice)) {
                throw std::invalid_argument("Некорректный ввод! Вы должны ввести число.");
            }

            switch (choice) {
                case 1:
                    try {
                        std::cout << "Введите тип (Газета или Журнал): "; 
                        std::cin >> type;
                        std::cout << "Введите название: "; 
                        std::getline(std::cin >> std::ws, name);
                        std::cout << "Введите цену: "; 
                        if (!(std::cin >> price)) {
                            throw std::invalid_argument("Некорректный ввод цены! Должно быть число.");
                        }
                        addPublication(pubs, {type, name, price});
                    } catch (const std::exception& e) {
                        std::cerr << "Ошибка добавления публикации: " << e.what() << '\n';
                        std::cin.clear();
                        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    }
                    break;

                case 2:
                    std::cout << pubs;
                    break;

                case 3:
                    try {
                        std::cout << "Введите имя файла: "; 
                        std::getline(std::cin >> std::ws, name);
                        loadPublications(pubs, name);
                    } catch (const std::exception& e) {
                        std::cerr << "Ошибка при загрузке: " << e.what() << '\n';
                    }
                    break;

                case 4:
                    try {
                        std::cout << "Введите имя файла: "; 
                        std::getline(std::cin >> std::ws, name);
                        savePublications(pubs, name);
                    } catch (const std::exception& e) {
                        std::cerr << "Ошибка при сохранении: " << e.what() << '\n';
                    }
                    break;

                case 5:
                    std::cout << "Выход из программы.\n";
                    break;

                default:
                    std::cerr << "Неверный выбор.\n";
                    break;
            }

        } catch (const std::exception& e) {
            std::cerr << "Ошибка: " << e.what() << '\n';
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }

    } while (choice != 5);

    return EXIT_SUCCESS;
}
