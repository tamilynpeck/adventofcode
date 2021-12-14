from Whales import Whales

input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_align_crabs():
    whales = Whales(input=input)
    assert whales.lowest_fuel() == 37


def test_fuel_cost():
    assert Whales.fuel_cost(input, 1) == 41
    assert Whales.fuel_cost(input, 3) == 39
    assert Whales.fuel_cost(input, 10) == 71


def test_align_crabs_exponential_cost():
    whales = Whales(input=input)
    assert whales.lowest_fuel(exponential_cost=True) == 168


def test_exponential_fuel_cost():
    assert Whales.exponential_fuel_cost(input, 5) == 168
    assert Whales.exponential_fuel_cost(input, 2) == 206
