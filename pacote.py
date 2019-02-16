import sys
from songcrawler import songcrawler

def main(argv):
    if len(argv) <= 2:
        print(songcrawler(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
