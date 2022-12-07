def part1(inp):
    l = []
    unique_len = 4
    for i, c in enumerate(inp):
        if len(l) == unique_len:
            l.pop(0)
        l.append(c)
        print(l)
        if len(set(l)) == unique_len:
            print(i + 1)
            return


def part2(inp):
    l = []
    unique_len = 14
    for i, c in enumerate(inp):
        if len(l) == unique_len:
            l.pop(0)
        l.append(c)
        print(l)
        if len(set(l)) == unique_len:
            print(i + 1)
            return


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
