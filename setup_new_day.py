import os
import sys
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
        with open(path, "w") as f:
            f.write(data)


path = Path(base_path, "input.txt")
create_file(path)

path = Path(base_path, f"day{day}.py")
data = f"""from aoc.utils import read_file"""
create_file(path, data)

# copy import file?

path = Path(base_path, f"test_day{day}.py")
data = f"""from aoc.utils import read_file
from day{day} import class_name
"""
create_file(path, data)
