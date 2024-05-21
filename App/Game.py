import pygame
from App.Maze import *
from App.Algorithms import *
import sys

'''
Script para a execução do jogo Unequal Size Lenght Maze.

Código gerado com auxílio do CHATGPT, adaptado até ficar no estado desejado.
'''


'''
Paleta de cores utilizada no jogo.
'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 240, 15)
PINK = (255, 102, 204)
CHINT = (255, 128, 128)
GREEN = (34,139,34)
GRAY = (200, 200, 200)

'''
Criação do menu principal do jogo.

Mostra as opções de dificuldade ou a opção de criar o seu próprio labirinto e retorna a escolha do jogador.
'''
def main_menu():
    BUTTON_X = 170
    BUTTON_Y = [100, 180, 260, 340, 420, 500, 580]
    BUTTON_WIDTH = 500
    BUTTON_HEIGHT = 50
    LEVELS = ["Super Easy", "Easy", "Medium", "Hard", "Expert", "Impossible", "Build Your Own Maze"]

    pygame.init()

    window = pygame.display.set_mode((800, 700))
    window.fill(WHITE)
    pygame.display.set_caption("Maze Game - Main Menu")

    font = pygame.font.SysFont(None, 50)
    text = font.render("Choose a Difficulty Level:", True, BLACK)
    window.blit(text, (200, 50))

    for i, level in enumerate(LEVELS):
        pygame.draw.rect(window, PINK, (BUTTON_X, BUTTON_Y[i], BUTTON_WIDTH, BUTTON_HEIGHT))
        text = font.render(level, True, WHITE)
        window.blit(text, (BUTTON_X + 50, BUTTON_Y[i] + 10))

    pygame.display.update()

    selected_level = None
    while selected_level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, level in enumerate(LEVELS):
                    if BUTTON_X <= mouse_pos[0] <= BUTTON_X + BUTTON_WIDTH and BUTTON_Y[i] <= mouse_pos[1] <= BUTTON_Y[i] + BUTTON_HEIGHT:
                        selected_level = i
                        break

    pygame.quit()
    return selected_level

'''
Função para jogar o labirinto.

Recebe um labirinto e inicia o jogo, permitindo ao jogador mover-se no tabuleiro.
Pode ser jogado com as setas do teclado ou com o rato.

Há opção de pedir uma dica, que mostra o próximo movimento a ser feito para o jogador.

