from lib.artist_repository import *
from lib.artist import *

# when i call all(), 
# a list of all artists are returned 

def test_all(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [ 
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
        ]
    
# when i call artist_names()
# a list of artist names appears 

def test_artist_names(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = ArtistRepository(db_connection)
    assert repository.artist_names() == [ 
        ('Pixies'),
        ('ABBA'),
        ('Taylor Swift'),
        ('Nina Simone')
    ]

def test_create(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(5, "test", "blues")
    repository.create(artist)
    assert repository.all() == [ 
                Artist(1, 'Pixies', 'Rock'),
                Artist(2, 'ABBA', 'Pop'),
                Artist(3, 'Taylor Swift', 'Pop'),
                Artist(4, 'Nina Simone', 'Jazz'),
                Artist(5, 'test', 'blues')
                ]