
from collections import Counter
import os
from aoc_2015.aoc_dec1.constants import DOCUMENT_URL, INSTRUCTION_MAP
from aoc_2015.aoc_dec1.constants import DOCUMENT_NAME
from utils import COOKIES, download_url_to_file, get_file_content

"""
Program to help Santa navigate a large apartment building p1

1. Load the floor instructions
2. Count sum of up "(" instructions as 1 and down ")" instructions as -1

"""

def aoc_dec1_p1() -> None:
    if not os.path.exists(DOCUMENT_NAME):
        download_url_to_file(DOCUMENT_URL, DOCUMENT_NAME, COOKIES)

    instructions = get_file_content(DOCUMENT_NAME)
    instructions_counter = Counter(instructions)
    
    floor = sum([INSTRUCTION_MAP[instruction] * instructions_counter[instruction] for instruction in "()"])
    
    print(floor)
    

if __name__ == "__main__":
    aoc_dec1_p1()