import pandas as pd
import numpy as np

file = "input.txt"

with open(file) as input_file:
    input = [line.strip() for line in input_file.readlines()]
    # trim leading white space
    # replace two space with one space


def parse_bingo_input(input):
    numbers = input[0].split(",")
    board_numbers = input[1:]
    boards = []
    for i, row in enumerate(board_numbers):
        if row == "":
            data = [
                row.lstrip().replace("  ", " ").split(" ")
                for row in board_numbers[i + 1 : i + 6]
            ]
            df = pd.DataFrame(data)
            boards.append(df)

    return numbers, boards


def play_bingo(numbers, boards, losing=False):
    winning = []
    for number in numbers:
        print("call: ", number)
        for i, board in enumerate(boards):
            if i in winning:
                continue
            find_match(board, number)

            has_bingo = bingo(board)
            if has_bingo and (not losing or len(winning) == len(boards) - 1):
                print
                sum = remaining_board_sum(board)
                return sum * int(number)
            elif has_bingo and losing:
                winning.append(i)


def find_match(df, value):
    result = df.isin([value])
    existing_row = result.any()
    columns = list(existing_row[existing_row == True].index)
    for col in columns:
        rows = list(result[col][result[col] == True].index)

        for row in rows:
            # print(row, col, df.at[row, col])
            df.at[row, col] = np.nan
    return None, None


def bingo(df):
    row_bingo = df[df.isnull().all(1)]
    if not row_bingo.empty:
        # print(row_bingo)
        print("row bingo")
        return True
    column_bingo = df.dropna(how="all", axis=1)
    if len(df.columns) != len(column_bingo.columns):
        print("column bingo")
        # print(column_bingo)
        return True
    diaganol_bingo = "yikes"
    return False


def remaining_board_sum(df):
    df = df.fillna(0)
    for column in df.columns:
        df[column] = df[column].astype(int)

    return df.values.sum()
