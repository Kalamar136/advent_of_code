
from collections import Counter
from pathlib import Path
from utils import COOKIES, DOCUMENT_URL, download_url_to_file, get_file_content, get_input_path

FLOOR_START_POSITION = 0
INSTRUCTION_MAP = {"(": 1, ")": -1}

def aoc_dec1_p1(input_path: Path) -> int:
    """
    Program to help Santa navigate a large apartment building p1

    1. Load the floor instructions
    2. Count sum of up "(" instructions as 1 and down ")" instructions as -1

    """

    instructions = get_file_content(input_path)
    instructions_counter = Counter(instructions)
    
    floor = sum([INSTRUCTION_MAP[instruction] * instructions_counter[instruction] for instruction in "()"])
    
    return floor

def aoc_dec1_p2(input_path: Path) -> None:
    """
    Program to help Santa navigate a large apartment building p2

    1. Load the floor instructions
    2. Compute cumulative floor position until arriving to floor -1

    """
    floor = FLOOR_START_POSITION
    index = 1
    with open(input_path, "r") as f:
        while True:
            instruction = f.read(1)
            if not instruction:
                break

            floor += INSTRUCTION_MAP[instruction]
            if floor == -1:
                break

            index += 1

    return index

if __name__ == "__main__":
    INPUT_PATH = get_input_path("floor_instructions", Path(__file__).parent)
    if not INPUT_PATH.exists():
        download_url_to_file(DOCUMENT_URL.format(day=1), INPUT_PATH, COOKIES)

    print(f"Last floor: {aoc_dec1_p1(INPUT_PATH)}")
    print(f"Instruction at floor -1: {aoc_dec1_p2(INPUT_PATH)}")