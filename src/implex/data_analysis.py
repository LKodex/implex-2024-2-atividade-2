import matplotlib.pyplot as plt
import time

def plot_value_comparison(results, filePrefix=""):
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
    plt.savefig(f"{filePrefix}-value_comparison.png")

def plot_time_comparison(results, filePrefix=""):
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
    plt.savefig(f"{filePrefix}-time_comparison.png")

def generate_plots(results):
    now = "-".join(map(str, time.localtime()[:6]))
    plot_value_comparison(results, now)
    plot_time_comparison(results, now)
