from common.FileReader import DataReader
from aoc2023.day1_trebuchet import Trebuchet
from aoc2023.day2_cube_conundrum import CubeConundrum
from aoc2023.day3_gear_ratios import GearRatios
from aoc2023.day4_scratchcards import Scratchcards
from aoc2023.day5 import Almanac


reader = DataReader(file_name="202301.txt")
trebuchet = Trebuchet(data=reader.data)
result = trebuchet.calibrate_sum()
print("trebuchet part 1", result)

result = trebuchet.calibrate_sum_after_interpreting_data()
print("trebuchet part 2", result)

reader = DataReader(file_name="202302.txt")
cube = CubeConundrum(reader.data)
result = cube.possible_games(red=12, green=13, blue=14)
print("cube part 1", result)

result = cube.power()
print("cube part 2", result)

reader = DataReader(file_name="202303.txt")
gear = GearRatios(reader.data)
result = gear.get_gear_part_total()
print("gear part 1", result)

result = gear.get_gear_ratios()
print("gear part 2", result)

reader = DataReader(file_name="202304.txt")
scratchcards = Scratchcards(reader.data)
result = scratchcards.get_card_total()
print("scratchcards part 1", result)

result = scratchcards.get_total_scratchcards()
print("scratchcards part 2", result)

reader = DataReader(file_name="202305.txt")
almanac = Almanac(reader.data)
result = almanac.get_closest_location()
print("almanac part 1", result)

almanac = Almanac(reader.data)
result = almanac.get_closest_location_by_seed_pair()
print("almanac part 2", result)
