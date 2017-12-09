import string


def score(stream: string) -> int:
    """Calculates the total score for all groups in stream.
    Advent of Code 2017, day 9, part 1."""
    return 0


if __name__ == '__main__':
    with open('day09_input.txt') as file:
        day09_input = file.read()

    print(score(day09_input))
