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

# You can translate all text here

title_message = Fore.CYAN + Style.BRIGHT + "============================"
app_name_message = Fore.CYAN + "    Spotify to YouTube MP3"
separator_message = Fore.CYAN + Style.BRIGHT + "============================"
playlist_prompt_message = Fore.BLUE + "[+] Please enter the Spotify playlist link: "
downloading_message = Fore.BLUE + "[...] Downloading: {}"
video_found_message = Fore.GREEN + "[!] YouTube video found: {}"
video_not_found_message = Fore.RED + "[!] No video found for: {}"
title_not_found_message = Fore.RED + "[!] Title not found for: {}"
search_message = Fore.YELLOW + "[...] Searching for video for the title: {}"
download_error_message = Fore.RED + "[X] Error downloading {}: {}"
youtube_search_error_message = Fore.RED + "[X] Error during YouTube search for {}: {}"