import functools
from typing import List


class Monkey:
    def __init__(self, number: int,
                 items: List[int],
                 operation: str,
                 test: str,
                 if_true: str,
                 if_false: str) -> None:
        super().__init__()
        self.number = number
        items.reverse()
        self.items = items
        self.operation = eval("lambda old: " + operation.lstrip("new = "))
        self.test = int(test.replace("divisible by ", ""))
        self.if_true = int(if_true.replace("throw to monkey ", ""))
        self.if_false = int(if_false.replace("throw to monkey ", ""))

        self.inspects = 0

    def play(self):
        item = self.items.pop()
        self.inspects += 1

        # part 1
        # val = self.operation(item) // 3
        val = self.operation(item)

        res = val % self.test

        if res == 0:
            return self.if_true, val
        else:
            return self.if_false, val

    def __repr__(self) -> str:
        return f"""
        Monkey {self.number}:
        Items: {self.items}
        Operation: {self.operation}
        Test: {self.test}
        If true: {self.if_true}
        If false: {self.if_false}
        Inspects: {self.inspects}
        """


class KeepAway:
    def __init__(self, monkeys: List[Monkey]) -> None:
        super().__init__()
        self.monkeys = monkeys

    def play(self):
        for monkey in self.monkeys:
            while len(monkey.items) > 0:
                dest, item = monkey.play()
                self.monkeys[dest].items.insert(0, item)


def parse_monkey(inp):
    lines = inp.split("\n")
    number = int(lines[0].lstrip("Monkey ").rstrip(":"))
    items = list(map(int, lines[1].lstrip("Starting items: ").split(",")))
    operation = lines[2].replace("Operation: ", "")
    test = lines[3].replace("Test: ", "")
    if_true = lines[4].replace("If true: ", "")
    if_false = lines[5].replace("If false: ", "")
    return Monkey(number, items, operation, test, if_true, if_false)


def part1(inp):
    monkeys = []
    for monkey_string in inp.split("\n\n"):
        monkey = parse_monkey(monkey_string)
        monkeys.append(monkey)
    game = KeepAway(monkeys)

    for _ in range(20):
        game.play()

    monkeys.sort(key=lambda m: m.inspects, reverse=True)
    res = functools.reduce(lambda a, b: a * b,
                           map(lambda m: m.inspects, monkeys[0:2]))
    print(res)


def part2(inp):
    monkeys = []
    for monkey_string in inp.split("\n\n"):
        monkey = parse_monkey(monkey_string)
        monkeys.append(monkey)
    game = KeepAway(monkeys)

    for i in range(1000):
        print("round", i)
        for monkey in monkeys:
            print("Monkey", monkey.number, monkey.inspects)
        game.play()

    monkeys.sort(key=lambda m: m.inspects, reverse=True)
    res = functools.reduce(lambda a, b: a * b,
                           map(lambda m: m.inspects, monkeys[0:2]))
    print(res)


def main():
    with open("example.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
