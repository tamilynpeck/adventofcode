class Day2:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        id_ranges = self.data[0].split(",")

        invalid_values = []

        for id_range in id_ranges:
            invalid_ids = self.valid_id(id_range)
            invalid_values.extend(invalid_ids)

        return sum(invalid_values)

    def solve_part_two(self):
        pass

    def valid_id(self, line):
        starting, ending = map(int, line.split("-"))
        invalid_ids = []

        for num in range(starting, ending + 1):
            num_str = str(num)
            # divide str in half, check if both halves are the same
            half = len(num_str) // 2
            if num_str[:half] == num_str[half:]:
                invalid_ids.append(num)

        return invalid_ids
