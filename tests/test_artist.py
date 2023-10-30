from lib.artist import *

def test_construsts():
    artist = Artist(1, "test", "punk")
    assert artist.id == 1
    assert artist.name == "test"
    assert artist.genre == "punk"

