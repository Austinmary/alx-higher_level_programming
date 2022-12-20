#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
    except Exception as n:
        print(f"Exception: {n}", file=sys.stderr)
    else:
        return result
