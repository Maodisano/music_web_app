from lib.database_connection import *
# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


# when i put an ablbum into albums 
# it will appear in GET / albums 


def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    post_response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
            "Album(1, In Rainbows, 2007, 1)\n" \
            "Album(2, Voyage, 2022, 2)" \
            

# test get all artists with properties

def test_get_all_artists(db_connection, web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
            "Artist(1, Pixies, Rock)\n" \
            "Artist(2, ABBA, Pop)\n" \
            "Artist(3, Taylor Swift, Pop)\n" \
            "Artist(4, Nina Simone, Jazz)" \
            

# test get just all artist names 

def test_get_all_artists(db_connection, web_client):
    response = web_client.get('/artists/names')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

# test post artists, checks get method to return all with properties 

def test_post_artist(web_client):
    response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
            "Artist(1, Pixies, Rock)\n" \
            "Artist(2, ABBA, Pop)\n" \
            "Artist(3, Taylor Swift, Pop)\n" \
            "Artist(4, Nina Simone, Jazz)\n" \
            "Artist(5, Wild Nothing, indie)" \
        
    second_response = web_client.get('/artists/names')
    assert second_response.status_code == 200
    assert second_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild Nothing'




# def test_get_albums(db_connection, web_client):
#     db_connection.seed = ('seeds/albums_table.sql')
#     response = web_client.get('/albums')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "Album(1, In Rainbows, 2007, 1)"


