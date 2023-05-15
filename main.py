import spotipy
import pytube
from spotipy.oauth2 import SpotifyClientCredentials
import os
import dotenv
import datetime
from time import sleep

dotenv.load_dotenv()
downloaded_songs = []
explicit_tag = " (explicit)" # Appends this if the song is explicit

def clr_trmnl(on_clr_callback=None): 
    os.system("cls" if os.name == "nt" else "clear")
    try: on_clr_callback()
    except: pass

def log_cur_progress():
    for song in downloaded_songs:
        print(song)


def init():
    global CLIENTID
    global CLIENTSECRET
    global playlist_link
    global playlistName

    CLIENTID = os.getenv("SPOTIFY_CLIENTID")
    CLIENTSECRET = os.getenv("SPOTIFY_CLIENTSECRET")
    
    playlistName = input("Enter the save directory: ")
    playlist_link = input("Enter the playlist URL: ")


def auth():
    global spotifyinst
    global playlist_URI

    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENTID, client_secret=CLIENTSECRET)
    spotifyinst = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]


def download_audio(url, fname, explicit):
    clr_trmnl(log_cur_progress)
    ytinst = pytube.YouTube(url, use_oauth=True, allow_oauth_cache=True)
    stream = ytinst.streams.filter(only_audio=True)

    processedfname = fname
    if explicit: processedfname += explicit_tag

    stream[0].download(f"./{playlistName}", filename=f"{processedfname}.mp3")
   
    song_index = downloaded_songs.index(f"{fname} - Downloading...")
    downloaded_songs[song_index] = f"{fname} - Downloaded!"
    clr_trmnl(log_cur_progress)


def begin_playlist_download():
    for track in spotifyinst.playlist_tracks(playlist_URI)["items"]:
        sleep(1)
        print("sleeping")
        tname = track["track"]["name"]
        artname = track["track"]["artists"][0]["name"]

        srch = pytube.Search(f"{tname} by {artname}")
        searchResults = []
        for v in srch.results:
            searchResults.append(v.watch_url)

        downloaded_songs.append(f"{tname} - {artname} - Downloading...")

        try:
            download_audio(searchResults[0], f"{tname} - {artname}", track["track"]["explicit"])
        except Exception as e: 
            downloaded_songs.append(f"{tname} - {artname} - Failed to Download ({e})")
            pass


def main():
    init()
    auth()
    begin_playlist_download()


if __name__ == "__main__":
    main()
