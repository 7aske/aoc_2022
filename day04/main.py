def get_range(pair):
    [start, end] = pair.split("-")

    return int(start), int(end)


def complete_overlap(line):
    [first, second] = line.split(",")
    first_range = get_range(first)
    second_range = get_range(second)

    return (first_range[0] >= second_range[0] and first_range[1] <=
            second_range[1]) or (
            second_range[0] >= first_range[0] and second_range[1] <=
            first_range[1])


def partial_overlap(line):
    [first, second] = line.split(",")
    first_range = get_range(first)
    second_range = get_range(second)

    return (second_range[0] <= first_range[0] <= second_range[1]) or (
            second_range[0] <= first_range[1] <= second_range[1]) or (
            first_range[0] <= second_range[0] <= first_range[1]) or (
            first_range[0] <= second_range[1] <= first_range[1])


def part1(inp):
    print(len(list(filter(complete_overlap, inp.split("\n")))))


def part2(inp):
    print(len(list(filter(partial_overlap, inp.split("\n")))))


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
