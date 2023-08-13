import re

import RULES

VERSION = "1.0.0"

def perform_shallow_analysis(script):
    lines = script.split("\n")
    errors = []
    for i, line in enumerate(lines):
        ok = False
        for rule in RULES.COMMANDS:
            if re.match(rule, line):
                ok = True
                break
        if not ok:
            errors.append(i)
    return errors

class result():
    def __init__(self, status, data) -> None:
        self.status = status
        self.data = data
def perform_analysis(script:str):
    varspace = [0]*65536
    imgVars = []
    pointers = []
    lines = script.split("\n")
    for i, line in enumerate(lines):
        lines[i] = line.split(" ")
    errors = perform_shallow_analysis(script)
    if errors:
        print("FATAL: Cannot perform deep analysis, because syntax is incorrect")
        return result("ERROR", errors)
    warnings = []
    init_blocks = []
    tick_blocks = []
    for i, line in enumerate(lines):
        if line[0] == "@":
            if line[1] == "on_init":
                init_blocks.append(i)
            if line[1] == "on_tick":
                tick_blocks.append(i)
    for i in range (1, len(init_blocks)):
        warnings.append({
            "line": i,
            "message": "Duplicate init block. "
        })
    
    if warnings:
        print("WARNING possible errors found")
        return result("WARNING",warnings)
    return result("OK", [])
