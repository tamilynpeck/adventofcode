from common.FileReader import InMemoryFileReader

file_name = "test.txt"

file_data = """A Y
B X
C Z"""


def test_memory_reader():
    file_reader = InMemoryFileReader()
    file_reader.setup(file_name, file_data)

    result = file_reader.read_txt(file_name)

    assert result == ["A Y", "B X", "C Z"]
