from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f'https://www.billboard.com/charts/hot-100/2022-07-09')
content = response.text
soup = BeautifulSoup(content, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

song_artist_spans = soup.select("li ul li span")
artist_names = [artist.getText().strip() for artist in song_artist_spans]
_artist_names = []
for artist in artist_names:
    if (not artist == '-') and (not artist.isdigit()):
        _artist_names.append(artist)


spotify_client_id = os.environ['SP_CLIENT_ID']
spotify_client_secret = os.environ['SP_CLIENT_SECRET']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=spotify_client_id,
        client_secret=spotify_client_secret,
        redirect_uri="https://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path='token.txt',
        username= os.environ['SP_USERNAME']
))

results = sp.current_user()
USER_ID = results['id']

song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{date.split('-')[0]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=USER_ID, name=f"BILLBOARD 100 - {date}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
