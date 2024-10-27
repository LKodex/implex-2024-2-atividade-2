def cutRodDP(prices, n):
    # Criando a tabela para armazenar os valores máximos de venda
    max_val = [0] * (n + 1)
    
    # Para cada comprimento da tora de 1 até n
    for i in range(1, n + 1):
        max_price = -1
        # Para cada corte possível da tora
        for j in range(1, i + 1):
            # Calcula o valor máximo ao tentar cortar em tamanhos diferentes
            max_price = max(max_price, prices[j - 1] + max_val[i - j])
        max_val[i] = max_price
    
    return max_val[n]
