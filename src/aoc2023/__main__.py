from common.FileReader import DataReader
from aoc2023.day1_trebuchet import Trebuchet
from aoc2023.day2_cube_conundrum import CubeConundrum


reader = DataReader(file_name="202301")
trebuchet = Trebuchet(data=reader.data)
result = trebuchet.calibrate_sum()
print("trebuchet part 1", result)

result = trebuchet.calibrate_sum_after_interpreting_data()
print("trebuchet part 2", result)

reader = DataReader(file_name="202302")
cube = CubeConundrum(reader.data)
result = cube.possible_games(red=12, green=13, blue=14)
print("cube part 1", result)

result = cube.power()
print("cube part 2", result)