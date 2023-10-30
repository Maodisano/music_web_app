from lib.album import *

# contrusts with an id title release date and artist id

def test_construsts():
    album = Album(1, "test title", 1000, 2)
    assert album.id == 1
    assert album.title == "test title"
    assert album.release_year == 1000
    assert album.artist_id == 2

# output can be converted into strings
#  
def test_object_returns_string():
    album = Album(1, 'In Rainbows', 2007, 1)
    assert str(album) == "Album(1, In Rainbows, 2007, 1)"