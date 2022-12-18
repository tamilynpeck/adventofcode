from SevenSegmentSearch import SevenSegmentSearch, Pattern

file = "test_input.txt"

input = SevenSegmentSearch.parse_input(file)


def test_parse_input():
    assert len(input) == 10


def test_count_unique_ouput_values():
    search = SevenSegmentSearch(input=input)
    assert search.count_unique_output_values() == 26


# def test_decoded_output_total():
#     search = SevenSegmentSearch(input=input)
#     assert search.decoded_output_total() == 61229


def test_decode_pattern():
    search = SevenSegmentSearch(input=input)
    key = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
    expected = {
        "acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1,
    }
    # assert search.decode_pattern(key) == expected
    pattern = Pattern(key.split(" "))
    assert pattern.key == expected


def test_pattern():
    assert Pattern.length[0] == 6
    assert Pattern.contained[0] == [8]


expected = {
    "acedgfb": 8,
    "cdfbe": 5,
    "gcdfa": 2,
    "fbcad": 3,
    "dab": 7,
    "cefabd": 9,
    "cdfgeb": 6,
    "eafb": 4,
    "cagedb": 0,
    "ab": 1,
}

test = {
    # 8: "1111111",
    1: "1100000",
    4: "1111000",

    7: "1010010"
    0: "1110111"

}