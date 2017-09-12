#!/usr/bin/python3

# Imports solely for typing
from typing import List, Callable
from io import TextIOWrapper

import argparse
from numpy.random import chisquare
from random import gauss, randint

# def chisquare(df: int, shape: Any=...) -> float: ...

GetRandomIndex = Callable[[int], int]

NUMBER_OF_DRAWS_TO_ATTEMPT: int = 50

ABS_Z_GENERATOR: GetRandomIndex = lambda length: int(abs(gauss(0, length/3)))
EQUAL_CHANCE_GENERATOR: GetRandomIndex = lambda length: randint(0, length - 1)
CHISQUARE_GENERATOR: GetRandomIndex = lambda length: int(chisquare(length//2))
RANDOM_NUMBER_GENERATION_RULE: GetRandomIndex = ABS_Z_GENERATOR


def getRandomIndex(length: int) -> int:
    # Choose a random number according to the rules defined in
    # RANDOM_NUMBER_GENERATION_RULE
    randomNumber: int = RANDOM_NUMBER_GENERATION_RULE(length)

    # Let's keep track of how many times we've drawn numbers.
    tries: int = 0
    # If we have too great an index, let's try again.
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


def processargs() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Randomly selects a movie.")
    parser.add_argument(
        '-i',
        '--input-file',
        help='The input file to pick movies from [default: movie_list.txt]',
        default="movie_list.txt",
        type=open,
    )

    return parser.parse_args()


def readInMovies(fd: TextIOWrapper) -> List[str]:
    output: List[str] = fd.readlines()
    fd.close()

    return output


# def main(args: List[str]) -> None:
def main() -> None:
    args = processargs()

    # Get the list of movies
    movies = readInMovies(args.input_file)

    assert len(movies) > 0, "Please add movies to the list."

    index = getRandomIndex(len(movies))

    print(movies[index][:-1])


if __name__ == '__main__':
    main()
