import hashlib

PUZZLE_INPUT = "ckczppom"

def aoc_dec4(input: str, number_leading_zeroes: int = 5) -> int:
    """
        Help Santa mine AdventCoins (Brute Force)

        1. Loop through positive numbers (1, 2, 3...)
        2. For each append to input and try hashing to see if we get at least <number_leading_zeroes> leading zeroes
    
    """

    trailing_number = 0
    advent_coin_hash = ""

    while advent_coin_hash[:number_leading_zeroes] != '0' * number_leading_zeroes:
        trailing_number += 1
        hash_input = input + str(trailing_number)

        hash_output = hashlib.md5(hash_input.encode())
        advent_coin_hash = hash_output.hexdigest()

    return trailing_number

if __name__ == "__main__":
    print(f"AdventCoin p1: {aoc_dec4(PUZZLE_INPUT)}")
    print(f"AdventCoin p2: {aoc_dec4(PUZZLE_INPUT, 6)}")
