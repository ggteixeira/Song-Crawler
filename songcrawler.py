import requests
from bs4 import BeautifulSoup

def songcrawler(band_name, song_amount  = 0):
    page = requests.get(f"https://www.vagalume.com.br/{band_name}/")
    soup = BeautifulSoup(page.text, 'html.parser')

    all_songs = soup.find_all(class_="nameMusic")

    songlist = list()
    for song_name in all_songs:
        songname = song_name.contents[0]
        songlist.append(songname)
    
    for song in songlist:
        print(song)
    print(f"Você pediu {song_amount} canções!")
