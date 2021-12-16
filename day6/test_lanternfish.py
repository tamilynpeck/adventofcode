from LanternFish import LanternFish

input = [3, 4, 3, 1, 2]


def test_number_of_fish():
    fish = LanternFish(input)
    assert fish.days(18) == 26
    assert fish.days(80) == 5934
    # assert fish.days(256) == 26984457539


def test_large_number_of_fish():
    fish = LanternFish(input)
    assert fish.better_days(18) == 26
    assert fish.better_days(80) == 5934
    # assert fish.days(256) == 26984457539
