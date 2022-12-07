from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase

priorities = {x: ord(x) - 38 for x in uppercase}
priorities.update({x: ord(x) - 96 for x in lowercase})


def part1(inp):
    s = 0
    for line in inp.split("\n"):
        first_half = set(line[:len(line) // 2])
        second_half = set(line[len(line) // 2:])

        for letter in first_half:
            if letter in second_half:
                print(first_half, second_half)
                print(letter, priorities[letter])
                s += priorities[letter]
    print(s)


def find_common(grp):
    found = {}
    for rucksack in grp:
        for item in set(rucksack):
            if item in found:
                found[item] += 1
            else:
                found[item] = 1

    for k, v in found.items():
        if v == 3:
            return k

    raise ValueError("No unique type across backpacks")


def part2(inp):
    lines = inp.split("\n")

    s = 0
    for grp in [lines[x:x + 3] for x in range(0, len(lines), 3)]:
        item = find_common(grp)
        print(item)
        s += priorities[item]
    print(s)


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
