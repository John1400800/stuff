-- SELECT Track.Name as Track_Name, Album.Title as Album_Name, Artist.Name as Artist_Name FROM Artist
-- LEFT JOIN Album ON Artist.ArtistId = Album.ArtistId
-- LEFT JOIN Track ON Track.AlbumId = Album.AlbumId
-- WHERE Artist.Name LIKE 'A%' AND Album.Title != 'NULL'
-- ORDER BY Album.Title;

-- SELECT DISTINCT Genre_Name, Artist_Id, Album_Name FROM
-- (SELECT
--     Track.TrackId as Track_Id,
--     Track.Name as Track_Name,
--     Genre.GenreId as Genre_Id,
--     Genre.Name as Genre_Name,
--     Album.AlbumId as Album_Id,
--     Album.Title as Album_Name,
--     Artist.ArtistId as Artist_Id
-- FROM Track
-- INNER JOIN Genre ON Track.GenreId = Genre.GenreId
-- INNER JOIN Album ON Track.AlbumId = Album.AlbumId
-- INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
-- ORDER BY Artist_Id, Album_Name)
-- WHERE Genre_Name =  'Metal'


-- SELECT DISTINCT Album.Title FROM Track
-- INNER JOIN Genre ON Track.GenreId = Genre.GenreId
-- INNER JOIN Album ON Track.AlbumId = Album.AlbumId
-- INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
-- WHERE Genre.Name =  'Metal'
-- ORDER BY Artist.ArtistId, Album.Title;

-- SELECT 
--     Genre.GenreId as Genre_ID,
--     Genre.Name as Genre_Name,
--     Track.TrackId as Track_ID,
--     Track.Name as Track_Name,
--     Album.AlbumId as Album_ID,
--     Artist.ArtistId as Artist_ID,
--     Artist.Name as ARTIST_NAME
-- FROM Genre
-- INNER JOIN Track ON Genre.GenreId = Track.GenreId
-- INNER JOIN Album ON Track.AlbumId = Album.AlbumId
-- INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
-- WHERE Genre.Name = 'Rock'
-- ORDER BY Artist.Name



-- SELECT DISTINCT
--     Artist.Name
-- FROM Genre
-- INNER JOIN Track ON Genre.GenreId = Track.GenreId
-- INNER JOIN Album ON Track.AlbumId = Album.AlbumId
-- INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId
-- WHERE Genre.Name = 'Rock'
-- ORDER BY Artist.Name

SELECT DISTINCT GenreId FROM Track