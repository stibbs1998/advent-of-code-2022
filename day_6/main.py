INPUT = ""


def solve(my_input):
    CHARS = 14
    for i in range(len(my_input)):
        if len(set(my_input[i : i + CHARS])) == CHARS:
            print(i + CHARS)
            break


if __name__ == "__main__":

    solve(INPUT)
