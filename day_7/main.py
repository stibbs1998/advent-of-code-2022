INPUT = """
"""


def sum_dict(dictionary):
    counter = 0
    for key in dictionary:
        if isinstance(dictionary[key], int):
            counter += dictionary[key]
        elif isinstance(dictionary[key], dict):
            counter += sum_dict(dictionary[key])

    return counter


def walk_path(path_sizes, obj):
    sum_for_path = sum_dict(obj)
    if sum_for_path <= 100_000:
        path_sizes.append(sum_for_path)
    for k, v in obj.items():
        if isinstance(v, dict):
            return walk_path(path_sizes, v)

    return sum(path_sizes)


def solve(my_input):

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
        if line[0] in "1234567890":
            size, file_name = line.split(" ")
            pwd[file_name] = int(size)

    return walk_path([], my_filepath)


if __name__ == "__main__":

    print(solve(INPUT))
