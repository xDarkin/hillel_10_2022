from pathlib import Path
from typing import Generator

LESSON_4_DIR = Path(__file__).parent
ROCKYOU_FILENAME = LESSON_4_DIR / "rockyou.txt"


def filter_lines(filename: Path, pattern: str) -> Generator:
    with open(filename, encoding="utf-8") as file:
        while True:
            line = file.readline().replace("\n", "")

            if not line:
                break

            if pattern in line.lower():
                yield line


for john in filter_lines(ROCKYOU_FILENAME, "john"):
    print(john)
