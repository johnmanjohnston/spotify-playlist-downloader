# spotify-playlist-downloder
Free Spotify playlist downloader, made using Python

## Introduction
This is a tool which lets you download a Spotify playlist, without paying for Spotify Premium. 
Compared to other Spotify playlist downloaders, this version is much more lightweight, and small.
`main.py` is where all the magic happens. The code lets you input a Spotify playlist link.
The songs from the playlist are analyzed, and then we use `pytube` to search for the song from YouTube.
The first result is then downloaded.

## Setup/Installation
(All the installation commands assume you're using Bash. If you're using PowerShell, replace `python` with `py` and you should recieve the same result)
> Install Python 3.x (Python 3.11 was used in development)
> Install `pytube` (to install, run `> python3 -m pip install pytube`)
> Install `spotipy` (to install, run `python3 -m pip install spotipy`)
> Install `dotenv` (to install, run `python3 -m pip install python-dotenv`)
> Clone this repo
> Head over to your Spotify Developer Dashboard, and create a new app, and assign your Client ID and Client Secret in the `.env` file

You should now be able to run `main.py` and download your playlist for free
