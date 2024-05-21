import numpy as np
import matplotlib.pyplot as plt
import time
from memory_profiler import memory_usage
from App.Algorithms import *

'''
Código gerado com auxílio do CHATGPT, adaptado até ficar no estado desejado.

Documento de testes de tempo, memória e dos algoritmos de pesquisa e heurísticos.
Imprime três gráficos referentes a essas 3 métricas para cada algoritmo e Mazes de teste.

Para executar, basta compilar este arquivo.
Os resultados deste script estão disponíveis na pasta "Results", assim como prints dos Mazes testados.
'''

def test_algorithms_with_heuristics(algorithms, heuristics, mazes):
    results = {}

    for algorithm in algorithms:
        for heuristic in heuristics:
            results[f'{algorithm.__name__} {heuristic.__name__}'] = {'time': [], 'memory': [], 'operations': []}
            for maze in mazes:
                start_time = time.time()
                memory_usage_before = memory_usage()
                _, operations = algorithm(maze, heuristic)
                end_time = time.time()
                memory_usage_after = memory_usage()
                time_taken = end_time - start_time

                results[f'{algorithm.__name__} {heuristic.__name__}']['time'].append(time_taken)

                results[f'{algorithm.__name__} {heuristic.__name__}']['memory'].append(memory_usage_after[0] - memory_usage_before[0])

                results[f'{algorithm.__name__} {heuristic.__name__}']['operations'].append(operations)

    return results

def test_algorithms(algorithms, mazes):
    results = {}

    for algorithm in algorithms:
        results[algorithm.__name__] = {'time': [], 'memory': [], 'operations': []}
        for maze in mazes:
            start_time = time.time()
            memory_usage_before = memory_usage()
            _, operations = algorithm(maze)
            end_time = time.time()
            memory_usage_after = memory_usage()
            time_taken= end_time - start_time

            results[algorithm.__name__]['time'].append(time_taken)

            results[algorithm.__name__]['memory'].append(memory_usage_after[0] - memory_usage_before[0])

            results[algorithm.__name__]['operations'].append(operations)

    return results

mazes = [Maze(3, 3, []),
        Maze(4, 5, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)]),        
        Maze(5, 8, [(2, 0), (3, 0), (0, 6), (1, 6)]),
        Maze(6, 6, [(0, 4)]),        
        Maze(6, 7, [(0, 0), (0, 1), (0, 2)])
                ]

algorithms = [bfs, dfs]
algorithms_h = [a_star, greedy_search]
heuristics = [h1, h2, lambda state: h1(state) + h2(state)]


results = test_algorithms_with_heuristics(algorithms_h, heuristics, mazes)
results2 = test_algorithms(algorithms, mazes)

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

results = Merge(results, results2)

for algorithm in results:
    plt.plot(results[algorithm]['time'], label=f"{algorithm}")
plt.xlabel('Maze Index')
plt.ylabel('Time taken (seconds)')
plt.xticks(list(range(len(mazes))))
plt.title('Time taken by each algorithm with different heuristics')
plt.legend()
plt.show()

for algorithm in results:
    plt.plot(results[algorithm]['memory'], label=f"{algorithm}")
plt.xlabel('Maze Index')
plt.xticks(list(range(len(mazes))))
plt.ylabel('Memory Usage (MB)')
plt.title('Memory usage by each algorithm with different heuristics')
plt.legend()
plt.show()

for algorithm in results:
    plt.plot(results[algorithm]['operations'], label=f"{algorithm}")
plt.xlabel('Maze Index')
plt.xticks(list(range(len(mazes))))
plt.ylabel('Memory Usage (MB)')
plt.title('Memory usage by each algorithm with different heuristics')
plt.legend()
plt.show()
