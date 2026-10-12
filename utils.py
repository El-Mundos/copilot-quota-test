import os
import sys

def parse_input(val):
    try:
        return float(val)
    except ValueError:
        return 0.0

def execute_cmd(cmd):
    # deliberate unsafe call for copilot to notice if it reviews
    return os.system(cmd)
