class Day9:
    def __init__(self, data):
        self.data = [int(x) for x in data[0]]
        print(self.data)

    def solve_part_one(self):
        blocks = self.individual_blocks(self.data)
        compact = self.file_compacting(blocks)
        checksum = self.checksum(compact)
        return checksum

    def individual_blocks(self, numbers):
        blocks = []
        file_id = 0
        for i, value in enumerate(numbers):
            if i % 2 == 0:
                for _ in range(value):
                    blocks.append(file_id)
                file_id += 1
            else:
                for _ in range(value):
                    blocks.append(".")
        return blocks

    def file_compacting(self, line):
        for _ in range(0, len(line), 2):
            if "." not in line:
                break

            next_space = line.index(".")
            line = line[:next_space] + [line[-1]] + line[next_space + 1 :]
            line = line[:-1]
        return line

    def checksum(self, numbers):
        values = [value * i for i, value in enumerate(numbers)]
        return sum(values)

    def solve_part_two(self):
        blocks = self.individual_blocks_part_two(self.data)
        compact = self.file_compacting_part_two(blocks)
        checksum = self.checksum(compact)
        return checksum

    def file_compacting_part_two(self, line):
        for _ in range(0, len(line), 2):
            if "." not in line:
                break

            next_space = line.index(".")
            line = line[:next_space] + [line[-1]] + line[next_space + 1 :]
            line = line[:-1]
        return line

    def individual_blocks_part_two(self, numbers):
        blocks = []
        file_id = 0
        for i, value in enumerate(numbers):
            if i % 2 == 0:
                blocks.append([file_id] * value)
                file_id += 1
            else:
                blocks.append(["."] * value)

        return blocks
