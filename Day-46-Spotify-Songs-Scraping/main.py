from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os

user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ").strip()

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_input}")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.prettify())

songs = []
song_titles = soup.select("li ul li h3")
for song in song_titles:
    songs.append(song.getText().strip())
    print(song.getText().strip())

# Authenticate Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get('client_id'),
        client_secret=os.environ.get('client_secret'),
        show_dialog=True,
        cache_path="token.txt",
        username=os.environ.get('username'),
    )
)
user_id = sp.current_user()['id']
sunidhi_uri = 'spotify:artist:3eDT9fwXKuHWFvgZaaYC5v'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(sunidhi_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
