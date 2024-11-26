#include <cstdlib>
#include <cstdint>
#include <limits>
#include <iostream>

#include "func.hpp"

int main() {
    std::setlocale(LC_ALL, "ru_RU.UTF-8");
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
