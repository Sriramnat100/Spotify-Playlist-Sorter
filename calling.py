import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="http://localhost",
                                               scope="user-library-read"))