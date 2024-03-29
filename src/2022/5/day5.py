class Stacks:
    def __init__(self, crate_data):
        self.crate_data = crate_data

    @staticmethod
    def create_stacks(stacks):
        column_char_width = 3
        column_space_width = 1
        labels = [int(char) for char in stacks.pop() if char.isdigit()]
        max_len = max([len(row) for row in stacks])
        stacks = [row.ljust(max_len, " ") for row in stacks]
        crate_data = {key: [] for key in labels}

        for i, label in enumerate(labels):
            index = i * column_char_width + i * column_space_width
            for stack in stacks:
                crate = stack[index + 1].strip()
                if crate:
                    crate_data[label].insert(0, crate)

        return Stacks(crate_data)

    def top_crates(self):
        return "".join([self.crate_data[key][-1] for key in self.crate_data])


class CrateMover9000:
    @staticmethod
    def organize_crates(stacks, moves):
        for move in moves:
            count, from_stack, to_stack = [
                int(chars) for chars in move.split(" ") if chars.isdigit()
            ]
            for _ in range(0, count):
                crate = stacks[from_stack].pop()
                stacks[to_stack].append(crate)
        return Stacks(stacks)


class CrateMover9001:
    @staticmethod
    def organize_crates(stacks, moves):
        for move in moves:
            count, from_stack, to_stack = [
                int(chars) for chars in move.split(" ") if chars.isdigit()
            ]
            crates = [stacks[from_stack].pop() for _ in range(0, count)]
            stacks[to_stack].extend(crates[::-1])
        return Stacks(stacks)


class SupplyStacks:
    def __init__(self, data):
        self.stacks, self.moves = SupplyStacks.parse_data(data)

    def sort_crates(self, crate_mover=CrateMover9000):
        stacks = Stacks.create_stacks(self.stacks)
        organized_stacks = crate_mover.organize_crates(stacks.crate_data, self.moves)
        return organized_stacks.top_crates()

    @staticmethod
    def parse_data(data):
        stacks = [row for row in data if row and not row.startswith("move")]
        moves = [row for row in data if row.startswith("move")]

        return stacks, moves
