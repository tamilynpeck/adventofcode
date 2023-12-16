class Day15:
    def __init__(self, data):
        self.sequence = data[0].split(",")

    def solve_part_one(self):
        sequence_values = []
        for step in self.sequence:
            current_value = hash_algorithm(step)
            sequence_values.append(current_value)

        return sum(sequence_values)

    def solve_part_two(self):
        boxes = {}
        for step in self.sequence:
            if "=" in step:
                label, focal = step.split("=")
                lens = Lens(label, focal, operation="add")
            else:
                label, focal = step.split("-")
                lens = Lens(label, focal, operation="remove")

            box_number = lens.box_number
            if box_number not in boxes.keys():
                boxes[box_number] = Box(box_number)

            boxes[box_number].process_lens(lens)

        return sum([box.focusing_power() for box in boxes.values()])


def hash_algorithm(step):
    current_value = 0
    for char in step:
        char_code = ord(char)
        current_value += char_code
        current_value *= 17
        current_value %= 256

    return current_value


class Lens:
    def __init__(self, label, focal, operation):
        self.label = label
        self.focal = focal
        self.box_number = hash_algorithm(label)
        self.operation = operation

    def __repr__(self):
        return f"[{self.label} {self.focal}]"


class Box:
    def __init__(self, number):
        self.number = number
        self.items = []

    def process_lens(self, lens):
        if lens.operation == "add":
            self.add_item(lens)
        if lens.operation == "remove":
            self.remove_item(lens)

    def add_item(self, item):
        existing_i = [
            i for i, lens in enumerate(self.items) if lens.label == item.label
        ]
        if existing_i:
            i = existing_i[0]
            self.items[i].focal = item.focal
            self.items[i].box_number = self.number
        else:
            self.items.append(item)

    def remove_item(self, item):
        keep = [lens for lens in self.items if lens.label != item.label]
        self.items = keep

    def focusing_power(self):
        powers = []

        for i, lens in enumerate(self.items):
            power = (1 + self.number) * (i + 1) * int(lens.focal)
            powers.append(power)

        return sum(powers)

    def __repr__(self):
        return f"{self.items}"
