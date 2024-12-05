import pytest
from utils import read_txt
from day5 import Day5


test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def test_part_one():
    data = read_txt(test_data)
    program = Day5(data)

    result = program.solve_part_one()

    assert result == 143


def test_part_two():
    data = read_txt(test_data)
    program = Day5(data)

    result = program.solve_part_two()

    assert result == 123


@pytest.mark.parametrize(
    "line,expected",
    [(0, True), (1, True), (2, True), (3, False), (4, False), (5, False)],
)
def test_program_function(line, expected):
    data = read_txt(test_data)
    program = Day5(data)

    result = program.check_rules(program.updates[line])

    assert result == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        (3, ["97", "75", "47", "61", "53"]),
        (4, ["61", "29", "13"]),
        (5, ["97", "75", "47", "29", "13"]),
    ],
)
def test_program_function(line, expected):
    data = read_txt(test_data)
    program = Day5(data)

    result = program.correct_order(program.updates[line])

    assert result == expected


# def test_mapped_rules():
#     data = read_txt(test_data)
#     program = Day5(data)

#     result = program.sort_rules()

#     assert result == ["97", "75", "47", "61", "53", "29", "13"]


# def test_sort_by_rules():
#     data = read_txt(test_data)
#     program = Day5(data)

#     result = program.sort_rules(["75", "97", "47", "61", "53"])

#     assert result == ["97", "75", "47", "61", "53"]
