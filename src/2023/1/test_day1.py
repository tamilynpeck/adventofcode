import pytest
from day1 import Trebuchet
from utils import read_txt


def test_trebuchet_calibration():
    test_data = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""
    data = read_txt(test_data)

    trebuchet = Trebuchet(data)
    result = trebuchet.calibrate_sum()

    assert result == 142


@pytest.mark.parametrize(
    "line,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_trebuchet_calibration_value(line, expected):
    assert Trebuchet.calibration_value(line) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ("1abc2", "12"),
        ("pqr3stu8vwx", "38"),
        ("a1b2c3d4e5f", "12345"),
        ("treb7uchet", "7"),
        ("two1nine", "219"),
        ("eightwothree", "823"),
        ("abcone2threexyz", "123"),
        ("xtwone3four", "2134"),
        ("4nineeightseven2", "49872"),
        ("zoneight234", "18234"),
        ("7pqrstsixteen", "76"),
    ],
)
def test_interpret_line(value, expected):
    assert Trebuchet.interpret_line(value) == expected


def test_trebuchet_convert_text_to_int():
    test_data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    data = read_txt(test_data)

    trebuchet = Trebuchet(data)
    result = trebuchet.calibrate_sum_after_interpreting_data()

    assert result == 281
