def get_win(shape):
    if shape == 1:
        return 2
    if shape == 2:
        return 3
    if shape == 3:
        return 1


def get_draw(shape):
    return shape


def get_lose(shape):
    if shape == 1:
        return 3
    if shape == 2:
        return 1
    if shape == 3:
        return 2


def translate(a):
    if a == "X" or a == "A":
        return 1
    elif a == "Y" or a == "B":
        return 2
    elif a == "Z" or a == "C":
        return 3


def translate_result(opponent, result):
    if result == 'X':
        return get_lose(opponent)
    if result == 'Y':
        return get_draw(opponent)
    if result == 'Z':
        return get_win(opponent)


def get_result(line):
    [first, second] = line.split(" ")
    first_tr = translate(first)
    # part 1
    # second_tr = translate(second)

    # part 2
    second_tr = translate_result(first_tr, second)

    if first_tr == second_tr:
        return second_tr + 3

    if (second_tr == 3 and first_tr == 2) or (
            second_tr == 2 and first_tr == 1) or (
            second_tr == 1 and first_tr == 3):
        return second_tr + 6

    return second_tr


def main():
    with open("input.txt") as file:
        inp = file.read()
        a = sum(map(get_result, inp.split("\n")))
        print(a)


if __name__ == '__main__':
    main()
