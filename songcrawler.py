import sys
from scraper import songs_finder

def filter_songs(songs_list):
    prompt = True
    print(f"O artista escolhido possui {len(songs_list)} canções. \n")
    
    while prompt:
        num = int(input("Quantas canções você deseja mostrar? \n"))
        if num > 0:
            if num > len(songs_list):
                print("O número excede o total de canções. Tente novamente.")
            else:
                filtered_list = map(lambda song: song, songs_list[:num]) 
                prompt = False
    
    print('\n'.join(filtered_list))

def main(*args):
    artist_name = ' '.join(map(str, *args))
    songs = songs_finder(artist_name)
    # print(f"{len(songs)} songs from {artist_name.title()}.")
    # print('\n'.join(songs))
    return songs

if __name__ == "__main__":
    filter_songs(main(sys.argv[1:]))
