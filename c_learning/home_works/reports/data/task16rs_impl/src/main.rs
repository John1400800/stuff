use std::collections::LinkedList;
use std::fs::{File, OpenOptions};
use std::io::{self, BufRead, BufReader, Write};

#[derive(Debug, PartialEq, Eq)]
enum PublicationType {
    Newspaper,
    Magazine,
}

impl std::str::FromStr for PublicationType {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "Газета" => Ok(PublicationType::Newspaper),
            "Журнал" => Ok(PublicationType::Magazine),
            _ => Err(format!("Неизвестный тип публикации: {}", s)),
        }
    }
}

impl std::fmt::Display for PublicationType {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let name = match self {
            PublicationType::Newspaper => "Газета",
            PublicationType::Magazine => "Журнал",
        };
        write!(f, "{}", name)
    }
}

#[derive(Debug)]
struct Publication {
    pub_type: PublicationType,
    name: String,
    cost: f64,
}

impl std::fmt::Display for Publication {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{}: {}, Цена: {} монеты",
            self.pub_type, self.name, self.cost
        )
    }
}

fn add_publication(pubs: &mut LinkedList<Publication>, r#pub: Publication) {
    match r#pub.pub_type {
        PublicationType::Magazine => pubs.push_front(r#pub),
        PublicationType::Newspaper => pubs.push_back(r#pub),
    }
}

fn load_publications(pubs: &mut LinkedList<Publication>, filename: &str) -> io::Result<()> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        let parts: Vec<&str> = line.split(',').map(str::trim).collect();
        if parts.len() != 3 {
            eprintln!("Ошибка: Некорректный формат строки: {}", line);
            continue;
        }

        let pub_type: PublicationType = parts[0].parse().unwrap_or_else(|_| {
            eprintln!("Ошибка: Неверный тип публикации: {}", parts[0]);
            PublicationType::Newspaper
        });
        let name = parts[1].to_string();
        let cost = parts[2].parse::<f64>().unwrap_or_else(|_| {
            eprintln!("Ошибка: Неверный формат цены: {}", parts[2]);
            0.0
        });

        add_publication(
            pubs,
            Publication {
                pub_type,
                name,
                cost,
            },
        );
    }

    Ok(())
}

fn save_publications(pubs: &LinkedList<Publication>, filename: &str) -> io::Result<()> {
    let mut file = OpenOptions::new()
        .write(true)
        .create(true)
        .truncate(true)
        .open(filename)?;

    for pub_item in pubs {
        writeln!(
            file,
            "{}, {}, {}",
            pub_item.pub_type, pub_item.name, pub_item.cost
        )?;
    }

    Ok(())
}

fn main() {
    let mut pubs: LinkedList<Publication> = LinkedList::new();
    loop {
        println!(
            "\nМеню:
1. Добавить публикацию
2. Показать публикации
3. Загрузить из файла
4. Сохранить в файл
5. Выход"
        );

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).unwrap();
        let choice: u32 = choice.trim().parse().unwrap_or(0);

        match choice {
            1 => {
                let mut pub_type = String::new();
                println!("Введите тип (Газета или Журнал): ");
                io::stdin().read_line(&mut pub_type).unwrap();

                let pub_type: PublicationType = match pub_type.trim().parse() {
                    Ok(t) => t,
                    Err(_) => {
                        println!("Ошибка: Неверный тип публикации.");
                        continue;
                    }
                };

                let mut name = String::new();
                println!("Введите название: ");
                io::stdin().read_line(&mut name).unwrap();

                let mut cost = String::new();
                println!("Введите цену: ");
                io::stdin().read_line(&mut cost).unwrap();
                let cost: f64 = cost.trim().parse().unwrap_or_else(|_| {
                    println!("Ошибка: Неверный ввод цены.");
                    0.0
                });

                add_publication(
                    &mut pubs,
                    Publication {
                        pub_type,
                        name: name.trim().to_string(),
                        cost,
                    },
                );
                println!("Публикация добавлена.");
            }
            2 => {
                if pubs.is_empty() {
                    println!("Список пуст.");
                } else {
                    for pub_item in &pubs {
                        println!("{}", pub_item);
                    }
                }
            }
            3 => {
                let mut filename = String::new();
                println!("Введите имя файла: ");
                io::stdin().read_line(&mut filename).unwrap();
                if let Err(e) = load_publications(&mut pubs, filename.trim()) {
                    println!("Ошибка: Не удалось загрузить из файла: {}", e);
                } else {
                    println!("Публикации успешно загружены.");
                }
            }
            4 => {
                let mut filename = String::new();
                println!("Введите имя файла: ");
                io::stdin().read_line(&mut filename).unwrap();
                if let Err(e) = save_publications(&pubs, filename.trim()) {
                    println!("Ошибка: Не удалось сохранить в файл: {}", e);
                } else {
                    println!("Публикации успешно сохранены.");
                }
            }
            5 => {
                println!("Выход из программы.");
                break;
            }
            _ => println!("Ошибка: Неверный выбор."),
        }
    }
}
