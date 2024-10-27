def cutRodGreedy(prices, n):
    total_value = 0
    while n > 0:
        # Encontra o pedaço com a maior densidade (pi/i)
        max_density = 0
        best_cut = 0
        for i in range(1, n + 1):
            density = prices[i - 1] / i
            if density > max_density:
                max_density = density
                best_cut = i
        # Atualiza o valor total e o comprimento restante da tora
        total_value += prices[best_cut - 1]
        n -= best_cut
    return total_value
