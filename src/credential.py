import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = ""
client_secret = ""

credentials = SpotifyClientCredentials(
    client_id = client_id,
    client_secret = client_secret
    )

sp = spotipy.Spotify(auth_manager = credentials)
