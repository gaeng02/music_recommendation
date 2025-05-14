import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.environ.get("")
client_secret = os.environ.get("")

credentials = SpotifyClientCredentials(
    client_id = client_id,
    client_secret = client_secret
    )

sp = spotipy.Spotify(auth_manager = credentials)
