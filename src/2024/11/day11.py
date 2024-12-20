class Day11:
    def __init__(self, data):
        self.data = list(map(int, data[0].split(" ")))
        self.stones = {key: 1 for key in self.data}
        print(self.stones)

    def solve_part_one(self, blinks=25):
        stones = self.stones
        for _ in range(0, blinks):
            stones = Day11.blink(stones)

        return sum(stones.values())

    def solve_part_two(self):
        return self.solve_part_one(blinks=75)

    def blink(stones: dict):
        new_stones = {}
        for stone, count in stones.items():
            new = Day11.update_stone(stone)
            for n in new:
                if n in new_stones:
                    new_stones[n] += count
                else:
                    new_stones[n] = count

        return new_stones

    def update_stone(stone):
        if stone == 0:
            return [1]
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            first_half = int(str(stone)[:half])
            second_half = int(str(stone)[half:])
            return [first_half, second_half]
        else:
            value = stone * 2024
            return [value]
