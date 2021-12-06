from HydrothermalVenture import HydrothermalVenture

file = "test_input.txt"

with open(file) as input_file:
    input = [line.strip() for line in input_file.readlines()]


def test_file_import():
    venture = HydrothermalVenture(input)
    assert venture.input[0] == [[0, 9], [5, 9]]


def test_map_lines():
    venture = HydrothermalVenture(input)
    assert venture.all_points[0] == "0,9"


def test_count():
    venture = HydrothermalVenture(input)
    assert venture.overlap_points == 5


def test_diagonal():
    venture = HydrothermalVenture(input, diagonal=True)
    assert venture.input[0] == [[0, 9], [5, 9]]
    assert venture.all_points[0] == "0,9"
    assert venture.overlap_points == 12


def test_build_diagonal_line():
    # An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    # An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
    row = [[1, 1], [3, 3]]
    line = HydrothermalVenture.build_diagonal_line(row)
    assert line == ["1,1", "2,2", "3,3"]

    row = [[9, 7], [7, 9]]
    line = HydrothermalVenture.build_diagonal_line(row)
    assert line == ["9,7", "8,8", "7,9"]
