from functools import reduce
import operator
import os
from aoc_2015.aoc_dec2.constants import DOCUMENT_URL
from aoc_2015.aoc_dec2.constants import DOCUMENT_NAME
from utils import COOKIES, download_url_to_file

"""
Program to help the Elves calculate total ribbon length p1

1. Load the presents dimensions
2. Compute smallest side perimeter (twice sum of smallest dimensions)
3. Compute volume and add to smallest side perimeter

"""

def aoc_dec2_p1() -> None:
    if not os.path.exists(DOCUMENT_NAME):
        download_url_to_file(DOCUMENT_URL, DOCUMENT_NAME, COOKIES)

    total_ribbon_length = 0
    with open(DOCUMENT_NAME, "r") as f:
        for present_specs in f:
            dimensions = list(map(lambda d: int(d), present_specs.split("x")))
            volume = reduce(operator.mul, dimensions)

            max_dimension = max(dimensions)
            smallest_dimensions = dimensions.copy()
            smallest_dimensions.remove(max_dimension)

            smallest_side_perimeter = 2 * sum(smallest_dimensions)

            ribbon_length = smallest_side_perimeter + volume
            total_ribbon_length += ribbon_length
    
    print(total_ribbon_length)    

if __name__ == "__main__":
    aoc_dec2_p1()