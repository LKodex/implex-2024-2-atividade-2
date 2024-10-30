import matplotlib.pyplot as plt

def plot_value_comparison(results):
    n = results['n']
    vDP = results['vDP']
    vGreedy = results['vGreedy']

    plt.figure(figsize=(10, 6))
    plt.plot(n, vDP, label='Programação Dinâmica', marker='o')
    plt.plot(n, vGreedy, label='Greedy', marker='x')
    plt.xlabel('Tamanho da Tora (n)')
    plt.ylabel('Valor Total de Venda')
    plt.title('Comparação: Valor Total de Venda (DP vs Greedy)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_time_comparison(results):
    n = results['n']
    tDP = results['tDP']
    tGreedy = results['tGreedy']

    plt.figure(figsize=(10, 6))
    plt.plot(n, tDP, label='Tempo DP', marker='o')
    plt.plot(n, tGreedy, label='Tempo Greedy', marker='x')
    plt.xlabel('Tamanho da Tora (n)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Comparação: Tempo de Execução (DP vs Greedy)')
    plt.legend()
    plt.grid(True)
    plt.show()

def generate_plots(results):
    plot_value_comparison(results)
    plot_time_comparison(results)
