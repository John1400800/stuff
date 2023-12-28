import sqlite3


def track_list(artist_name: str) -> str:

    with sqlite3.connect(r'les10_SQLdatabase\theory\Chinook_Sqlite.sqlite') as music_db:
        c = music_db.cursor()
        c.execute(
            """SELECT DISTINCT Name FROM Track
                WHERE AlbumId IN (SELECT AlbumId FROM Album 
                        WHERE ArtistId = (SELECT ArtistId FROM Artist
                            WHERE Name = ?))
                            ORDER BY Name;""", (artist_name,))
        return '\n'.join([tpl[0] for tpl in c.fetchall()])


artist_name = input()
print(track_list(artist_name))
