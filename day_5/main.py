INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def solve(my_input):

    crates = []
    instructions = False

    for line in iter(my_input.splitlines()[1:]):
        if "[" in line:
            crates.append(line)
        elif instructions:
            if len(line.strip()) > 0:
                i_ = line.split(" ")
                n, start, end = [int(i_[x]) for x in [1, 3, 5]]
                while n > 0:
                    crates_organized[end - 1].append(crates_organized[start - 1].pop())
                    n -= 1
        else:
            indecies = [line.find(x) for x in "123"]
            crates_organized = [[] for x in indecies]
            instructions = True

            while crates:
                c = crates.pop()
                c = [c[ind] if c[ind] != " " else None for ind in indecies]

                for i, x in enumerate(c):
                    if x:
                        crates_organized[i].append(x)

    elf_code = "".join(
        [crates_organized[i].pop() for i in range(len(crates_organized))]
    )

    print(elf_code)


if __name__ == "__main__":

    solve(INPUT)
