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
* Install Python 3.x (Python 3.11 was used in development)
* Install `pytube` (to install, run `python3 -m pip install pytube`)
* Install `spotipy` (to install, run `python3 -m pip install spotipy`)
* Install `dotenv` (to install, run `python3 -m pip install python-dotenv`)
* Clone this repo
* Head over to your Spotify Developer Dashboard, and create a new app, and assign your Client ID and Client Secret in the `.env` file

You should now be able to run `main.py` and download your playlist for free

## Demo
A demo playlist created to showcase the working of this program is shown here:

![image](https://user-images.githubusercontent.com/97091148/212735840-9d6331c8-6914-4fb4-9015-6840a24500dd.png)

Running the `main.py` file, and entering the link for the demo playlist is shown here:

![image](https://user-images.githubusercontent.com/97091148/212738024-263d80b5-2d2b-4993-a5c5-979fcb8bb56b.png)

The main Python file then analyses the playlist, then starts downloading it. Progress of the downloading songs is shown here: 

![image](https://user-images.githubusercontent.com/97091148/212738084-6d64a1d6-29a7-45e0-9ec1-73d81a212297.png)

The downloaded songs are then saved in a directory, as shown here:

![image](https://user-images.githubusercontent.com/97091148/212738354-2e537b81-3194-4e61-af1a-2ff7ac8113b1.png)
