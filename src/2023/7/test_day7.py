import pytest
from utils import read_txt
from day7 import Day7, Hand

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_day7():
    data = read_txt(test_data)
    program = Day7(data)

    result = program.solve_part_one()

    assert result == 6440


def test_day7_part_two():
    data = read_txt(test_data)
    program = Day7(data, wild=True)

    result = program.solve_part_two()

    assert result == 5905


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("33333", False, 4),
        ("J3333", True, 4),
        # ("J3332", True, False),
        # ("J3332", False, False),
        # ("J2332", True, False),
        # ("J2332", False, False),
        ("JJJJJ", True, 4),
        ("JJJJJ", False, 4),
    ],
)
def test_five_of_a_kind(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("33332", False, 2),
        # ("33333", False, False),
        # ("32233", False, False),
        # ("J3332", False, False),
        # ("3KTJJ", True, False),
        ("J3332", True, 2),
        ("332JJ", True, 2),
    ],
)
def test_four_of_a_kind(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("23332", False, 1),
        # ("32T3K", False, False),
        # ("22222", False, False),
        # ("J2222", True, False),
        ("2J332", True, 1),
        ("J3322", True, 1),
        # ("32T3J", True, False),
    ],
)
def test_full_house(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("QQQJA", False, 0),
        # ("32T3K", False, False),
        # ("23332", False, False),
        ("32T3J", True, 0),
        ("33T4J", True, 0),
    ],
)
def test_three_of_a_kind(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("23432", False, -1),
        # ("32T3K", False, False),
        # ("23332", False, False),
        # ("3KT4J", True, False),
        # ("33T4J", True, False),
        # ("3KTJJ", True, False),
    ],
)
def test_two_pair(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("2K432", False, -2),
        # ("32T9K", False, False),
        # ("23332", False, False),
        # ("23432", False, False),
        ("3KT4J", True, -2),
        ("3KT99", True, -2),
        ("J37QA", True, -2),
        # ("J37QA", False, False),
    ],
)
def test_one_pair(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("2K439", False, -4),
        ("32T9K", False, -4),
        ("3KT4J", False, -4),
        ("2K439", True, -4),
        ("32T9K", True, -4),
        ("J37QA", False, -4),
    ],
)
def test_high_card(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)

    assert hand.type_strength == expected
