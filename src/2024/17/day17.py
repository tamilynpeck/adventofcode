class Day17:
    def __init__(self, data):
        self.data = data
        self.register_a = int(data[0].split(": ")[1])
        self.register_b = int(data[1].split(": ")[1])
        self.register_c = int(data[2].split(": ")[1])
        self.program = [int(x) for x in data[4].split(": ")[1].split(",")]
        self.output = []

        self.print_registers()

    def print_registers(self):
        print(f"A: {self.register_a}, B: {self.register_b}, C: {self.register_c}")
        print(self.program)

    def solve_part_one(self):
        for i, step in enumerate(self.program):
            print(f"Step {i}: {step}")
            if step % 2 != 0:
                continue
            combo_operand = self.get_combo_operand(i)
            literal_operand = self.program[i + 1]
            if step == 0:
                self.register_a = int(self.register_a / (2**combo_operand))
            elif step == 1:
                # calculates the bitwise XOR of register B and the instruction's literal operand
                self.register_b = self.register_b ^ literal_operand
            elif step == 2:
                # calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits)
                self.register_b = combo_operand % 8
            elif step == 3:
                if self.register_a == 0:
                    continue
                # it jumps by setting the instruction pointer to the value of its literal operand;
                # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
            elif step == 4:
                # bitwise XOR of register B and register C
                self.register_b = self.register_b ^ self.register_c
            elif step == 5:
                self.register_a = 0
            elif step == 6:
                self.register_b = int(self.register_a / (2**combo_operand))
            elif step == 7:
                self.register_c = int(self.register_a / (2**combo_operand))

        return ",".join([str(x) for x in self.output])

    def solve_part_two(self):
        pass

    def get_combo_operand(self, step):
        value = self.program[step + 1]
        if value == 4:
            return self.register_a
        elif value == 5:
            return self.register_b
        elif value == 6:
            return self.register_c
        else:
            return value
