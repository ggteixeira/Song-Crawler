import requests
from bs4 import BeautifulSoup


def scraper(*args):
    # Tratamento da string passada como parâmetro:
    band_name = '-'.join(map(str, *args)).lower()

    # Scraping:
    page = requests.get(f"https://www.vagalume.com.br/{band_name}/")
    soup = BeautifulSoup(page.text, 'html.parser')
    all_songs = soup.find_all(class_="nameMusic")

    songlist = list()
    for song_name in all_songs:
        songname = song_name.contents[0]
        songlist.append(songname)

    # Print da lista de canções
    song_count = len(songlist)
    print(f"O artista '{band_name}' possui {song_count} canções.")

    prompt = True  # Condição de parada melhor que o break
    while prompt:
        num = int(input("Quantas canções você deseja mostrar? \n"))
        if num > 0:
            if num > song_count:
                print("O número excede o total de canções. Tente novamente. \n")
            else:
                for song in songlist[:num]:
                    print(song)
                    prompt = False
        else:
            print("Você precisa selecionar o número de canções para mostrar. \n")
