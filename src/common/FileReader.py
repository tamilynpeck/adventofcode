from pathlib import Path
import os


class FileReader:
    def __init__(self, base_path=os.getenv("WORKDIR", "input")):
        self.base_path = base_path

    def read_txt(self, file):
        file_path = Path(self.base_path, file)

        with open(file_path) as input_file:
            data = input_file.read()
            return data.splitlines()


class InMemoryFileReader:
    def __init__(self):
        self.files = {}

    def read_txt(self, file):
        if str(file) not in self.files:
            return None

        return self.files[file].splitlines()

    def setup(self, file, data):
        self.files[file] = data


class DataReader:
    def __init__(self, file_name, file_reader=FileReader()):
        self.file_reader = file_reader
        self.file_name = file_name
        self.data = self.file_reader.read_txt(self.file_name)


class MemoryDataReader:
    def __init__(self, data):
        self.file_reader = InMemoryFileReader()
        self.file_name = "memory"
        self.file_reader.setup(self.file_name, data)
        self.data = self.file_reader.read_txt(self.file_name)
