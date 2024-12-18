#!/usr/bin/env python3
import random
import sys

def main():
    try:
        A = int(sys.stdin.read().strip())
        B = random.randint(-10, 10)
        if B == 0:
            raise ZeroDivisionError("B cannot be zero.")
        result = A / B
        print(result)
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"B = {B}, A/B = {result}\n")
    except Exception as e:
        print(e, file=sys.stderr)

if __name__ == "__main__":
    main()
