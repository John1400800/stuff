import sqlite3


def album_list(genre_name: str) -> str:
    with sqlite3.connect(r'les10_SQLdatabase\theory\Chinook_Sqlite.sqlite') as music_db:
        c = music_db.cursor()
        c.execute(
            """SELECT DISTINCT Album.Title FROM Track
                INNER JOIN Genre ON Track.GenreId = Genre.GenreId
                INNER JOIN Album ON Track.AlbumId = Album.AlbumId
                INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
                WHERE Genre.Name = ?
                ORDER BY Artist.ArtistId, Album.Title;""", (genre_name,)
        )
        # return [tpl[0] for tpl in c.fetchall()]
        return '\n'.join([tpl[0] for tpl in c.fetchall()])


genre = input()
print(album_list(genre))

# lst_geners = [
#     'Rock',
#     'Jazz',
#     'Metal',
#     'Alternative & Punk',
#     'Rock And Roll',
#     'Blues',
#     'Latin',
#     'Reggae',
#     'Pop',
#     'Soundtrack',
#     'Bossa Nova',
#     'Easy Listening',
#     'Heavy Metal',
#     'R&B/Soul',
#     'Electronica/Dance',
#     'World',
#     'Hip Hop/Rap',
#     'Science Fiction',
#     'TV Shows',
#     'Sci Fi & Fantasy',
#     'Drama',
#     'Comedy',
#     'Alternative',
#     'Classical',
#     'Opera'
# ]

# res_lst = []
# for gener in lst_geners:
#     res_lst.extend(album_list(gener))

# print(len(set(res_lst)))
