class Day1:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        lock = [x for x in range(0, 100)]
        i = 50
        password = 0

        for rotation in self.data:
            direction = rotation[0]
            num = int(rotation[1:])

            right_amount = (i + num) % len(lock)
            left_amount = (i - num) % len(lock)

            print(i, ">>", rotation)
            if direction == "R":
                i = right_amount
            else:
                i = left_amount

            if i == 0:
                password += 1

        return password

    def solve_part_two(self):
        lock = [x for x in range(0, 100)]
        i = 50
        pass_zero_count = 0

        for rotation in self.data:
            direction = rotation[0]
            num = int(rotation[1:])

            print(i, ">>")
            if direction == "R":
                right_amount = i + num
                new_i = right_amount % len(lock)
                quotient = right_amount // len(lock)
                print(rotation, new_i, quotient)
                pass_zero_count += quotient if i != 0 else max(0, quotient - 1)
                pass_zero_count += 1 if new_i == 0 and quotient == 0 else 0

                i = new_i
            else:
                left_amount = i - num
                new_i = left_amount % len(lock)
                quotient = left_amount // len(lock)
                print(rotation, new_i, quotient)
                pass_zero_count += (
                    abs(quotient) if i != 0 else max(0, abs(quotient) - 1)
                )
                pass_zero_count += 1 if new_i == 0 and abs(quotient) == 0 else 0
                i = new_i
            print(pass_zero_count)

        return pass_zero_count
