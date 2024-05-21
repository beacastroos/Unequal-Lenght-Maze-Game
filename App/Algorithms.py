import heapq
from App.Maze import *

'''
Implementação do algoritmo de pesquisa em largura (BFS).
'''

def bfs(problem):
    queue = [problem]
    visited = set() # estados visitados para evitar loops
    operations = 0

    while queue:
        current = queue.pop(0).copy() # retirar o primeiro elemento da fila e fazer uma cópia
        operations += 1

        visited.add(current) # adicionar o estado atual ao conjunto de estados visitados

        if current.win(): # verificar se a solução foi encontrada
            return current, operations

        for dir in current.available_moves(): # gerar os novos estados a partir do estado atual
            child_state = current.copy() # criar uma cópia do estado atual
            child_state.move(dir) # aplicar o movimento
            if child_state not in visited:
                queue.append(child_state) # adicionar o novo estado à fila

    return None, operations

'''
Implementação do algoritmo de pesquisa em profundidade (DFS).
'''

def dfs(problem):
    stack = [problem]
    visited = set() # estados visitados para evitar loops

    operations = 0

    while stack:
        current = stack.pop().copy() # retirar o último elemento da fila e fazer uma cópia
        operations += 1

        visited.add(current) # adicionar o estado atual ao conjunto de estados visitados

        if current.win(): # verificar se a solução foi encontrada
            return current, operations

        for move in reversed(current.available_moves()): # gerar os novos estados a partir do estado atual e inverter a sua ordem
            child_state = current.copy() # criar uma cópia do estado atual
            child_state.move(move) # aplicar o movimento
            if child_state not in visited:
                stack.append(child_state) # adicionar o novo estado à fila

    return None, operations

'''
Implementação das heirísticas para os algoritmos de pesquisa informada.
'''

def h1(state):
    """Heurística que retorna a distância de Manhattan da posição atual à posição final."""
    cur_x, cur_y = state.pos
    return abs(cur_x - 0) + abs(cur_y - state.l - 1)

def h2(state):
    """ Heurística que retorna o número de quadrados brancos por visitar. """
    n = 0
    for i in range(state.l):
        line = ''.join(str(state.board[i])) # converter a linha do tabuleiro numa string
        n += line.count('0')
    return n

'''
Implementação do algoritmo heuríctico de pesquisa gulosa (Greedy Search).
'''
def greedy_search(maze, heuristic):
    # Definir o método __lt__ para comparar os estados com base na respetiva heurística
    setattr(Maze, "__lt__", lambda self, other: heuristic(self) < heuristic(other))

    states = [maze]
    visited = set()  # estados visitados para evitar loops
    operations = 0

    while states:
        current = heapq.heappop(states)  # estado atual com menor custo com base na heurística
        operations += 1

        visited.add(current)

        if current.win():  # verificar se a solução foi encontrada
            return current, operations

        for move in current.available_moves(): # gerar os novos estados a partir do estado atual
            child = current.copy()  # criar uma cópia do estado atual
            child.move_(move) # aplicar o movimento
            if child not in visited:
                heapq.heappush(states, child) # adicionar os novos estados

    return None, operations

'''
Implementação do algoritmo heurístico A*.
'''
def a_star(maze, heuristic):
    ''' O custo do caminho percorrido é representado pela variável segments, que conta o número de segmentos do caminho'''
    return greedy_search(maze, lambda state: heuristic(state) + state.segments) # adicionar o custo do caminho percorrido à heurística