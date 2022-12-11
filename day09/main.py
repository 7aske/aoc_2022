from enum import Enum


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    UP = "U"
    DOWN = "D"

    @staticmethod
    def parse(val):
        if val == "L":
            return Direction.LEFT
        if val == "R":
            return Direction.RIGHT
        if val == "U":
            return Direction.UP
        if val == "D":
            return Direction.DOWN


class Position:
    def __init__(self, func=None, prev=None) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self.move_func = lambda x, y: print(x, y) if func is None else func
        self.prev = prev if prev is not None else None

    def move(self, direction: Direction, amount: int):
        if direction is direction.LEFT:
            self.x -= amount
        if direction is direction.RIGHT:
            self.x += amount
        if direction is direction.UP:
            self.y += amount
        if direction is direction.DOWN:
            self.y -= amount

        if self.prev is not None:
            self.prev.move_to(self)

    def is_adjacent(self, other: "Position"):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def on_move(self, func):
        self.move_func = func

    def move_to(self, other: "Position"):
        while not self.is_adjacent(other):
            delta_x = self.x - other.x
            delta_y = self.y - other.y

            if delta_x > 0:
                self.x -= 1
            if delta_x < 0:
                self.x += 1

            if delta_y > 0:
                self.y -= 1
            if delta_y < 0:
                self.y += 1

        self.move_func(self.x, self.y)
        if self.prev is not None:
            self.prev.move_to(self)

    def __repr__(self) -> str:
        return f"({self.x},{self.y}, prev={self.prev})"


def part2(inp):
    positions = set()

    def on_move(x, y):
        print("M", x, y)
        positions.add((x, y))

    head = Position()
    tail = [head]
    for x in range(0, 9):
        pos = Position()
        tail[x].prev = pos
        tail.append(pos)
    tail[len(tail) - 1].on_move(on_move)

    for line in inp.split("\n"):
        direction, amount = line.split(" ")
        direction = Direction.parse(direction)
        amount = int(amount)

        for _ in range(amount):
            print("Moving head", direction)
            head.move(direction, 1)
    print(len(positions))


def print_head_tail(head: Position, tail: Position):
    for y in range(head.y - 3, head.y + 3):
        for x in range(head.x - 3, head.x + 3):
            if (x == tail.x) and (y == tail.y):
                print("T", end='')
            elif (x == head.x) and (y == head.y):
                print("H", end='')
            else:
                print(".", end='')
        print()


def part1(inp):
    head = Position()
    tail = Position()

    positions = set()

    def on_move(x, y):
        print("M", x, y)
        positions.add((x, y))

    tail.on_move(on_move)

    for line in inp.split("\n"):
        direction, amount = line.split(" ")
        direction = Direction.parse(direction)
        amount = int(amount)

        for _ in range(amount):
            print("Moving head", direction)
            head.move(direction, 1)
            print("T", tail)
            tail.move_to(head)
            print("H", head)

    print(len(positions))


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
