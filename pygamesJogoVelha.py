import pygame
import sys

# Inicializar o pygame
pygame.init()

# Configurações básicas
WIDTH, HEIGHT = 300, 300  # Tamanho da tela
LINE_WIDTH = 5  # Espessura das linhas
BOARD_ROWS, BOARD_COLS = 3, 3
CIRCLE_RADIUS = 25
CIRCLE_WIDTH = 5
CROSS_WIDTH = 5
SPACE = 30

# Cores
BG_COLOR = (255, 255, 255)
LINE_COLOR = (100, 100, 155)
CIRCLE_COLOR = (139, 131, 100)
CROSS_COLOR = (66, 66, 66)
WIN_LINE_COLOR = (255, 0, 0)

# Criar janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')
screen.fill(BG_COLOR)

# Tabuleiro
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Função para desenhar as linhas do tabuleiro
def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * HEIGHT // BOARD_ROWS), (WIDTH, i * HEIGHT // BOARD_ROWS), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH // BOARD_COLS, 0), (i * WIDTH // BOARD_COLS, HEIGHT), LINE_WIDTH)

draw_lines()

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * WIDTH / BOARD_COLS + WIDTH / BOARD_COLS / 2),
                                                          int(row * HEIGHT / BOARD_ROWS + HEIGHT / BOARD_ROWS / 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * WIDTH / BOARD_COLS + SPACE, row * HEIGHT / BOARD_ROWS + SPACE),
                                 ((col + 1) * WIDTH / BOARD_COLS - SPACE, (row + 1) * HEIGHT / BOARD_ROWS - SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 ((col + 1) * WIDTH / BOARD_COLS - SPACE, row * HEIGHT / BOARD_ROWS + SPACE),
                                 (col * WIDTH / BOARD_COLS + SPACE, (row + 1) * HEIGHT / BOARD_ROWS - SPACE),
                                 CROSS_WIDTH)

def draw_win_line(start_pos, end_pos):
    pygame.draw.line(screen, WIN_LINE_COLOR, start_pos, end_pos, LINE_WIDTH * 2)

# Variáveis de controle
player = 'X'
game_over = False
win_pos = None

# Função para verificar vitória
def check_win():
    global game_over, win_pos
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            game_over = True
            win_pos = ((0, row * HEIGHT // BOARD_ROWS + HEIGHT // 6), (WIDTH, row * HEIGHT // BOARD_ROWS + HEIGHT // 6))
            return board[row][0]
    
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            game_over = True
            win_pos = ((col * WIDTH // BOARD_COLS + WIDTH // 6, 0), (col * WIDTH // BOARD_COLS + WIDTH // 6, HEIGHT))
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        game_over = True
        win_pos = ((0, 0), (WIDTH, HEIGHT))
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        game_over = True
        win_pos = ((WIDTH, 0), (0, HEIGHT))
        return board[0][2]
    
    return None

# Função para reiniciar o jogo
def restart_game():
    global board, player, game_over, win_pos
    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
    player = 'X'
    game_over = False
    win_pos = None
    screen.fill(BG_COLOR)
    draw_lines()

# Loop principal
temp = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // (HEIGHT // BOARD_ROWS)
            col = x // (WIDTH // BOARD_COLS)
            if board[row][col] is None:
                board[row][col] = player
                player = 'O' if player == 'X' else 'X'
                winner = check_win()
                if winner:
                    print(f'O jogador {winner} venceu!')
                    temp += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
    
    draw_figures()
    if win_pos:
        draw_win_line(win_pos[0], win_pos[1])
    pygame.display.update()
