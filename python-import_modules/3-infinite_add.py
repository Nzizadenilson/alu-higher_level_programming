#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]
    numbers = [int(arg) for arg in args]
    total = sum(numbers)
    print(total)

if __name__ == "__main__":
    main()
