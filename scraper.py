import requests
from bs4 import BeautifulSoup


def songs_finder(artist):

    # Recebe um nome de artista e trata a string p/ se adequar à URL
    artist_name = artist.lower().replace(" ", "-")

    # Recebe o conteúdo bruto de uma página, já com a URL completa
    content = fetch_page_content(url_for(artist_name))

    # Recebe uma página com seu conteúdo parseado
    html = parse_content_to_html(content)

    # Recebe uma lista de links para as canções, segundos seus nomes
    songs_anchors = find_songs_anchors(html)

    """Retorna uma lista, através do 'list()',
    com todos os conteúdos dentro dos anchors, através de 'anchor.contents[0]',
    a partir da lista de links, a 'songs_anchors'.
    """
    return list(map((lambda anchor: anchor.contents[0]), songs_anchors))


def url_for(artist):
    """Recebe o nome devidamente tratado de um artista
    e retorna sua URL completa, pronta para a raspagem de dados."""

    return f"https://www.vagalume.com.br/{artist}/"


def fetch_page_content(url):
    """Recebe uma URL e retorna uma página trazida da web."""
    return requests.get(url)


def parse_content_to_html(content):
    """Recebe o texto em HTML de uma página web
    e retorna um objeto com sua versão parseada"""
    return BeautifulSoup(content.text, "html.parser")


def find_songs_anchors(html):
    """Recebe um HTML parseado
    e encontra nele tudo que estiver dentro da classe 'nameMusic'
    """
    return html.find_all(class_="nameMusic")
