def steps(n: int) -> int:
    """Calculates the Manhattan Distance between n and 1.
    Advent of Code 2017, day 3, part 1."""

    def smaller_odd_square(num: int) -> int:
        """Finds the largest odd n such that n^2 < num."""
        current = 1
        while (current + 2)**2 < num:
            current += 2
        return current

    def adj_distances(shell_num: int) -> list:
        """Creates a list of the form [shell_num - 1, shell_num - 2, ..., 0, 1, ..., shell_num]."""
        if shell_num == 0:
            return [0, 1]

        d = [shell_num - 1]
        while d[-1] != 0:
            d.append(d[-1] - 1)
        for i in range(1, shell_num + 1):
            d.append(i)
        return d

    if n == 1:
        return 0

    square = smaller_odd_square(n)
    shell = (square + 1) // 2
    index = n - (square**2 + 1)
    distances = adj_distances(shell)
    adj = distances[index % len(distances)]

    return shell + adj


def first_larger(n: int) -> int:
    """Returns the first vaue written larger than n.
    IDEA: Represent the spiral with a dictionary. The key is a tuple (or string/int, whatever works)
    that represents the row and column so adjacent ones can always be easily referenced.
    Advent of Code 2017, day 3, part 2."""
    return 1


if __name__ == '__main__':
    day03_input = 265149
    print(steps(day03_input))
    print(first_larger(day03_input))
