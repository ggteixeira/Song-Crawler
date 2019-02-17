import sys
from argparse import ArgumentParser
from scraper import scraper


def main(argv):
    return scraper(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
