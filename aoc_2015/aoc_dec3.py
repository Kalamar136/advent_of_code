from pathlib import Path
from utils import COOKIES, download_url_to_file, DOCUMENT_URL, get_input_path

MOVE_MAP = {"^": (0,1), "v": (0,-1), ">":(1,0), "<":(-1,0)}

def aoc_dec3_p1(input_path: Path) -> int:
    """
        Help Santa visit houses p1

        1. Load the houses directions
        2. Keep track of Santa's coordinates (x,y) starting at (0,0)
        3. At every move, compute Santa's new location
        4. If Santa has been there increment the counter and store the new location in a hashtable
    
    """

    coordinates = (0,0)
    visited_houses = {coordinates}
    with open(input_path, "r") as f:
        while True:
            instruction = f.read(1)
            if not instruction:
                break
            
            move = MOVE_MAP[instruction]
            coordinates = tuple(x + y for x, y in zip(coordinates, move))

            if coordinates not in visited_houses:
                visited_houses.add(coordinates)
    
    return len(visited_houses)


def aoc_dec3_p2(input_path: Path) -> int:
    """
    Program to help Santa visit houses p2

    1. Load the houses directions
    2. Keep track of Santa's and Robo-Santa's coordinates (x,y) starting at (0,0)
    3. At every move, compute Santa's or Robo-Santa's new location
    4. If Santa or Robo-Santa has been there increment the counter and store the new location in a hashtable

    """

    santa_coordinates = (0,0)
    robo_santa_coordinates = (0,0)
    visited_houses = {santa_coordinates}
    santa_turn = True
    with open(input_path, "r") as f:
        while True:
            instruction = f.read(1)
            if not instruction:
                break
            
            move = MOVE_MAP[instruction]
            current_coordinates = santa_coordinates if santa_turn else robo_santa_coordinates

            updated_coordinates = tuple(x + y for x, y in zip(current_coordinates, move))
            if santa_turn:
                santa_coordinates = updated_coordinates
            else:
                robo_santa_coordinates = updated_coordinates

            if updated_coordinates not in visited_houses:
                visited_houses.add(updated_coordinates)
            santa_turn = not santa_turn
    
    return len(visited_houses)

if __name__ == "__main__":
    INPUT_PATH = get_input_path("houses_directions", Path(__file__).parent)
    if not INPUT_PATH.exists():
        download_url_to_file(DOCUMENT_URL.format(day=3), INPUT_PATH, COOKIES)

    print(f"Houses visited part 1: {aoc_dec3_p1(INPUT_PATH)}")
    print(f"Houses visited part 2: {aoc_dec3_p2(INPUT_PATH)}")
