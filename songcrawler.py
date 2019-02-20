import sys
from scraper import songs_finder


def display_songs(songs_list, size):
    if size in range(1, len(songs_list)):
        filtered_list = map(lambda song: song, songs_list[:size])
    else:
        filtered_list = map(lambda song: song, songs_list)
    print("\n".join(filtered_list))


def display_artist_info(artist_name, size_of_songs):
    print(f"O artista {artist_name} possui {size_of_songs} canções. \n")


def ask_for_size():
    return int(input("Quantas canções você deseja mostrar? \n"))


def main(*args):
    artist_name = ' '.join(map(str, *args))
    songs = songs_finder(artist_name)
    display_artist_info(artist_name, len(songs))
    display_songs(songs, ask_for_size())


if __name__ == "__main__":
    main(sys.argv[1:])
