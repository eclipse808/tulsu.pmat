#!/usr/bin/env python3
import sys
import math

def main():
    try:
        C = float(sys.stdin.read().strip())
        if C < 0:
            raise ValueError("Cannot take square root of a negative number.")
        result = math.sqrt(C)
        with open('output.txt', 'w') as output_file:
            output_file.write(str(result))
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"C = {C}, sqrt(C) = {result}\n")
    except Exception as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()
