INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def sum_dict(dictionary):
    counter = 0
    for key in dictionary:
        if isinstance(dictionary[key], int):
            counter += dictionary[key]
        elif isinstance(dictionary[key], dict):
            counter += sum_dict(dictionary[key])

    return counter


def walk_path(directory_space, obj):
    sum_for_path = sum_dict(obj)
    directory_space.append(sum_for_path)
    for k, v in obj.items():
        if isinstance(v, dict):
            directory_space.append(walk_path(directory_space, v))

    return directory_space


def gather_system_files(my_input):
    my_filepath = {}
    pwd = my_filepath
    prev_wd = []

    for line in iter(my_input.splitlines()[1:]):
        if line[:4] == "$ cd":
            dir_name = line.split(" ")[2]
            if dir_name == "..":
                pwd = prev_wd.pop()  # Go up one level by popping the stack
            elif dir_name == "/":
                pwd = my_filepath  # Go to top level
                prev_wd = []
            elif dir_name not in pwd:
                prev_wd.append(pwd)  # Add previous folder to the stack
                pwd[dir_name] = {}  # Initialize folder
                pwd = pwd[dir_name]  # Make folder current directory
        if line[0] in "1234567890":  # A file has appeared
            size, file_name = line.split(" ")
            pwd[file_name] = int(size)

    # my_filepath = gather_system_files(my_input)
    directory_space = walk_path([], my_filepath)
    return directory_space


def solve_part_1(my_input):

    final_counter = 0
    for item in gather_system_files(my_input):
        if isinstance(item, int) and item <= 100_000:
            final_counter += item
    return final_counter


def solve_part_2(my_input):
    # Part 2
    MAX_DISK_SPACE = 70_000_000
    DESIRED_SPACE = 30_000_000

    directory_space = gather_system_files(my_input)
    CURRENT_SPACE = (
        MAX_DISK_SPACE - directory_space[0]
    )  # Top level directory, which is total disk space

    cheapest_to_delete = MAX_DISK_SPACE

    for item in directory_space:
        if (
            isinstance(item, int)
            and CURRENT_SPACE + item > DESIRED_SPACE
            and item < cheapest_to_delete
        ):  # if we reclaim that space, and it pushes us over DESIRED_SPACE
            cheapest_to_delete = item

    return cheapest_to_delete


if __name__ == "__main__":

    print(solve_part_1(INPUT))
    print(solve_part_2(INPUT))
