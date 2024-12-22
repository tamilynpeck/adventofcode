class Day17:
    def __init__(self, data):
        self.data = data
        self.set_data()
        self.program = [int(x) for x in data[4].split(": ")[1].split(",")]
        self.output = []

        self.print_registers()

    def set_data(self):
        self.register_a = int(self.data[0].split(": ")[1])
        self.register_b = int(self.data[1].split(": ")[1])
        self.register_c = int(self.data[2].split(": ")[1])

    def print_registers(self):
        print(f"A: {self.register_a}, B: {self.register_b}, C: {self.register_c}")

    def solve_part_one(self):
        pointer = 0
        while pointer < len(self.program):
            opcode = self.program[pointer]
            combo_operand = self.get_combo_operand(pointer)
            literal_operand = self.program[pointer + 1]
            # print(f"Pointer {pointer}: {opcode} ({combo_operand}, {literal_operand})")
            new_pointer = self.evaluate(opcode, combo_operand, literal_operand)
            pointer = new_pointer if new_pointer is not None else pointer + 2

            # self.print_registers()
        return ",".join([str(x) for x in self.output])

    def solve_part_two(self):
        test_value = 0
        while self.program != self.output:
            self.set_data()
            self.register_a = test_value
            # print(f"Testing {test_value}")
            self.solve_part_one()
            if self.program == self.output:
                break
            test_value += 1
            if test_value == 10000:
                break

        return test_value

    def get_combo_operand(self, opcode):
        value = self.program[opcode + 1]
        if value == 4:
            return self.register_a
        elif value == 5:
            return self.register_b
        elif value == 6:
            return self.register_c
        else:
            return value

    def evaluate(self, opcode, combo_operand, literal_operand):
        if opcode == 0:
            self.register_a = int(self.register_a / (2**combo_operand))
        elif opcode == 1:
            # calculates the bitwise XOR of register B and the instruction's literal operand
            self.register_b = self.register_b ^ literal_operand
        elif opcode == 2:
            # calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits)
            self.register_b = combo_operand % 8
        elif opcode == 3:
            if self.register_a == 0:
                return
            # it jumps by setting the instruction pointer to the value of its literal operand;
            # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
            # print(f"Jumping to {literal_operand}")
            return literal_operand
        elif opcode == 4:
            # bitwise XOR of register B and register C
            self.register_b = self.register_b ^ self.register_c
        elif opcode == 5:
            # calculates the value of its combo operand modulo 8
            self.output.append(combo_operand % 8)
        elif opcode == 6:
            self.register_b = int(self.register_a / (2**combo_operand))
        elif opcode == 7:
            self.register_c = int(self.register_a / (2**combo_operand))
