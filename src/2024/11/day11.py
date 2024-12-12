class Day11:
    def __init__(self, data):
        self.data = list(map(int, data[0].split(" ")))
        print(self.data)

    def solve_part_one(self, blinks=25):
        stones = self.data
        for _ in range(0, blinks):
            stones = Day11.blink(stones)
            print(stones)

        return len(stones)

    def solve_part_two(self):
        return self.solve_part_one(blinks=75)

    def blink(stones):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                first_half = int(str(stone)[:half])
                second_half = int(str(stone)[half:])
                new_stones.append(first_half)
                new_stones.append(second_half)
            else:
                value = stone * 2024
                new_stones.append(value)

        return new_stones
