from rock_paper_scissors import rock_paper_scissors


def test_rock_paper_scissors():
    file = "test_input.txt"

    result = rock_paper_scissors(file)

    assert result == 15


def test_part_one_input():
    file = "input.txt"

    result = rock_paper_scissors(file)

    assert result == 13675

def test_part_one_input_b():
    file = "input_b.txt"

    result = rock_paper_scissors(file)

    assert result == 14069

def test_rock_paper_scissors_part_two():
    file = "test_input.txt"

    result = rock_paper_scissors(file, default_calc=False)

    assert result == 12
