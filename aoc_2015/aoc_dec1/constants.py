import os


DOCUMENT_NAME= f"{os.path.dirname(os.path.abspath(__file__))}/floor_instructions.txt"
DOCUMENT_URL= "https://adventofcode.com/2015/day/1/input"
FLOOR_START_POSITION = 0
INSTRUCTION_MAP = {"(": 1, ")": -1}