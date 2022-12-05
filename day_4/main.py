INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def parse_strategy(my_input):

    counter = 0
    for line in iter(my_input.splitlines()):
        first_pair, second_pair = line.split(",")
        first_set = set(
            range(int(first_pair.split("-")[0]), int(first_pair.split("-")[1]) + 1, 1)
        )
        second_set = set(
            range(int(second_pair.split("-")[0]), int(second_pair.split("-")[1]) + 1, 1)
        )

        # If Intersection = 1st/2nd Set, full overlap
        counter += (
            1
            if first_set.intersection(second_set) == first_set
            or first_set.intersection(second_set) == second_set
            else 0
        )

    print(counter)


if __name__ == "__main__":

    parse_strategy(INPUT)
