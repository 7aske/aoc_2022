def get_top_score(x, y, matrix):
    tree = matrix[y][x]
    count = 0
    for y in range(y - 1, -1, -1):
        curr = matrix[y][x]
        count += 1
        if curr >= tree:
            break
    return count


def get_bottom_score(x, y, matrix):
    tree = matrix[y][x]
    count = 0
    for y in range(y + 1, len(matrix)):
        curr = matrix[y][x]
        count += 1
        if curr >= tree:
            break
    return count


def get_left_score(x, y, matrix):
    tree = matrix[y][x]
    count = 0
    for x in range(x - 1, -1, -1):
        curr = matrix[y][x]
        count += 1
        if curr >= tree:
            break
    return count


def get_right_score(x, y, matrix):
    tree = matrix[y][x]
    count = 0
    for x in range(x + 1, len(matrix[y])):
        curr = matrix[y][x]
        count += 1
        if curr >= tree:
            break
    return count


def part2(inp):
    matrix = []
    for line in inp.split("\n"):
        trees = list(map(int, list(line)))
        matrix.append(trees)

    max_score = 0
    matrix_len = len(matrix)
    for y in range(matrix_len):
        row_len = len(matrix[y])
        for x in range(row_len):
            top = get_top_score(x, y, matrix)
            bot = get_bottom_score(x, y, matrix)
            left = get_left_score(x, y, matrix)
            right = get_right_score(x, y, matrix)
            score = top * bot * left * right
            if score > max_score:
                max_score = score
    print(max_score)


def part1(inp):
    matrix = []
    visible = []
    for line in inp.split("\n"):
        trees = list(map(int, list(line)))
        matrix.append(trees)
        visible.append([False for _ in range(len(trees))])

    for y in range(len(matrix)):
        row_len = len(matrix[y])
        max_height = 0
        # left to right
        for x in range(row_len):
            current = matrix[y][x]
            if current > max_height or x == 0:
                visible[y][x] = True
                max_height = current

        max_height = 0
        # right to left
        for x in range(row_len - 1, -1, -1):
            current = matrix[y][x]
            if current > max_height or x == row_len - 1:
                visible[y][x] = True
                max_height = current

    for x in range(len(matrix[0])):
        matrix_len = len(matrix)
        max_height = 0
        # top to bottom
        for y in range(matrix_len):
            current = matrix[y][x]
            if current > max_height or y == 0:
                visible[y][x] = True
                max_height = current

        max_height = 0
        # bottom to top
        for y in range(len(matrix[0]) - 1, -1, -1):
            current = matrix[y][x]
            if current > max_height or y == matrix_len - 1:
                visible[y][x] = True
                max_height = current

    count = 0
    for line in visible:
        count += sum(map(int, line))

    print(count)


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
