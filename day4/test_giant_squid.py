from giant_squid import *
import pandas as pd

file = "testinput.txt"

with open(file) as input_file:
    input = [line.strip() for line in input_file.readlines()]

numbers, boards = parse_bingo_input(input)


def test_input_import():

    assert numbers == [
        "7",
        "4",
        "9",
        "5",
        "11",
        "17",
        "23",
        "2",
        "0",
        "14",
        "21",
        "24",
        "10",
        "16",
        "13",
        "6",
        "15",
        "25",
        "12",
        "22",
        "18",
        "20",
        "8",
        "19",
        "3",
        "26",
        "1",
    ]
    assert type(boards[0]) == pd.DataFrame
    assert boards[0].at[0, 0] == "22"
    assert boards[0].at[3, 4] == "5"


def test_winning_board_final_score():
    winning_board = play_bingo(numbers, boards)
    assert winning_board == 4512


def test_losing_board_final_score():
    losing_board = play_bingo(numbers, boards, losing=True)
    assert losing_board == 1924
