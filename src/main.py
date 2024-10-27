#!/usr/bin/env python3

# José Vitor Oda Pires (2020.1906.049-0)
# Lucas Gonçalves Cordeiro (2021.1906.031-0)

from sys import argv, exit, stderr
import random
import time
from implex import greedy, dp

def generatePrices(fim, seed):
    random.seed(seed)
    return sorted(random.randint(1, fim + 1) for _ in range(fim))

def main(inc, fim, stp, seed):
    data = {}
    priceTable = generatePrices(fim, seed)
    for n in range(inc, fim + 1, stp):
        dpData = timeTheAlgo(greedy.cutRodGreedy, "DP", priceTable, n)
        greedyData = timeTheAlgo(dp.cutRodDP, "Greedy", priceTable, n)
        greedyAccuracy = greedyData["vGreedy"] / dpData["vDP"]
        greedyAccuracyRounded = round(greedyAccuracy * 100, 2)
        data[n] = { "%": greedyAccuracyRounded }
        data[n] |= dpData | greedyData
    print(data)

def timeTheAlgo(algorithm, label: str, *args) -> dict:
    start = time.time()
    data = algorithm(args[0], args[1])
    end = time.time()

    timeSpent = end - start

    return {
        f"v{label}": data,
        f"t{label}": timeSpent,
    }

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
