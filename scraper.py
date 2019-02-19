import requests
from bs4 import BeautifulSoup


def songs_finder(artist):
    artist_name = artist.lower().replace(" ", "-")
    content = fetch_page_content(url_for(artist_name))

    html = parse_content_to_html(content)
    songs_anchors = find_songs_anchors(html)

    return list(map((lambda anchor: anchor.contents[0]), songs_anchors))


def url_for(artist):
    return f"https://www.vagalume.com.br/{artist}/"


def fetch_page_content(url):
    return requests.get(url)


def parse_content_to_html(content):
    return BeautifulSoup(content.text, "html.parser")


def find_songs_anchors(html):
    return html.find_all(class_="nameMusic")
