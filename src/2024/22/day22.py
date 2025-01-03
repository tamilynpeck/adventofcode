class Day22:
    def __init__(self, data):
        self.data = [int(x) for x in data]
        print(self.data)

    def solve_part_one(self):
        numbers = []
        for secret_number in self.data:
            number = self.get_secret_number_n(secret_number)
            numbers.append(number)

        return sum(numbers)

    def get_secret_number_n(self, secret_number, n=2000):
        number = secret_number
        for _ in range(n):
            number = self.next_number(number)
        return number

    def solve_part_two(self):
        prices = []
        for secret_number in self.data:
            price = self.get_secret_number_pattern(secret_number)
            if price:
                prices.append(price)

        return sum(prices)

    def get_secret_number_pattern(self, secret_number, n=2000, pattern=[-2, 1, -1, 3]):
        # change_pattern = [-1, -1, 0, 2]  # -2,1,-1,3
        last_price = None
        recent_diffs = []
        number = secret_number
        for _ in range(n):
            number = self.next_number(number)
            price = self.get_ones_digit(number)
            if not last_price:
                last_price = price
                continue
            diff = price - last_price
            recent_diffs.append(diff)
            if len(recent_diffs) > 4:
                recent_diffs.pop(0)
            if recent_diffs == pattern:
                # print(
                #     secret_number,
                #     "price",
                #     price,
                #     "diffs",
                #     recent_diffs,
                # )
                return price
            last_price = price

    def next_number(self, secret_number):
        # Each step of the process involves mixing and pruning:
        # To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation.
        # To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation.

        # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        result = secret_number * 64
        secret_number = secret_number ^ result
        secret_number = secret_number % 16777216

        # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
        result = secret_number // 32
        secret_number = secret_number ^ result
        secret_number = secret_number % 16777216

        # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
        result = secret_number * 2048
        secret_number = secret_number ^ result
        secret_number = secret_number % 16777216

        return secret_number

    def get_ones_digit(self, number):
        return int(str(number)[-1])
