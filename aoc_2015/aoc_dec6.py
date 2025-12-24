from pathlib import Path
from typing import List, Tuple
import numpy as np
from utils import COOKIES, download_url_to_file, DOCUMENT_URL, get_input_path

INSTRUCTIONS_MAP_P1 = {"turn on": True, "turn off": False}
INSTRUCTIONS_MAP_P2 = {"turn on": 1, "turn off": -1, "toggle": 2}
GRID_DIMS = 1000

def instruction_parser(instruction: str) -> Tuple[str, Tuple[int], Tuple[int]]:
    instruction_components = instruction.strip().split()
    v1 = tuple(int(x) for x in instruction_components[-3].split(","))
    v2 = tuple(int(x) for x in instruction_components[-1].split(","))
    instruction_action = " ".join(instruction_components[:-3])

    return instruction_action, v1, v2

def aoc_dec6_p1(input_path: Path) -> int:
    """
        Figure out the best holiday lighting configration p1

        1. Load the instructions
        2. Execute the rectangle subset instruction with numpy vectorized operations
    
    """

    # Initialize holiday lighting grid
    lighting_grid = np.zeros((GRID_DIMS, GRID_DIMS), dtype=bool)

    with open(input_path, "r") as f:
        for instruction in f:
            # Parsing the instruction
            instruction_action, v1, v2 = instruction_parser(instruction)

            lighting_rectangle = lighting_grid[v1[0]:v2[0]+1, v1[1]:v2[1]+1]
            if instruction_action in INSTRUCTIONS_MAP_P1.keys():
                lighting_rectangle[:] = INSTRUCTIONS_MAP_P1[instruction_action]
            else:
                lighting_rectangle[:] ^= True   # Toggling lights

    return lighting_grid.sum()


def aoc_dec6_p2(input_path: Path) -> int:
    """
        Figure out the best holiday lighting configration p2

        1. Load the instructions
        2. Execute the rectangle subset instruction with numpy vectorized operations
    
    """

    # Initialize holiday lighting grid
    lighting_grid = np.zeros((GRID_DIMS, GRID_DIMS), dtype=int)

    with open(input_path, "r") as f:
        for instruction in f:
            # Parsing the instruction
            instruction_action, v1, v2 = instruction_parser(instruction)

            lighting_rectangle = lighting_grid[v1[0]:v2[0]+1, v1[1]:v2[1]+1]
            lighting_rectangle[:] += INSTRUCTIONS_MAP_P2[instruction_action]
            lighting_rectangle[:] = lighting_rectangle.clip(min=0)

    return lighting_grid.sum()

if __name__ == "__main__":
    INPUT_PATH = get_input_path("lighting_instructions", Path(__file__).parent)
    if not INPUT_PATH.exists():
        download_url_to_file(DOCUMENT_URL.format(day=6), INPUT_PATH, COOKIES)

    print(f"Number of lights on p1: {aoc_dec6_p1(INPUT_PATH)}")
    print(f"Number of lights on p2: {aoc_dec6_p2(INPUT_PATH)}")
