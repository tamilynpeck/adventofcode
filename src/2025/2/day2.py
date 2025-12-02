class Day2:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        id_ranges = self.data[0].split(",")

        invalid_values = []

        for id_range in id_ranges:
            invalid_ids = self.invalid_id(id_range)
            invalid_values.extend(invalid_ids)

        return sum(invalid_values)

    def solve_part_two(self):
        id_ranges = self.data[0].split(",")

        invalid_values = []

        for id_range in id_ranges:
            invalid_ids = self.invalid_id_part_two(id_range)
            invalid_values.extend(invalid_ids)

        return sum(invalid_values)

    def invalid_id(self, line):
        starting, ending = map(int, line.split("-"))
        invalid_ids = []

        for num in range(starting, ending + 1):
            num_str = str(num)
            # divide str in half, check if both halves are the same
            half = len(num_str) // 2
            if num_str[:half] == num_str[half:]:
                invalid_ids.append(num)

        return invalid_ids

    def invalid_id_part_two(self, line):
        starting, ending = map(int, line.split("-"))
        invalid_ids = []

        for num in range(starting, ending + 1):
            num_str = str(num)
            len_num = len(num_str)
            # Try different numbers of parts (divisors of length)
            for num_parts in range(2, len_num + 1):
                if len_num % num_parts == 0:
                    part_size = len_num // num_parts
                    parts = [
                        num_str[j * part_size : (j + 1) * part_size]
                        for j in range(num_parts)
                    ]
                else:
                    continue

                if len(set(parts)) == 1:
                    invalid_ids.append(num)
                    break

        return invalid_ids
