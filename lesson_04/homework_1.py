import os
import shutil
from pathlib import Path
from typing import Generator

from pympler import asizeof

dir_: Path = Path.cwd()
ROCKYOU_FILENAME: Path = dir_ / "rockyou.txt"

input_pattern: str = input("Input pattern to look for: ")


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline().replace("\n", "")
            if pattern in line.lower():
                yield line
            if line == "       1":
                break


for ln in filter_lines(ROCKYOU_FILENAME, input_pattern):
    with open("new_file_1.txt", "a") as fl:
        fl.write(ln + "\n")

source: Path = dir_ / "new_file_1.txt"
target: Path = dir_ / "new_file.txt"
shutil.copy(source, target)
os.remove(source)

with open("new_file.txt", "r") as fl_1:
    lines = len(fl_1.readlines())
    print("Total Number of lines:", lines)

print("File size:", asizeof.asizeof(target))
