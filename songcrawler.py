import sys
from scraper import scraper


def main(argv):
    # if len(argv) == 1:
        return scraper(argv)
    # elif len(argv) == 2:
    #     return scraper(argv[0], (argv[1]))


if __name__ == "__main__":
    main(sys.argv[1:])
