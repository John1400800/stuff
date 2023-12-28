import sqlite3


def list_artists(gener: str):
    with sqlite3.connect(r'les10_SQLdatabase\theory\Chinook_Sqlite.sqlite') as music_db:
        c = music_db.cursor()
        c.execute(
            """SELECT DISTINCT Artist.Name FROM Genre
                LEFT JOIN Track ON Genre.GenreId = Track.GenreId
                LEFT JOIN Album ON Track.AlbumId = Album.AlbumId
                LEFT JOIN Artist ON Album.ArtistId = Artist.ArtistId
                WHERE Genre.Name = ?
                ORDER BY Artist.Name""", (gener,)
        )
        # return [tpl[0] for tpl in c.fetchall()]
        return '\n'.join([tpl[0] for tpl in c.fetchall()])


gener = input()
print(list_artists(gener))

lst_geners = [
    'Rock',
    'Jazz',
    'Metal',
    'Alternative & Punk',
    'Rock And Roll',
    'Blues',
    'Latin',
    'Reggae',
    'Pop',
    'Soundtrack',
    'Bossa Nova',
    'Easy Listening',
    'Heavy Metal',
    'R&B/Soul',
    'Electronica/Dance',
    'World',
    'Hip Hop/Rap',
    'Science Fiction',
    'TV Shows',
    'Sci Fi & Fantasy',
    'Drama',
    'Comedy',
    'Alternative',
    'Classical',
    'Opera'
]

res_lst = []
for gener in lst_geners:
    res_lst.extend(list_artists(gener))

print(len(set(res_lst)))
