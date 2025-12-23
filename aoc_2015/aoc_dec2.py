from pathlib import Path
from functools import reduce
import operator
from utils import COOKIES, download_url_to_file, DOCUMENT_URL, get_input_path

def aoc_dec2_p1(input_path: Path) -> int:
    """
    Program to help the Elves calculate total wrapping paper area

    1. Load the presents dimensions
    2. Compute all sides' area
    3. Find minimum area and add to twice the sum of sides' area

    """

    total_wrapping_area = 0
    with open(input_path, "r") as f:
        for present_specs in f:
            dimensions = list(map(lambda d: int(d), present_specs.split("x")))
            areas = [dimensions[i] * dimensions[(i+1) % 3] for i in range(3)]
            min_area = min(areas)

            wrapping_area = sum(map(lambda a: 2*a, areas)) + min_area
            total_wrapping_area += wrapping_area
    
    return total_wrapping_area    

def aoc_dec2_p2(input_path: Path) -> int:
    """
    Program to help the Elves calculate total ribbon length

    1. Load the presents dimensions
    2. Compute smallest side perimeter (twice sum of smallest dimensions)
    3. Compute volume and add to smallest side perimeter

    """

    total_ribbon_length = 0
    with open(input_path, "r") as f:
        for present_specs in f:
            dimensions = list(map(lambda d: int(d), present_specs.split("x")))
            volume = reduce(operator.mul, dimensions)

            max_dimension = max(dimensions)
            smallest_dimensions = dimensions.copy()
            smallest_dimensions.remove(max_dimension)

            smallest_side_perimeter = 2 * sum(smallest_dimensions)

            ribbon_length = smallest_side_perimeter + volume
            total_ribbon_length += ribbon_length
    
    return total_ribbon_length    

if __name__ == "__main__":
    INPUT_PATH = get_input_path("presents_dimensions", Path(__file__).parent)
    if not INPUT_PATH.exists():
        download_url_to_file(DOCUMENT_URL.format(day=2), INPUT_PATH, COOKIES)

    print(f"Total wrapping paper area: {aoc_dec2_p1(INPUT_PATH)}")
    print(f"Total ribbon length: {aoc_dec2_p2(INPUT_PATH)}")