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
        ("33333", False, True),
        ("J3333", True, True),
        ("J3332", True, False),
        ("J3332", False, False),
        ("J2332", True, False),
        ("J2332", False, False),
        ("JJJJJ", True, True),
        ("JJJJJ", False, True),
    ],
)
def test_five_of_a_kind(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 6
    result = hand.five_of_a_kind()

    assert result == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("33332", False, True),
        ("33333", False, False),
        ("32233", False, False),
        ("J3332", False, False),
        ("3KTJJ", True, False),
        ("J3332", True, True),
        ("332JJ", True, True),
    ],
)
def test_four_of_a_kind(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 5
    result = hand.four_of_a_kind()

    assert result == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("23332", False, True),
        ("32T3K", False, False),
        ("22222", False, False),
        ("J2222", True, False),
        ("2J332", True, True),
        ("J3322", True, True),
        ("32T3J", True, False),
    ],
)
def test_full_house(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 4
    result = hand.full_house()

    assert result == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("QQQJA", False, True),
        ("32T3K", False, False),
        ("23332", False, False),
        ("32T3J", True, True),
        ("33T4J", True, True),
    ],
)
def test_three_of_a_kind(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 3
    result = hand.three_of_a_kind()

    assert result == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("23432", False, True),
        ("32T3K", False, False),
        ("23332", False, False),
        ("3KT4J", True, False),
        ("33T4J", True, False),
        ("3KTJJ", True, False),
    ],
)
def test_two_pair(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 2
    result = hand.two_pair()

    assert result == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("2K432", False, True),
        ("32T9K", False, False),
        ("23332", False, False),
        ("23432", False, False),
        ("3KT4J", True, True),
        ("3KT99", True, True),
        ("J37QA", True, True),
        ("J37QA", False, False),
    ],
)
def test_one_pair(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 1
    result = hand.one_pair()

    assert result == expected


@pytest.mark.parametrize(
    "hand,wild,expected",
    [
        ("2K439", False, True),
        ("32T9K", False, True),
        ("3KT4J", False, True),
        ("2K439", True, True),
        ("32T9K", True, True),
        ("23332", False, False),
        ("23432", False, False),
        ("3KT9J", True, False),
        ("J37QA", False, True),
    ],
)
def test_high_card(hand, wild, expected):
    hand = Hand(hand, 0, wild=wild)
    if expected:
        assert hand.type == 0
    result = hand.high_card()

    assert result == expected
