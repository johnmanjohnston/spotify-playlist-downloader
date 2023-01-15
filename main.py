import spotipy
import pytube
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import dotenv

dotenv.load_dotenv()

CLIENTID = os.getenv("SPOTIFY_CLIENTID")
CLIENTSECRET = os.getenv("SPOTIFY_CLIENTSECRET")
playlistName = "Playlist";

def downloadAudio(url, fname):
    ytinst = pytube.YouTube(url)
    stream = ytinst.streams.filter(only_audio=True)
    stream[0].download(f"./{playlistName}", filename=f"{fname}.mp3")


playlist_link = "https://open.spotify.com/playlist/4ZozXBEWRXqnQrRTCwYFDR?si=10d72daafbf9488d"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENTID, client_secret=CLIENTSECRET)
spotifyinst = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
playlist_URI = playlist_link.split("/")[-1].split("?")[0]

track_uris = [x["track"]["uri"] for x in spotifyinst.playlist_tracks(playlist_URI)["items"]]

for track in spotifyinst.playlist_tracks(playlist_URI)["items"]:
    tname = track["track"]["name"]
    artname = track["track"]["artists"][0]["name"]

    s = pytube.Search(f"{tname} by {artname}")
    searchResults = []
    for v in s.results:
        searchResults.append(v.watch_url)
    os.system('cls' if os.name == 'nt' else 'clear')
            
    downloadAudio(searchResults[0], f"{tname} - {artname}")