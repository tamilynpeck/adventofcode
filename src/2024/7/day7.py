class Day7:
    def __init__(self, data):
        self.data = []
        for row in data:
            value, numbers = row.split(":")
            numbers = numbers.split()
            row = [int(value), [int(num) for num in numbers]]
            self.data.append(row)
            print(row)

    def solve_part_one(self):
        valid_values = []
        for row in self.data:
            value, numbers = row
            if self.test_combinations(value, numbers):
                valid_values.append(value)
        print(valid_values)
        return sum(valid_values)

    def solve_part_two(self):
        valid_values = []
        for row in self.data:
            value, numbers = row
            if self.test_combinations(value, numbers, True):
                valid_values.append(value)
        print(valid_values)
        return sum(valid_values)

    def test_combinations(self, expected_value, numbers, concat_operator=False):
        def generate_combinations(numbers):
            if len(numbers) == 1:
                return [str(numbers[0])]

            results = set()
            for i in range(1, len(numbers)):
                left = generate_combinations(numbers[:i])
                right = generate_combinations(numbers[i:])

                for l in left:
                    for r in right:
                        results.add(f"{l} + {r}")
                        results.add(f"{l} * {r}")
                        if concat_operator:
                            results.add(f"{l} || {r}")

            return results

        combinations = generate_combinations(numbers)
        for combo in combinations:
            result = eval_no_precedence(combo)
            # print(f"{combo} = {result}")
            if result == expected_value:
                print(f"Match found: {combo} = {expected_value}")
                return True
        return False


def eval_no_precedence(expression):
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = int(tokens[i + 1])
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        #  combines the digits from its left and right inputs into a single number. 12 || 345 would become 12345
        elif operator == "||":
            result = int(str(result) + str(operand))
        i += 2
    return result
