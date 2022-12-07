def top_elem(stack):
    if len(stack) > 0:
        return stack[len(stack) - 1]
    return ""


def parse(inp):
    parsed_crates = []
    moves = []

    do_parse_crates = True
    for line in inp.split("\n"):
        if line == "":
            do_parse_crates = False
            parsed_crates.pop()
            continue
        if do_parse_crates:
            parsed_crates.append(line)
        else:
            moves.append(line)

    crates = [[] for _ in range(len(parsed_crates[0]) + 1 // 4)]
    for line in parsed_crates:
        data = [line[x:x + 3].replace("[", "").replace("]", "") for x in
                range(0, len(line), 4)]
        for i, item in enumerate(data):
            if item.isspace():
                continue
            crates[i].insert(0, item)

    return crates, moves


def move_stacks_of_elements(crates, moves):
    for move in moves:
        [_, num, _, src, _, dest] = move.split(" ")
        num = int(num)
        src = int(src)
        dest = int(dest)

        helper_stack = []
        len_to_move = min(len(crates[src - 1]), num)

        for _ in range(len_to_move):
            helper_stack.append(crates[src - 1].pop())

        for _ in range(len(helper_stack)):
            crates[int(dest) - 1].append(helper_stack.pop())

        helper_stack.clear()


def move_single_elements(crates, moves):
    for move in moves:
        [_, num, _, src, _, dest] = move.split(" ")
        for _ in range(int(num)):
            if len(crates[int(src) - 1]) > 0:
                item = crates[int(src) - 1].pop()
                crates[int(dest) - 1].append(item)


def part1(inp):
    crates, moves = parse(inp)

    move_single_elements(crates, moves)
    print("".join(map(top_elem, crates)))


def part2(inp):
    crates, moves = parse(inp)

    move_stacks_of_elements(crates, moves)
    print("".join(map(top_elem, crates)))


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
