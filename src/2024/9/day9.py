class Day9:
    def __init__(self, data):
        self.data = [int(x) for x in data[0]]

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
        values = [int(value) * i for i, value in enumerate(numbers) if value != "."]
        return sum(values)

    def solve_part_two(self):
        blocks = self.individual_blocks_part_two(self.data)
        values = "".join([str(value) for values in blocks for value in values])
        print(values[:100])
        compact = self.file_compacting_part_two(blocks)
        checksum = self.checksum_part_two(compact)
        return checksum

    def file_compacting_part_two(self, file):
        f = len(file) - 1

        def find_index_with_space(length):
            for i, values in enumerate(file):
                if "." in values and length <= len(values):
                    return i

        while f > 0:
            # log = False
            value = file[f]
            if "." in value:
                f -= 1
                continue
            # if len(value) > 1 and value[0] == 9830:
            #     log = True
            value_len = self.len_of_list_values(value)
            index = find_index_with_space(value_len)
            # if log:
            #     print(f, value, index)
            if index is None or index >= f:
                f -= 1
                continue

            if value_len == len(file[index]):
                file[index] = value
            else:
                rem_prev_values = file[index][: len(file[index]) - value_len]
                file[index] = value
                file.insert(index + 1, rem_prev_values)
                f += 1

            file[f] = ["." for _ in range(value_len)]
            if f < len(file) - 1 and "." in file[f] and "." in file[f + 1]:
                file[f] = file[f] + file[f + 1]
                del file[f + 1]
            if "." in file[f] and "." in file[f - 1]:
                file[f] = file[f - 1] + file[f]
                del file[f - 1]
                f -= 1

            f -= 1

        return file

    def individual_blocks_part_two(self, numbers):
        blocks = []
        file_id = 0
        for i, value in enumerate(numbers):
            if i % 2 == 0:
                blocks.append([file_id] * value)
                file_id += 1
            elif value > 0:
                blocks.append(["."] * value)

        return blocks

    def checksum_part_two(self, numbers):
        values = "".join([str(value) for values in numbers for value in values])
        print(values)
        return self.checksum([x for x in values])

    def len_of_list_values(self, values):
        values = "".join([str(value) for value in values])
        return len(values)
