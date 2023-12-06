import os
import sys
import shutil
from datetime import date
from pathlib import Path

print(sys.argv)

year = date.today().year
day = date.today().day + 1

if len(sys.argv) > 2:
    year = sys.argv[1]
    day = sys.argv[2]

base_path = Path(os.getcwd(), f"src/{year}/{day}")
base_path.mkdir(exist_ok=True, parents=True)


def create_file(path, data=""):
    if not path.exists():
        print(f"Creating file: {path}")
        with open(path, "w") as f:
            f.write(data)


input_path = Path(base_path, "input.txt")
create_file(input_path)

program_path = Path(base_path, "program.py")
program_data = f"""from utils import read_file
from day{day} import Day{day}

data = read_file("input.txt")

program = Day{day}(data)
result = program.solve_part_one()
print("part 1", result)

result = program.solve_part_two()
print("part 2", result)"""
create_file(program_path, program_data)


day_path = Path(base_path, f"day{day}.py")
data = f"""class Day{day}:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        pass

    def solve_part_two(self):
        pass"""
create_file(day_path, data)


test_path = Path(base_path, f"test_day{day}.py")
test_data = f"""import pytest
from utils import read_txt
from day{day} import Day{day}

test_data = ""

def test_day{day}():
    data = read_txt(test_data)
    program = Day{day}(data)

    result = program.solve_part_one()

    assert result == 0

@pytest.mark.parametrize(
    "line,expected",
    [
        ("line", "expected"),
    ],
)
def test_program_function(line, expected):
    data = read_txt(line)
    program = Day{day}(data)

    result = program.test()

    assert result == expected
"""
create_file(test_path, test_data)

util_path = Path(base_path, f"utils.py")
shutil.copyfile("src/common/utils.py", util_path)
