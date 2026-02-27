#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]  
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for i in range(num_args):
        print(f"{i+1}: {args[i]}")

if __name__ == "__main__":
    main()
