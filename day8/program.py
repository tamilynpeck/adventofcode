from SevenSegmentSearch import SevenSegmentSearch

file = "input.txt"


input = SevenSegmentSearch.parse_input(file)
search = SevenSegmentSearch(input=input)

unique_count = search.count_unique_output_values()
print(unique_count)
