import string
import networkx as nx

from aoc.day10.day10 import knot_hash


def disk(s: string) -> list:
    """Generates the disk for the given string (using 0s and 1s instead of #s and .s)."""
    rows = []
    for i in range(128):
        h = bin(int(knot_hash(f'{s}-{i}'), 16))[2:]
        rows.append(list(h))
    return rows


def square_count(s: string) -> int:
    """Counts the number of squares in the disk for the given string.
    Advent of Code 2017, day 14, part 1."""
    d = disk(s)
    total = 0
    for r in d:
        total += sum(int(x) for x in r)
    return total


def region_count(s: string) -> int:
    """Counts the number of regions in the disk for the given string.
    Advent of Code 2017, day 14, part 2."""
    g = nx.Graph()
    d = disk(s)

    for row in range(len(d)):
        for col in range(len(d[row])):
            current_node = f'{row},{col}'
            if d[row][col] == 1 and current_node not in list(g.nodes):
                g.add_node(current_node)
                try:
                    test_node = f'{row + 1},{col}'
                    if d[row + 1][col] == 1 and test_node not in list(g.nodes):
                        g.add_node(test_node)
                        g.add_edge(current_node, test_node)
                    test_node = f'{row},{col + 1}'
                    if d[row + 1][col] == 1 and test_node not in list(g.nodes):
                        g.add_node(test_node)
                        g.add_edge(current_node, test_node)
                    test_node = f'{row - 1},{col}'
                    if d[row + 1][col] == 1 and test_node not in list(g.nodes):
                        g.add_node(test_node)
                        g.add_edge(current_node, test_node)
                    test_node = f'{row},{col - 1}'
                    if d[row + 1][col] == 1 and test_node not in list(g.nodes):
                        g.add_node(test_node)
                        g.add_edge(current_node, test_node)
                except IndexError:
                    pass

    return nx.number_connected_components(g)


if __name__ == '__main__':
    day14_input = 'ffayrhll'
    print(square_count(day14_input))
    print(region_count(day14_input))
