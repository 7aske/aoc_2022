import enum
from typing import List


class Opcode(enum.Enum):
    ADDX = "addx"
    NOOP = "noop"


class Instruction:
    def __init__(self, opcode: Opcode, *args) -> None:
        super().__init__()
        self.opcode = opcode
        self.args = list(args)

    def __repr__(self) -> str:
        return f"{self.opcode} {self.args}"

    @staticmethod
    def parse_instruction(line: str) -> "Instruction":
        args = line.split(" ")
        opcode = Opcode(args[0])

        return Instruction(opcode, *args[1:])


class Program:
    def __init__(self, instructions: List[Instruction]) -> None:
        super().__init__()
        self.instructions = instructions
        self.pc = 0
        self.x = 1
        self.signal_value = []
        self.output_cycles = [20, 60, 100, 140, 180, 220]
        self.draw_func = lambda x, y: None

    def on_draw(self, func):
        self.draw_func = func

    def run(self):
        for instruction in self.instructions:
            self.decode(instruction)

    def increment_pc(self, val: int = 1):
        for _ in range(val):
            self.draw_func(self.x, self.pc)
            self.pc += 1
            if self.pc in self.output_cycles:
                self.signal_value.append(self.pc * self.x)

    def decode(self, instruction: Instruction):

        if instruction.opcode == Opcode.ADDX:
            self.increment_pc(2)
            self.x += int(instruction.args[0])
        elif instruction.opcode == Opcode.NOOP:
            self.increment_pc()
        else:
            raise TypeError(
                "Unsupported instruction " + str(instruction.opcode))


def part2(inp):
    instructions = list(map(Instruction.parse_instruction, inp.split("\n")))
    program = Program(instructions)

    def draw(reg, pc):
        x = pc % 40
        if x == 0:
            print()
        if x - 1 == reg or x == reg or x + 1 == reg:
            print('#', end='')
        else:
            print('.', end='')

    program.on_draw(draw)

    program.run()


def part1(inp):
    instructions = list(map(Instruction.parse_instruction, inp.split("\n")))
    program = Program(instructions)
    program.run()
    print(program.pc, program.x, sum(program.signal_value))


def main():
    with open("input.txt") as file:
        inp = file.read()
        part2(inp)


if __name__ == '__main__':
    main()
