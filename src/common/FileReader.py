from pathlib import Path
import os


class FileReader:
    base_path = os.getenv("WORKDIR", "input")

    def __init__(self):
        pass

    @staticmethod
    def read_txt(file):
        file_path = Path(FileReader.base_path, file)

        with open(file_path) as input_file:
            data = [line.strip() for line in input_file.readlines()]

        return data
