from pathlib import Path
from collections import Counter
import string
from utils import COOKIES, download_url_to_file, DOCUMENT_URL, get_input_path

VOWELS = {"a", "e", "i", "o", "u"}
FORBIDDEN_SUBS = {"ab", "cd", "pq", "xy"}
DOUBLE_LETTERED_SUBS = {lowercase_letter * 2 for lowercase_letter in string.ascii_lowercase}

def aoc_dec5_p1(input_path: Path) -> int:
    """
        Help Santa figure out the nice strings p1

        1. Load the strings
        2. Figure out the string's composition with Counter to detect vowels
        3. Use set logic to figure out if there are at least 3 distinct vowels
        4. Parse the string in groups of 2 (starting at index 0 and 1)
        5. Iterate through the substrings with length 2 to see if there are double letters or forbidden strings
    
    """

    number_nice_strings = 0
    with open(input_path, "r") as f:
        for string in f:
            counter = Counter(string)

            vowels_freqs = [count for vowel, count in counter.items() if vowel in VOWELS]
            number_of_vowels = sum(vowels_freqs)
            if number_of_vowels < 3:
                continue

            # Finding all substrings of length 2
            substrings_2 = {string[i:i+2] for i in range(0, len(string) - 1, 2)}
            substrings_2 |= {string[i:i+2] for i in range(1, len(string) - 1, 2)}

            forbidden_subs_contained = FORBIDDEN_SUBS & substrings_2
            double_lettered_subs_contained = DOUBLE_LETTERED_SUBS & substrings_2
            if double_lettered_subs_contained and not forbidden_subs_contained:
                number_nice_strings += 1

    return number_nice_strings


def aoc_dec5_p2(input_path: Path) -> int:
    """
    Help Santa figure out the nice strings p2

    1. Load the strings
    2. Iterate through every letter
    3. Condition letter_sandwich_contained: Figure out if the substring starting at the iterating letter is a "double letter sandwich" (XYX where X and Y are any letters)
    4. Condition two_letter_pair: Figure out if the substring starting at the iterating letter is a two letter substring that is repeated later in the string
    5. If both conditions are satisfied, increment number_nice_strings counter

    """

    number_nice_strings = 0
    with open(input_path, "r") as f:
        for string in f:
            letter_sandwich_contained = False
            two_letter_pair_present = False
            for i in range(len(string) - 2):
                if not letter_sandwich_contained:
                    letter_sandwich_contained = string[i] == string[i+2]
                
                if not two_letter_pair_present:
                    two_letter = string[i:i+2]
                    two_letter_pair_present = two_letter in string[i+2:]

                if letter_sandwich_contained and two_letter_pair_present:
                    number_nice_strings += 1
                    break
                
    return number_nice_strings

if __name__ == "__main__":
    INPUT_PATH = get_input_path("nice_naughty_strings", Path(__file__).parent)
    if not INPUT_PATH.exists():
        download_url_to_file(DOCUMENT_URL.format(day=5), INPUT_PATH, COOKIES)

    print(f"Number of nice strings p1: {aoc_dec5_p1(INPUT_PATH)}")
    print(f"Number of nice strings p2: {aoc_dec5_p2(INPUT_PATH)}")
