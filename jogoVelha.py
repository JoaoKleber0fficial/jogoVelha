# Tabuleiro

tabuleiro1 = ['', '', '']
tabuleiro2 = ['', '', '']
tabuleiro3 = ['', '', '']

tabuleiro = [tabuleiro1, tabuleiro2, tabuleiro3]

while True: 

    jogador1 = str(input("Escolha X ou O: "))

    jogador1 = jogador1.upper()

    jogador2 = ''

    if jogador1 == 'X':
        jogador2 = 'O'

        print(f'Jogador-1 é {jogador1} ou Jogador-2 é {jogador2}')
        break

    elif jogador1 == 'O':
        jogador2 == 'X'
    
        print(f'Jogador-1 é {jogador1} ou Jogador-2 é {jogador2}')
        break

    else:
        print('Coloque X ou O: ')

def tabuleiroExibir():
        print(tabuleiro1)
        print('---|---|---')
        print(tabuleiro2)
        print('---|---|---')
        print(tabuleiro3)

def verificarVitoria():
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != '':
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != '':
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != '':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != '':
        return True

    return False

def gameplay():
    jogadas = 0
    while jogadas < 9:
        if jogadas % 2 == 0:
            jogador_atual = jogador1
        else:
            jogador_atual = jogador2

        jogada = input(f"Jogador {jogador_atual}, escolha a casa (1-9): ")

        # Verifica se a jogada é válida
        while jogada not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            jogada = input("Escolha uma casa válida entre 1 e 9: ")

        mapeamento = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
        }

        linha, coluna = mapeamento[jogada]

        if tabuleiro[linha][coluna] == '':
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
        else:
            print("Essa casa já está ocupada, escolha outra.")
            continue

        # Exibe o tabuleiro
        tabuleiroExibir()

        # Verifica se alguém venceu
        if verificarVitoria():
            print(f"Jogador {jogador_atual} venceu!")
            break
    else:
        print("Empate! O jogo terminou sem vencedor.")
    
gameplay()
    