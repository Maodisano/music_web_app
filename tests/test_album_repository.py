from lib.album_repository import *
from lib.album import *

# when i call all(), 
# a list of all albums is returned 

def test_all(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [ Album(1, 'In Rainbows', 2007, 1)]

# when i call create()
# i create and album in the database that can be returned 

def test_create(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = AlbumRepository(db_connection)
    album = Album(2, "test title", 1000, 2)
    repository.create(album)
    assert repository.all() == [ 
                Album(1, "In Rainbows", 2007, 1),
                Album(2, "test title", 1000, 2)]