Há opção de pedir a um dos algoritmos para resolver o labirinto, mostrando a solução.
'''

def play(maze):
    BUTTON_X = 750
    BUTTON_Y = [5, 60, 115, 170, 225, 280, 335, 390, 445]
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    functions = [(a_star, h1),(a_star, h2), (a_star, lambda state: h1(state) + h2(state) ),(greedy_search, h1),(greedy_search, h2), (greedy_search, lambda state: h1(state) + h2(state) ), (bfs), (dfs)]

    '''
    Função que retorna a próxima jogada a ser feita, caso seja possível.

    Utiliza o algoritmo A* com a heurística h1 para calcular a próxima jogada (o algoritmo mais eficiente, depois de efetuarmos testes)
    '''
    def get_hint(maze):
        a, _ = a_star(maze, h1)
        l = len(maze.path)
        if a is None:
            return None
        return a.path[l]

    WINDOW_WIDTH = 700
    CELL_SIZE = WINDOW_WIDTH // maze.c
    WINDOW_HEIGHT = max(CELL_SIZE * maze.l, 500)
    WINDOW_WIDTH = 1000

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Unequal Size Lenght Maze")

    '''
    Função que desenha o tabuleiro do jogo.

    Desenha o tabuleiro, as paredes, o caminho percorrido e os botões para pedir dicas e resolver o labirinto.
    '''
    def draw_maze(maze):
        window.fill(WHITE)

        for i in range(maze.l):
            for j in range(maze.c):
                color = WHITE
                if maze.board[i][j] == 2:
                    color = BLACK
                elif maze.board[i][j] == -2:
                    color = BLUE
                elif i == 0 and j == maze.c - 1:
                    color = YELLOW
                pygame.draw.rect(window, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(window, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        

        path = maze.path
        if len(path) > 1:
            for i in range(len(path) - 1):
                start_x = (path[i][1] + 0.5) * CELL_SIZE
                start_y = (path[i][0] + 0.5) * CELL_SIZE
                end_x = (path[i + 1][1] + 0.5) * CELL_SIZE
                end_y = (path[i + 1][0] + 0.5) * CELL_SIZE
                pygame.draw.line(window, RED, (start_x, start_y), (end_x, end_y), 10)



        button_labels = [
            ("Hint (H)", BUTTON_Y[0]),
            ("A* H1 (1)", BUTTON_Y[1]),
            ("A* H2 (2)", BUTTON_Y[2]),
            ("A* H1+H2 (3)", BUTTON_Y[3]),
            ("GREEDY H1 (G)", BUTTON_Y[4]),
            ("GREEDY H2 (K)", BUTTON_Y[5]),
            ("GREEDY H1+H2 (J)", BUTTON_Y[6]),
            ("BFS (B)", BUTTON_Y[7]),
            ("DFS (D)", BUTTON_Y[8])
        ]

        for i, (label, y) in enumerate(button_labels):
            color = PINK
            if y == BUTTON_Y[0]:
                color = YELLOW
            pygame.draw.rect(window, color, (BUTTON_X, y, BUTTON_WIDTH, BUTTON_HEIGHT))
            font = pygame.font.SysFont(None, 30)
            text = font.render(label, True, WHITE)
            window.blit(text, (BUTTON_X + 10, y + 15))

        pygame.display.update()


    draw_maze(maze)
    font1 = pygame.font.SysFont(None, 70)
    
    '''
    Loop principal do jogo.

    Corre enquanto houver jogadas possíveis e o jogador não tenha ganho.
    '''
    running = True
    while running:
        for event in pygame.event.get():
            algorithms = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_b, pygame.K_d, pygame.K_g, pygame.K_j, pygame.K_k]
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                w = False
                if event.key == pygame.K_UP:
                    w = maze.move(['U'])
                    draw_maze(maze)
                elif event.key == pygame.K_DOWN:
                    w = maze.move(['D'])
                    draw_maze(maze)
                elif event.key == pygame.K_LEFT:
                    w = maze.move(['L'])
                    draw_maze(maze)
                elif event.key == pygame.K_RIGHT:
                    w = maze.move(['R'])
                    draw_maze(maze)
                elif event.key == pygame.K_h:
                    hint = get_hint(maze)
                    w = True
                    if hint is None:
                        text = font1.render("Impossible to continue!", True, RED)
                        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        running = False
                        w = True
                        main()
                        break

                    i = len(maze.path) - 1
                    start_x = (maze.path[i][1] + 0.5) * CELL_SIZE
                    start_y = (maze.path[i][0] + 0.5) * CELL_SIZE
                    end_x = (hint[1] + 0.5) * CELL_SIZE
                    end_y = (hint[0] + 0.5) * CELL_SIZE
                    pygame.draw.line(window, CHINT, (start_x, start_y), (end_x, end_y), 10)
                    pygame.display.update()

                if event.key in algorithms:
                    w = True
                    if event.key == pygame.K_1:
                        solution, _ = a_star(maze, h1)
                    if event.key == pygame.K_2:
                        solution, _ = a_star(maze, h2)
                    if event.key == pygame.K_3:
                        solution, _ = a_star(maze, lambda state: h1(state) + h2(state))
                    if event.key == pygame.K_b:
                        solution, _ = bfs(maze)
                    if event.key == pygame.K_d:
                        solution, _ = dfs(maze)
                    if event.key == pygame.K_g:
                        solution, _ = greedy_search(maze, h1)
                    if event.key == pygame.K_j:
                        solution, _ = greedy_search(maze, lambda state: h1(state) + h2(state))
                    if event.key == pygame.K_k:
                        solution, _ = greedy_search(maze, h2)
                    
                    if solution is None:
                        text = font1.render("Impossible to continue!", True, RED)
                        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        running = False
                        main()
                        break
                    else:
                        l = len(maze.path)-1
                        path = solution.path
                        if len(path) > 1:
                            for i in range(l, len(path) - 1):
                                start_x = (path[i][1] + 0.5) * CELL_SIZE
                                start_y = (path[i][0] + 0.5) * CELL_SIZE
                                end_x = (path[i + 1][1] + 0.5) * CELL_SIZE
                                end_y = (path[i + 1][0] + 0.5) * CELL_SIZE
                                pygame.draw.line(window, RED, (start_x, start_y), (end_x, end_y), 10)
                                pygame.time.wait(500)
                                pygame.display.update()
                        
                        text = font1.render("Win!", True, RED)
                        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        running = False
                        main()



                if maze.available_moves() == [] and not maze.win():
                    font = pygame.font.SysFont(None, 50)
                    text = font1.render('Impossible to continue!', True, RED)
                    window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    running = False
                    main()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // CELL_SIZE
                cell_y = mouse_pos[1] // CELL_SIZE
                x, y = maze.pos
                w = False
                if cell_x == y and cell_y == x - 1:
                    w = maze.move(['U'])
                    draw_maze(maze)
                elif cell_x == y and cell_y == x + 1:
                    w = maze.move(['D'])
                    draw_maze(maze)
                elif cell_y == x and cell_x == y - 1:
                    w = maze.move(['L'])
                    draw_maze(maze)
                elif cell_y == x and cell_x == y + 1:
                    w = maze.move(['R'])
                    draw_maze(maze)

                elif BUTTON_X <= mouse_pos[0] <= BUTTON_X + BUTTON_WIDTH:
                    click = False
                    solution = None

                    if BUTTON_Y[0] <= mouse_pos[1] <= BUTTON_Y[0] + BUTTON_HEIGHT:
                        hint = get_hint(maze)
                        if hint is None:
                            text = font1.render("Impossible to continue!", True, BLACK)
                            window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            running = False
                            w = True
                            main()
                            break

                        else:
                            w = True
                            i = len(maze.path) - 1
                            start_x = (maze.path[i][1] + 0.5) * CELL_SIZE
                            start_y = (maze.path[i][0] + 0.5) * CELL_SIZE
                            end_x = (hint[1] + 0.5) * CELL_SIZE
                            end_y = (hint[0] + 0.5) * CELL_SIZE
                            pygame.draw.line(window, CHINT, (start_x, start_y), (end_x, end_y), 10)
                            pygame.display.update()

                    for i in range(1, len(BUTTON_Y)):
                        h = BUTTON_Y[i]
                        w = True
                        if h <= mouse_pos[1] <= h + BUTTON_HEIGHT:
                            alg = functions[i-1]
                            click = True
                            if alg == dfs or alg == bfs:
                                solution, _ = alg(maze)
                            else:
                                solution, _ = alg[0](maze, alg[1])

                    if solution is None and click:
                        text = font1.render("Impossible to continue!", True, BLACK)
                        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        running = False
                        main()
                        break

                    elif click:
                        l = len(maze.path)-1
                        path = solution.path
                        w = True
                        if len(path) > 1:
                            for i in range(l, len(path) - 1):
                                start_x = (path[i][1] + 0.5) * CELL_SIZE
                                start_y = (path[i][0] + 0.5) * CELL_SIZE
                                end_x = (path[i + 1][1] + 0.5) * CELL_SIZE
                                end_y = (path[i + 1][0] + 0.5) * CELL_SIZE
                                pygame.draw.line(window, RED, (start_x, start_y), (end_x, end_y), 10)
                                pygame.time.wait(500)
                                pygame.display.update()

                        text = font1.render("Win!", True, BLACK)
                        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        running = False
                        main()

                if maze.available_moves() == [] and not maze.win():
                    text = font1.render('Impossible to continue!', True, RED)
                    window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                    pygame.display.update()
                    pygame.time.wait(2000)
                    running = False
                    main()

                if w == False and not maze.win():
                    text = font1.render('Invalid Play!', True, RED)
                    window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                    pygame.display.update()

            if maze.win():
                text = font1.render("You Won!", True, RED)
                window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                pygame.display.update()
                pygame.time.wait(2000)
                running = False
                main()

            elif maze.available_moves() == [] and not maze.win():
                text = font1.render("Impossible to continue!", True, RED)
                window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                pygame.display.update()
                pygame.time.wait(2000)
                running = False
                main()

    pygame.quit()


'''
Função para construir o seu próprio labirinto.

