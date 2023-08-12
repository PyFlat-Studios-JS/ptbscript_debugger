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