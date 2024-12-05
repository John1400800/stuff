#include <cstdlib>
#include <cstdint>
#include <limits>
#include <list>
#include <fstream>
#include <sstream>
#include <iostream>

enum class PublicationType { Newspaper, Magazine };

enum : size_t { Type, Name, Cost };
using Publication = std::tuple<PublicationType, std::string, double>;

std::istream& operator>>(std::istream& is, PublicationType& type) {
    std::string str;
    is >> str;
    if (str == "Газета")
        type = PublicationType::Newspaper;
    else if (str == "Журнал")
        type = PublicationType::Magazine;
    else
        is.setstate(std::ios::failbit);
    return is;
}

std::ostream& operator<<(std::ostream& out, PublicationType type) {
    return out << (type == PublicationType::Newspaper ? "Газета" : "Журнал");
}

std::ostream& operator<<(std::ostream& out, const std::list<Publication>& pubs) {
    if (pubs.empty())
        return out << "Список пуст.\n";
    for (const auto& pub : pubs)
        out << std::get<Type>(pub) << ": " << std::get<Name>(pub)
            << ", Цена: " << std::get<Cost>(pub) << " монеты.\n";
    return out;
}

void addPublication(std::list<Publication>& pubs, const Publication& pub) {
    if (std::get<Type>(pub) == PublicationType::Magazine)
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
        file << (std::get<Type>(pub) == PublicationType::Newspaper ? "Газета" : "Журнал")
             << ", " << std::get<Name>(pub) << ", " << std::get<Cost>(pub) << '\n';
    }
    return true;
}


int main() {
    // std::setlocale(LC_ALL, "ru_RU.UTF-8");
    std::list<Publication> pubs;
    uint32_t choice = 0;

    while (choice != 5) {
        std::cout << "\nМеню:\n"
                  << "1. Добавить публикацию\n"
                  << "2. Показать публикации\n"
                  << "3. Загрузить из файла\n"
                  << "4. Сохранить в файл\n"
                  << "5. Выход\n"
                  << "Ваш выбор: ";
        if (!(std::cin >> choice)) {
            std::cerr << "Ошибка: Некорректный ввод. Ожидается число.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            continue;
        }

        switch (choice) {
            case 1: {
                PublicationType type;
                std::string name;
                double price;

                std::cout << "Введите тип (Газета или Журнал): ";
                if (!(std::cin >> type)) {
                    std::cerr << "Ошибка: Неверный тип публикации.\n";
                    std::cin.clear();
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    break;
                }

                std::cout << "Введите название: ";
                std::getline(std::cin >> std::ws, name);

                std::cout << "Введите цену: ";
                if (!(std::cin >> price)) {
                    std::cerr << "Ошибка: Неверный ввод цены.\n";
                    std::cin.clear();
                    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                    break;
                }

                addPublication(pubs, {type, name, price});
                std::cout << "Публикация добавлена.\n";
                break;
            }
            case 2:
                std::cout << pubs;
                break;

            case 3: {
                std::string filename;
                std::cout << "Введите имя файла: ";
                std::getline(std::cin >> std::ws, filename);

                if (loadPublications(pubs, filename))
                    std::cout << "Публикации успешно загружены.\n";
                break;
            }

            case 4: {
                std::string filename;
                std::cout << "Введите имя файла: ";
                std::getline(std::cin >> std::ws, filename);

                if (savePublications(pubs, filename))
                    std::cout << "Публикации успешно сохранены.\n";
                break;
            }

            case 5:
                std::cout << "Выход из программы.\n";
                break;

            default:
                std::cerr << "Ошибка: Неверный выбор.\n";
                break;
        }
    }

    return EXIT_SUCCESS;
}
