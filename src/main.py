#!/usr/bin/env python3

# José Vitor Oda Pires (2020.1906.049-0)
# Lucas Gonçalves Cordeiro (2021.1906.031-0)

from sys import argv, exit, stderr
from random import randrange, seed

def main(inc, fim, stp, seed):
    pass

if __name__ == "__main__":
    if len(argv) < 4:
        programName = argv[0]
        errorMessage = f"Usage: {programName} <inc> <fim> <stp> [seed]"
        print(errorMessage, file=stderr)
        exit(1)
    try:
        inc = int(argv[1])
        fim = int(argv[2])
        stp = int(argv[3])
    except ValueError as e:
        errorMessage = f"Could not convert parameters to an integer.\nException: {e}"
        print(errorMessage, file=stderr)
        exit(1)
    seed = argv[4] if len(argv) > 4 else "randomSeed"
    main(inc, fim, stp, seed)
