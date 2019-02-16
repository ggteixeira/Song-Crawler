import sys
from songcrawler import songcrawler

def main(argv):
    if len(argv) == 1:
        return songcrawler(argv[0])
    elif len(argv) == 2:
        return songcrawler(argv[0], argv[1])
if __name__ == "__main__":
    main(sys.argv[1:])
