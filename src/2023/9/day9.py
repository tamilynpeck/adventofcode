class Day9:
    def __init__(self, data):
        self.data = data
        self.histories = [history.split(" ") for history in data]

    def solve_part_one(self):
        next_numbers = []
        for history in self.histories:
            next_numbers.append(Day9.solve_next_in_history(history))

        return sum(next_numbers)

    def solve_part_two(self):
        next_numbers = []
        for history in self.histories:
            next_numbers.append(Day9.solve_next_in_history(history[::-1]))

        return sum(next_numbers)

    def solve_next_in_history(history):
        history_sequence = [[int(number) for number in history]]

        for sequence in history_sequence:
            prev = sequence[0]
            next_sequence = [-prev + (prev := x) for x in sequence[1:]]
            history_sequence.append(next_sequence)
            if all(x == 0 for x in next_sequence):
                break

        last_values = [sequence[-1] for sequence in history_sequence[::-1]]
        prev = last_values[0]
        calc = [prev := (prev + x) for x in last_values[1:]]

        return calc[-1]
