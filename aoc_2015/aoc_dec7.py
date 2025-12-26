from functools import partial
import inspect
from pathlib import Path
from typing import Any, Callable, Dict, List, Tuple
import operator
from utils import COOKIES, download_url_to_file, DOCUMENT_URL, get_input_path

MASK_16BIT = 0xFFFF
INSTRUCTION_MAP = {
    "ASSIGNMENT": lambda x: x,
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": lambda n, x: operator.lshift(x, n) & MASK_16BIT,
    "RSHIFT": lambda n, x: operator.rshift(x, n),
    "NOT": lambda x: operator.invert(x) & MASK_16BIT
}

def no_inputs_left_gate(gate_operation: Callable):
    return not list(inspect.signature(gate_operation).parameters)

def parse_value(value: str):
    return int(value) if value.isdigit() else value

def propagate_wire_signals(signals: list[str], wires_resolve: Dict[str, Any], wires_dependencies: Dict[str, List[str]]):
    newly_resolved = signals
    while wires := newly_resolved:
        newly_resolved = []
        for wire in wires:
            dependencies = wires_dependencies.get(wire, [])
            for d in dependencies:
                updated_operation = partial(wires_resolve[d], wires_resolve[wire])
                if not no_inputs_left_gate(updated_operation):
                    wires_resolve[d] = updated_operation
                else:
                    wires_resolve[d] = updated_operation()
                    newly_resolved.append(d)


def instruction_parser(instruction: str) -> Tuple[str, str, Tuple[str|int, ...]]:
    instruction_components = instruction.strip().split()
    w = instruction_components.pop()

    if len(instruction_components) == 2:
        instruction_action = "ASSIGNMENT"
        inputs = (parse_value(instruction_components[0]), )
    elif len(instruction_components) == 3:
        instruction_action = instruction_components.pop(0)  # NOT instruction
        inputs = (parse_value(instruction_components.pop(0)), )
    else:
        instruction_action = instruction_components.pop(1)  # AND, OR, SHIFT instructions
        i1, i2 = instruction_components[:2]
        inputs = (parse_value(i2), parse_value(i1))

    return  w, instruction_action, inputs

def aoc_dec7_p1(input_path: Path) -> int:
    """
        Help little Bobby assemble the circuit p1

        1. Load the wire and gate instructions
        2. Initialize a dict to keep track of wires results (wires_resolve), and a dict to keep track of dependencies (wires_dependencies)
        3. For each instruction, parse its content (resolve whether it is a gate definition or wire assignment)
        4. For a gate definition, check to see if the wire inputs are already in the dict (in which case load them in the gate)
            4.1. Wire inputs that are not already in wires_resolve are added to wires_dependencies along with a dependency list to specify their dependent gates
        5. For wire assignments, add them to wires_resolve and check their dependencies in wires_dependencies if applicable to resolve them
        6. Return the value for a in wires_resolve
    
    """

    wires_resolve = {}
    wires_dependencies = {}
    with open(input_path, "r") as f:
        for wire_instruction in f:
            # Parsing the instruction
            w, instruction_action, inputs = instruction_parser(wire_instruction)
            operation = INSTRUCTION_MAP[instruction_action]

            for i in inputs:
                i_resolved = wires_resolve.get(i, None) if not isinstance(i, int) else i
                
                if isinstance(i_resolved, int):
                    operation = partial(operation, i_resolved)
                else:
                    wires_dependencies[i] = wires_dependencies.get(i, []) + [w]
            
            if not no_inputs_left_gate(operation):
                wires_resolve[w] = operation
            else:
                wires_resolve[w] = operation()

                newly_resolved = [w]
                propagate_wire_signals(newly_resolved, wires_resolve, wires_dependencies)
    
    return wires_resolve["a"]


def aoc_dec7_p2(input_path: Path) -> int:
    """
        Help little Bobby assemble the circuit p2

        1. Load the wire and gate instructions
        2. Initialize a dict to keep track of wires results (wires_resolve), and a dict to keep track of dependencies (wires_dependencies)
        3. For each instruction, parse its content (resolve whether it is a gate definition or wire assignment)
        4. For a gate definition, update the value of the wire to the gate operation in wires_resolve
        5. For wire assignments, add them to wires_resolve
        6. After building the wires_resolve and wires_dependencies dicts, find all wires assignments in wires_resolve (all keys that have an int value) and propagate their signals
        7. Update the value of 'b' in wires_resolve to be equal to 'a'
        8. Propagate a second time the wires values like in 6.
    
    """


    wires_resolve = {}
    wires_dependencies = {}
    with open(input_path, "r") as f:
        for wire_instruction in f:
            # Parsing the instruction
            w, instruction_action, inputs = instruction_parser(wire_instruction)
            operation = INSTRUCTION_MAP[instruction_action]

            for i in inputs:
                if isinstance(i, int):
                    operation = partial(operation, i)
                else:
                    wires_dependencies[i] = wires_dependencies.get(i, []) + [w]
            
            if not no_inputs_left_gate(operation):
                wires_resolve[w] = operation
            else:
                wires_resolve[w] = operation()
    
    wires_resolved = [wire for wire, value in wires_resolve.items() if isinstance(value, int)]
    wires_resolve_final = wires_resolve.copy()
    propagate_wire_signals(wires_resolved, wires_resolve, wires_dependencies)

    wires_resolve_final['b'] = wires_resolve['a']
    propagate_wire_signals(wires_resolved, wires_resolve_final, wires_dependencies)
    
    return wires_resolve_final["a"]

if __name__ == "__main__":
    INPUT_PATH = get_input_path("wires_gate_assembling", Path(__file__).parent)
    if not INPUT_PATH.exists():
        download_url_to_file(DOCUMENT_URL.format(day=7), INPUT_PATH, COOKIES)

    print(f"Wire 'a' signal p1: {aoc_dec7_p1(INPUT_PATH)}")
    print(f"Wire 'a' signal p1: {aoc_dec7_p2(INPUT_PATH)}")
