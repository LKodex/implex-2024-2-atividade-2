def dynamicProgramming(prices, n):
    maxValue = { 0: 0 }
    for logSize in range(1, n + 1):
        maxPrice = 0

        for cutSize in range(1, logSize + 1):
            remainingLogSize = logSize - cutSize
            cutPrice = prices[cutSize] + maxValue[remainingLogSize]
            maxPrice = max(maxPrice, cutPrice)
        maxValue[logSize] = maxPrice
    return maxValue[n]