Depois de receber as dimensões do labirinto, o jogador pode escolher onde colocar as paredes.
Retorna o labirinto construído.
'''
def build_own_maze():
    a = 1

    rows, cols = input_integers()
    WINDOW_WIDTH = 700
    CELL_SIZE = WINDOW_WIDTH // cols
    WINDOW_HEIGHT = max(CELL_SIZE * rows, 500)
    WINDOW_WIDTH = 1000

    BUTTON_X = 750
    BUTTON_Y = 115
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50

    walls = []
    board = [[0]*cols for _ in range(rows)]

    pygame.init()

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Build your own Maze!")

    def draw_board():
        window.fill(WHITE)

        for i in range(rows):
            for j in range(cols):
                color = WHITE
                if board[i][j] == 2:
                    color = BLACK
                elif board[i][j] == -2:
                    color = BLUE
                elif i == 0 and j == cols - 1:
                    color = YELLOW
                elif j == 0 and i == rows - 1:
                    color = BLUE
                pygame.draw.rect(window, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(window, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        pygame.draw.rect(window, GREEN, (BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT))
        font = pygame.font.SysFont(None, 30)
        text = font.render("Done", True, WHITE)
        window.blit(text, (BUTTON_X + 60, BUTTON_Y + 15))

        additional_text = font.render("Click to build a wall", True, BLACK)
        text_rect = additional_text.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT + 30))
        additional_text1 = font.render("Press Enter or Done", True, BLACK)
        text_rect1 = additional_text1.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT + 50))
        additional_text2 = font.render("when finished", True, BLACK)
        text_rect2 = additional_text1.get_rect(center=(BUTTON_X + BUTTON_WIDTH // 2, BUTTON_Y + BUTTON_HEIGHT + 70))
        window.blit(additional_text, text_rect)
        window.blit(additional_text1, text_rect1)
        window.blit(additional_text2, text_rect2)
        
        pygame.display.update()

    draw_board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[1] // CELL_SIZE
                y = mouse_pos[0] // CELL_SIZE
                if x < len(board) and y < len(board[0]) and not (x== 0 and y == len(board[0])-1) and not (x==len(board)-1 and y == 0):
                    if board[x][y] == 0:
                        pygame.draw.rect(window, BLACK, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        board[x][y] = 2 
                        walls.append((x, y))
                        pygame.display.update()
                    elif board[x][y] == 2:
                        pygame.draw.rect(window, WHITE, (y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        board[x][y] = 0  
                        walls.remove((x, y))
                        pygame.display.update()

                elif BUTTON_X <= mouse_pos[0] <= BUTTON_X + BUTTON_WIDTH and BUTTON_Y <= mouse_pos[1] <= BUTTON_Y + BUTTON_HEIGHT:
                    running = False

            elif event.type == pygame.QUIT:
                running = False
                a = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False
            draw_board()


    return Maze(rows, cols, walls) if a != 0 else None



'''
Função para receber as dimensões do labirinto.

