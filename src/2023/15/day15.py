class Day15:
    def __init__(self, data):
        print(data)
        self.sequence = data[0].split(",")

    def solve_part_one(self):
        sequence_values = []
        for step in self.sequence:
            current_value = 0
            for char in step:
                char_code = ord(char)
                current_value += char_code
                current_value *= 17
                current_value %= 256
                print(char, char_code, current_value)

            sequence_values.append(current_value)

        return sum(sequence_values)

    def solve_part_two(self):
        pass
