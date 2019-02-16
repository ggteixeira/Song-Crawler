import requests
from bs4 import BeautifulSoup

def songcrawler(band_name):
    page = requests.get(f"https://www.vagalume.com.br/{band_name}/")
    soup = BeautifulSoup(page.text, 'html.parser')

    song_list = soup.find_all(class_="nameMusic")

    lista = list()
    for song_name in song_list:
        song = song_name.contents[0]
        lista.append(song)
    
    return print(lista)