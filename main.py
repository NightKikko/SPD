#
# Made by https://github.com/NightKikko, please fork the repo if you want to
# use it. Thanks for using the code ❤ (Can you star the repo? ^^) ⭐
#

import requests
from bs4 import BeautifulSoup
import urllib.parse
from pytubefix import YouTube
import aiotube
import os
import re
from colorama import init, Fore, Style

from text import *

init(autoreset=True)


def display_menu():
    print(title_message)
    print(app_name_message)
    print(separator_message)

def clean_title(title):
    cleaned_title = re.sub(r'[^a-zA-Z0-9 _]', '', title)
    cleaned_title = cleaned_title.replace(" ", "_")
    return cleaned_title if cleaned_title else "Untitled_Playlist"

def download_audio(youtube_url, output_folder):
    try:
        yt = YouTube(youtube_url)
        print(downloading_message.format(yt.title))
        ys = yt.streams.get_audio_only()
        ys.download(output_path=output_folder, mp3=True)
    except Exception as e:
        print(download_error_message.format(youtube_url, e))

display_menu()
url_playlist_spotify = input(playlist_prompt_message).strip()

response = requests.get(url_playlist_spotify)
soup = BeautifulSoup(response.text, 'html.parser')

playlist_title = soup.title.string.split('-')[0].strip() if soup.title else "Playlist"
playlist_title = clean_title(playlist_title)

if not os.path.exists(playlist_title):
    os.makedirs(playlist_title)

track_links = []

for track in soup.find_all('a', href=True):
    link = track['href']
    if "track" in link:
        track_links.append("https://open.spotify.com" + link)

for track_url in track_links:
    track_response = requests.get(track_url)
    track_soup = BeautifulSoup(track_response.text, 'html.parser')

    title = track_soup.title.string.split('|')[0].strip() if track_soup.title else "Title not found"

    if title != "Title not found":
        print(search_message.format(title))
        try:
            search = aiotube.Search.video(urllib.parse.quote(title))
            if search.metadata:
                youtube_video_url = f"https://www.youtube.com/watch?v={search.metadata['id']}"
                print(video_found_message.format(youtube_video_url))
                download_audio(youtube_video_url, playlist_title)
            else:
                print(video_not_found_message.format(title))
        except Exception as e:
            print(youtube_search_error_message.format(title, e))
    else:
        print(title_not_found_message.format(track_url))
    
    print("\n")
