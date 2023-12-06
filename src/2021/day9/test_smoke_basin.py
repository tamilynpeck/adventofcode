from SmokeBasin import SmokeBasin

file = "test_input.txt"

input = SmokeBasin.parse_input(file)


def test_parse_input():
    assert len(input) == 10
