import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="8e17206030f14c2383d748fc59c4da01",
                                               client_secret="bc989d63f7fb45faaa5f2fb48ffeb4cc",
                                               redirect_uri="http://localhost",
                                               scope="user-library-read"))