def greedy(prices, n):
    totalValue = 0
    logSize = n

    while logSize > 0:
        maxDensity = 0
        bestCut = 0
        for i in range(1, logSize + 1):
            density = prices[i] / i
            if density > maxDensity:
                maxDensity = density
                bestCut = i
        totalValue += prices[bestCut]
        logSize -= bestCut
    return totalValue