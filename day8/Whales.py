from os import stat


class Whales:
    def __init__(self, input):
        self.input = input

    @staticmethod
    def build_and_sum_range_of_difference(value):
        return sum(range(1, value + 1, 1))

    @staticmethod
    def fuel_cost(crabs, position):
        return sum([abs(position - crab) for crab in crabs])

    @staticmethod
    def exponential_fuel_cost(crabs, position):
        return sum(
            [
                Whales.build_and_sum_range_of_difference(abs(position - crab))
                for crab in crabs
            ]
        )

    def lowest_fuel(self, exponential_cost=False):
        fuel_cost_func = (
            Whales.fuel_cost if not exponential_cost else Whales.exponential_fuel_cost
        )
        min_position = min(self.input)
        max_position = max(self.input)
        fuel_costs = []
        for position in range(min_position, max_position + 1):
            fuel_costs.append(fuel_cost_func(self.input, position))

        return min(fuel_costs)
