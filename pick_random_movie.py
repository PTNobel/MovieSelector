#!/usr/bin/python3

from typing import List, Optional, Callable
import sys
from numpy.random import chisquare
from random import gauss

# def chisquare(df: int, shape: Any=...) -> float: ...

GetRandomIndex = Callable[[int], int]

NUMBER_OF_DRAWS_TO_ATTEMPT: int = 50
DISABLE_READ_IN_MOVIES: bool = False
ABS_Z_GENERATOR: GetRandomIndex = lambda length: int(abs(gauss(0, length/3)))
CHISQUARE_GENERATOR: GetRandomIndex = lambda length: int(chisquare(length//2))
RANDOM_NUMBER_GENERATION_RULE: GetRandomIndex = ABS_Z_GENERATOR


def getRandomIndex(length: int) -> int:
    # Choose a random number according to the rules defined in
    # RANDOM_NUMBER_GENERATION_RULE
    randomNumber: int = RANDOM_NUMBER_GENERATION_RULE(length)

    # Let's keep track of how many times we've drawn numbers.
    tries: int = 0
    # If we have two great an index, let's try again.
    while randomNumber >= length:
        # Draw a new number...
        randomNumber = RANDOM_NUMBER_GENERATION_RULE(length)
        # We don't want the program to run forever... so let's just throw an
        # error after NUMBER_OF_DRAWS_TO_ATTEMPT.
        if tries > NUMBER_OF_DRAWS_TO_ATTEMPT:
            assert randomNumber >= length, \
                "Random number generator failed. Check numpy install"
        tries += 1

    return randomNumber


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
        # TODO implement arg processing etc.

    # Get the list of movies
    movies = readInMovies()

    index = getRandomIndex(len(movies))

    print(movies[index])


if __name__ == '__main__':
    main(sys.argv)
