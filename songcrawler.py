import sys
from scraper import songs_finder


def main(*args):
    artist_name = ' '.join(map(str, *args))
    songs = songs_finder(artist_name)
    print(f"{len(songs)} songs from {artist_name.title()}.")
    print('\n'.join(songs))


if __name__ == "__main__":
    main(sys.argv[1:])