Mostra um ecrã onde o jogador pode inserir as dimensões do labirinto e pressionar Enter para confirmar.
Retorna as dimensões inseridas.
'''
def input_integers():
    pygame.init()

    window_width = 700
    window_height = 300
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Enter Maze Size")

    font = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 30)

    text = ''
    instructions = "Enter maze size (rows cols), then press Enter:"
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        num_cols, num_rows = map(int, text.split())
                        return num_cols, num_rows
                    except ValueError:
                        text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        window.fill(WHITE)
        
        instructions_surface = small_font.render(instructions, True, BLACK)
        input_surface = font.render(text, True, BLACK)
        window.blit(instructions_surface, (10, 10))
        window.blit(input_surface, (10, 60))
        
        pygame.draw.rect(window, GRAY, (5, 100, window_width - 10, 80), 2)
        
        pygame.display.flip()


'''
Depois de receber as dimensões do labirinto e as posições das paredes, o jogo é iniciado.
'''
def play_custom_maze():
    custom_maze = build_own_maze()
    play(custom_maze)

'''
Função principal do jogo.

Mostra o menu principal e inicia o jogo com a dificuldade escolhida.
Se a dificuldade escolhida for 6, o jogador pode construir o seu próprio labirinto.
'''
def main():
    selected_level = main_menu()
    if selected_level is not None:
        if selected_level == 6:
            play_custom_maze()
        else:
            mazes = [
                Maze(3, 3, []),
                Maze(5, 8, [(2, 0), (3, 0), (0, 6), (1, 6)]),
                Maze(6, 6, [(0, 4)]),
                Maze(6, 6, [(0, 0), (0, 1), (0, 2)]),
                Maze(7, 7, [(1, 1), (1, 2), (3, 3), (4, 1)]),
                Maze(4, 5, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3)])
            ]
            play(mazes[selected_level])

if __name__ == "__main__":
    main()