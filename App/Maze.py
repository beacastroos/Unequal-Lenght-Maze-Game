import numpy as np
import copy


class Maze:
    '''
    Inicializa o labirinto.
-
    Para inicializar o labirinto deveremos introduzir as dimensões (número de
    linhas e de colunas) e uma lista de tuplos das posições das paredes.

    O labirinto (board) é inicializado com 0's nos quadrados brancos, 2's para
    paredes, 1's para os quadrados brancos visitados e -2 para o início.
    O histórico de movimentos é registado em moves, as paredes em walls,
    as dimenções em l (linhas) e c (colunas), as posições visitadas em path e a
    posição atual em pos. A última direção tomada, guardada em last_d, assim
    como o comprimento do caminho atual e do caminho anterior, cur_lenght e
    last_lenght respetivamente, são guardadas para assegurar que as regras são
    cumpridas.
    '''
    def __init__(self, l, c, walls):
        self.l = l; self.c = c

        self.board = np.zeros((l, c))
        self.board[l-1][0] = -2
        self.walls = walls
        for wall in walls:
            a, b = wall
            self.board[a][b] = 2

        self.moves = []
        self.pos = (l-1, 0)
        self.path = [(l-1,0)]
        self.segments = 0

        self.last_d = ''
        self.cur_lenght = 0
        self.last_lenght = 0


    '''
    Função que retorna os movimentos possíveis.

    Requisitos para um movimento ser possível:
        - O bloco escolhido estar dentro dos limites do tabuleiro;
        - O bloco escolhido ainda não ter sido visitado.
    '''
    def available_moves(self):
        n = []
        d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R':(0, 1)}
        x, y = self.pos[0], self.pos[1]
        di = self.last_d

        # Se o tamanho do caminho atual for igual ao tamanho do caminho anterior, só resta uma direção possível (a que estamos a seguir agora).
        if self.cur_lenght == self.last_lenght and di != '':
            if -1 < x+d[di][0] < self.l and -1 < y+d[di][1] < self.c and self.board[x+d[di][0]][y+d[di][1]] == 0:
                return [self.last_d,]
            return []

        if x == 0 and y == self.c - 1: # Se estiver na última posição.
            return []

        for m in d: # Para cada movimento no dicionário, verifica se cumpre os requisitos.
            if -1 < x+d[m][0] < self.l and -1 < y+d[m][1] < self.c and self.board[x+d[m][0]][y+d[m][1]] == 0:
                n.append(m)
        return n


    '''
    Função move que faz um ou mais movimentos no tabuleiro.
    Função move_ auxiliar da função move.

    Impede movimentos inválidos e pára se não tiver movimentos possíveis.
    '''
    def move(self, dirs):
        for dir in dirs:
            if dir not in self.available_moves():
                return False
            if self.available_moves() == []:
                return False
            self.move_(dir)
        return True

    def move_(self, dir): # Auxiliar do move
        d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R':(0, 1)}

        x, y = self.pos[0] + d[dir][0], self.pos[1] + d[dir][1] # Guarda a posição nova
        self.board[x][y] = 1 # Atualiza o board
        self.pos = (x, y)

        self.moves.append(dir)
        self.path.append(self.pos)

        # Atualiza a direção e o comprimento do caminho atual e anterior
        if dir == self.last_d:
            self.cur_lenght += 1
        else:
            self.last_lenght = self.cur_lenght
            self.cur_lenght = 1
            self.last_d = dir
            self.segments += 1


    '''
    Função que verifica se o jogo está ganho.

    Vê se já chegamos ao final e se já percorremos todos os quadrados brancos.
    Retorna True se acontecer, False se não acontecer.
    '''
    def win(self):
        x, y = self.pos
        is_full = (len(self.path)+len(self.walls) == self.l*self.c)
        is_end = (x == 0 and y == self.c-1)
        return is_full and is_end


    '''
    Definição de critério de comparação de labirintos.
    '''
    def __eq__(self, other):
        return np.array_equal(self.moves, other.moves)


    '''
    Definição da hash de labirintos.
    '''
    def __hash__(self):
        return hash(str(self.board))


    '''
    Definição da cópia do labirinto.
    '''
    def copy(self):
        return copy.deepcopy(self)




