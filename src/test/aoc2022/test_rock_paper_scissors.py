from aoc2022.rock_paper_scissors import rock_paper_scissors

TEST_INPUT_FILE = "year2022_day2_test.txt"


def test_rock_paper_scissors():

    result = rock_paper_scissors(TEST_INPUT_FILE)

    assert result == 15
