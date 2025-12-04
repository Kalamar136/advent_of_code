import os
from aoc_2015.aoc_dec1.constants import DOCUMENT_URL, FLOOR_START_POSITION, INSTRUCTION_MAP
from aoc_2015.aoc_dec1.constants import DOCUMENT_NAME
from utils import COOKIES, download_url_to_file

"""
Program to help Santa navigate a large apartment building p2

1. Load the floor instructions
2. Compute cumulative floor position until arriving to floor -1

"""

def aoc_dec1_p2() -> None:
    if not os.path.exists(DOCUMENT_NAME):
        download_url_to_file(DOCUMENT_URL, DOCUMENT_NAME, COOKIES)

    floor = FLOOR_START_POSITION
    index = 1
    with open(DOCUMENT_NAME, "r") as f:
        while True:
            instruction = f.read(1)
            if not instruction:
                break

            floor += INSTRUCTION_MAP[instruction]
            if floor == -1:
                break

            index += 1

    print(index)
    

if __name__ == "__main__":
    aoc_dec1_p2()