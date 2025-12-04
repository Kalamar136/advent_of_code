import os
from aoc_2015.aoc_dec2.constants import DOCUMENT_URL
from aoc_2015.aoc_dec2.constants import DOCUMENT_NAME
from utils import COOKIES, download_url_to_file

"""
Program to help the Elves calculate total wrapping paper area p1

1. Load the presents dimensions
2. Compute all sides' area
3. Find minimum area and add to twice the sum of sides' area

"""

def aoc_dec2_p1() -> None:
    if not os.path.exists(DOCUMENT_NAME):
        download_url_to_file(DOCUMENT_URL, DOCUMENT_NAME, COOKIES)

    total_wrapping_area = 0
    with open(DOCUMENT_NAME, "r") as f:
        for present_specs in f:
            dimensions = list(map(lambda d: int(d), present_specs.split("x")))
            areas = [dimensions[i] * dimensions[(i+1) % 3] for i in range(3)]
            min_area = min(areas)

            wrapping_area = sum(map(lambda a: 2*a, areas)) + min_area
            total_wrapping_area += wrapping_area
    
    print(total_wrapping_area)    

if __name__ == "__main__":
    aoc_dec2_p1()