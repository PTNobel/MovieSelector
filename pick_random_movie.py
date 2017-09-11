#!/usr/bin/python3

from typing import List, Optional
import sys
from numpy.random import chisquare

# def chisquare(df: int, shape: Any=...) -> float: ...

NUMBER_OF_CHISQUARE_DRAWS_TO_ATTEMPT: int = 50
DISABLE_READ_IN_MOVIES: bool = False


def processargs(): ...


def readInMovies(fileName: Optional[str] = None) -> List[str]:
    if DISABLE_READ_IN_MOVIES:
        return ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if fileName is None:
        fileName = "./movie_list.txt"

    fd = open(fileName)
    output: List[str] = fd.readlines()
    fd.close()

    return output


def main(args: List[str]) -> None:
    """After substaintial discussion a number drawn from the chi-square
    distribution with df = len(movies)/2 was chosen as the means of picking
    a movie to watch. This is biased tolds older entries on the too-watch
    list. This method chooses a movie according to these rules."""
    # TODO implement arg processing etc.

    # Get the list of movies
    movies = readInMovies()

    # Choose a random number according to the rules described above.
    randomNumber: int = int(chisquare(len(movies)//2))

    # Let's keep track of how many times we've drawn numbers.
    tries: int = 0
    # If we have two great an index, let's try again.
    while randomNumber >= len(movies):
        # Draw a new number...
        randomNumber = int(chisquare(len(movies)//2))
        # We don't want the program to run forever... so let's just throw an
        # error after NUMBER_OF_CHISQUARE_DRAWS_TO_ATTEMPT.
        if tries > NUMBER_OF_CHISQUARE_DRAWS_TO_ATTEMPT:
            assert randomNumber >= len(movies), \
                "Random number generator failed. Check numpy install"
        tries += 1

    print(movies[int(randomNumber)])


if __name__ == '__main__':
    main(sys.argv)
