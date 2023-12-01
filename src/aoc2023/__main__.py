from common.FileReader import DataReader
from aoc2023.day1_trebuchet import Trebuchet


PUZZLE_INPUT_FILE = "202301"
reader = DataReader(file_name="202301")
trebuchet = Trebuchet(data=reader.data)
result = trebuchet.calibrate_sum()
print("trebuchet part 1", result)

result = trebuchet.calibrate_sum_after_interpreting_data()
print("trebuchet part 2", result)
