INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def parse_strategy(my_input):

    counter = 0
    for line in iter(my_input.splitlines()):
        divisor_index = int(len(line) / 2)
        front_set = set(line[:divisor_index])
        back_set = set(line[divisor_index:])
        shared_char = list(front_set.intersection(back_set))[0]
        bonus = (
            ord(shared_char) - 64 if shared_char.isupper() else ord(shared_char) - 96
        ) + (26 if shared_char.isupper() else 0)
        counter += bonus

    return counter


if __name__ == "__main__":

    print(parse_strategy(INPUT))
