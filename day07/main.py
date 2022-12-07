from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def get_size(self):
        pass


class File(Node):
    def __init__(self, name, size) -> None:
        super().__init__()
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __repr__(self) -> str:
        return f"FILE {self.name}({self.size})"


class Directory(Node):
    def __init__(self, name, parent) -> None:
        super().__init__()
        self.name = name
        self.parent = parent
        self.children = []

    def get_size(self):
        return sum(map(lambda x: x.get_size(), self.children))

    def __repr__(self) -> str:
        return f"DIR {self.name} [{self.children}]"


def parse_fs_tree(inp):
    root = Directory("/", None)
    pwd = root

    for line in inp.split("\n")[1:]:
        args = line.split(" ")

        if args[0] == "$":
            cmd = args[1]
            if cmd == "cd":
                if args[2] == "..":
                    pwd = pwd.parent
                else:
                    new_dir = Directory(pwd.name + "/" + args[2], pwd)
                    pwd.children.append(new_dir)
                    pwd = new_dir
            elif cmd == "ls":
                continue
        elif line.startswith("dir"):
            continue
        else:
            f = File(args[1], int(args[0]))
            pwd.children.append(f)

    return root


def part1(inp):
    root = parse_fs_tree(inp)

    size_sum = 0
    walk_stack = list(filter(lambda x: isinstance(x, Directory), root.children))

    while len(walk_stack) > 0:
        current = walk_stack.pop()
        size = current.get_size()
        if size <= 100000:
            size_sum += size

        for node in current.children:
            if isinstance(node, Directory):
                walk_stack.append(node)

    print(size_sum)


def part2(inp):
    root = parse_fs_tree(inp)

    dirs = []
    walk_stack = list(filter(lambda x: isinstance(x, Directory), root.children))

    free = 70000000 - root.get_size()
    required = 30000000 - free

    while len(walk_stack) > 0:
        current = walk_stack.pop()

        size = current.get_size()

        if size >= required:
            dirs.append(current)

        for node in current.children:
            if isinstance(node, Directory):
                walk_stack.append(node)

    print(min(*map(lambda x: x.get_size(), dirs)))


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
