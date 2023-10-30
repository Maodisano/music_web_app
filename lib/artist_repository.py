from lib.artist import *

class ArtistRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM artists')
        return [ 
            Artist(row["id"], row["name"], row["genre"])
            for row in rows
            ]
    
    def artist_names(self):
        rows = self.connection.execute('SELECT name FROM artists')
        return [row["name"] for row in rows]

    # new function which returns only the names of each of the artists 

    def create(self, artist):
        self.connection.execute(
            'INSERT INTO artists (name, genre) VALUES (%s, %s)', 
                                [artist.name, artist.genre]
            )
        return None