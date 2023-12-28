ALL_CITIES: dict[str: tuple[str]] = {
    'Germany': ('Berlin', 'Hamburg', 'Munich', 'Cologne'),
    'Great Britain':
    ('London', 'Edinburgh', 'Royal Windsor', 'Roman-Era Bath'),
    'France': ('Paris', 'Marseille', 'Nice', 'Normandy'),
    'Netherlands':
    ('Amsterdam', 'Utrecht', 'Maastricht', 'Delft'),
    'Poland': ('Krakow', 'Warsaw', 'Gdansk', 'Wroclaw')
}

# вытаскивание нужных городов
def use_cities(use_countries: dict, dct_countrie_cities: dict) -> list:
    lst_use_cities = []
    for countrie in dct_countrie_cities.keys():
        if countrie in use_countries.keys():
            lst_use_cities.append(
                ((countrie, use_countries[countrie]),
                 dct_countrie_cities[countrie]))
    return lst_use_cities




print(use_cities())
