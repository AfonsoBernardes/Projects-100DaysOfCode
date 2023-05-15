import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_ID = os.environ.get("SPOTIFY_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
SPOTIFY_URI = os.environ.get("SPOTIFY_URI")
soup = BeautifulSoup()

date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")
year = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")

# Scrape website to retrieve top songs and corresponding artist.
top_songs = soup.select("li ul li h3")
top_songs_list = [song.getText().strip() for song in top_songs]
artists = soup.select("li ul li span")
artists_list = [artist.getText().strip() for artist in artists][::7]

songs_and_artist = zip(top_songs_list, artists_list)


# Setup Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Search Billboard songs on Spotify.
songs_uris = []
for song, artist in songs_and_artist:
    result = sp.search(q=f"track:{song} artist:{artist}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print("This song does not exist on Spotify. Skipped")


# Add songs to playlist.
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, )
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)
print(f"New playlist '{date} Billboard 100' successfully created on Spotify!")

