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
        i = 50
        pass_zero_count = 0

        for rotation in self.data:
            i, passes = move_dial(i, rotation)
            pass_zero_count += passes

        return pass_zero_count


def move_dial(i, rotation):
    direction = rotation[0]
    num = int(rotation[1:])
    lock_len = 100
    pass_zero_count = 0

    if direction == "R":
        pass_zero_count = (i + num) // lock_len
        new_i = (i + num) % lock_len
        print("i", new_i, "+", rotation, i, pass_zero_count)
    else:
        if i == 0:
            # Starting at 0, don't count the starting position
            pass_zero_count = num // lock_len
        elif num > i:
            pass_zero_count = (num - i - 1) // lock_len + 1
        else:
            pass_zero_count = 1 if num == i else 0
        new_i = (i - num) % lock_len
        # handling scenario when lands on 0, is there a better way?
        if new_i == 0 and i != 0 and num > lock_len:
            pass_zero_count += 1
        print("i", new_i, "-", rotation, i, pass_zero_count)

    return new_i, pass_zero_count
