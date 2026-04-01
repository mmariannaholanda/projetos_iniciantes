# jogo damas projeto

tabuleiro = [
    ['.', 'p', '.', 'p', '.', 'p', '.', 'p'],
    ['p', '.', 'p', '.', 'p', '.', 'p', '.'],
    ['.', 'p', '.', 'p', '.', 'p', '.', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
    ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
    ['b', '.', 'b', '.', 'b', '.', 'b', '.']
]


def mostrar_tabuleiro(tabuleiro):
    print('\nTabuleiro atual:')
    print('  0 1 2 3 4 5 6 7')
    for i, linha in enumerate(tabuleiro):
        print(f'{i} ' + ' '.join(linha))


def dentro_do_tabuleiro(linha, coluna):
    return 0 <= linha < 8 and 0 <= coluna < 8


def contar_pecas(tabuleiro):
    cont_b = 0
    cont_p = 0

    for linha in tabuleiro:
        for casa in linha:
            if casa == 'b' or casa == 'B':
                cont_b += 1
            elif casa == 'p' or casa == 'P':
                cont_p += 1

    return cont_b, cont_p


def existe_captura_para_b(tabuleiro):
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 'b':
                if dentro_do_tabuleiro(i - 2, j + 2):
                    if tabuleiro[i - 1][j + 1] == 'p' and tabuleiro[i - 2][j + 2] == '.':
                        return True

                if dentro_do_tabuleiro(i - 2, j - 2):
                    if tabuleiro[i - 1][j - 1] == 'p' and tabuleiro[i - 2][j - 2] == '.':
                        return True

    return False


def existe_captura_para_p(tabuleiro):
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 'p':
                if dentro_do_tabuleiro(i + 2, j + 2):
                    if tabuleiro[i + 1][j + 1] == 'b' and tabuleiro[i + 2][j + 2] == '.':
                        return True

                if dentro_do_tabuleiro(i + 2, j - 2):
                    if tabuleiro[i + 1][j - 1] == 'b' and tabuleiro[i + 2][j - 2] == '.':
                        return True

    return False


def damaB(tabuleiro):
    for j in range(8):
        if tabuleiro[0][j] == 'b':
            tabuleiro[0][j] = 'B'


def damaP(tabuleiro):
    for j in range(8):
        if tabuleiro[7][j] == 'p':
            tabuleiro[7][j] = 'P'


def existe_captura_para_B(tabuleiro):
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 'B':

                if dentro_do_tabuleiro(i - 2, j + 2):
                    if (tabuleiro[i - 1][j + 1] == 'p' or tabuleiro[i - 1][j + 1] == 'P') and tabuleiro[i - 2][j + 2] == '.':
                        return True

                if dentro_do_tabuleiro(i - 2, j - 2):
                    if (tabuleiro[i - 1][j - 1] == 'p' or tabuleiro[i - 1][j - 1] == 'P') and tabuleiro[i - 2][j - 2] == '.':
                        return True

                if dentro_do_tabuleiro(i + 2, j + 2):
                    if (tabuleiro[i + 1][j + 1] == 'p' or tabuleiro[i + 1][j + 1] == 'P') and tabuleiro[i + 2][j + 2] == '.':
                        return True

                if dentro_do_tabuleiro(i + 2, j - 2):
                    if (tabuleiro[i + 1][j - 1] == 'p' or tabuleiro[i + 1][j - 1] == 'P') and tabuleiro[i + 2][j - 2] == '.':
                        return True
    return False


def existe_captura_para_P(tabuleiro):
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] == 'P':

                if dentro_do_tabuleiro(i - 2, j + 2):
                    if (tabuleiro[i - 1][j + 1] == 'b' or tabuleiro[i - 1][j + 1] == 'B') and tabuleiro[i - 2][j + 2] == '.':
                        return True

                if dentro_do_tabuleiro(i - 2, j - 2):
                    if (tabuleiro[i - 1][j - 1] == 'b' or tabuleiro[i - 1][j - 1] == 'B') and tabuleiro[i - 2][j - 2] == '.':
                        return True

                if dentro_do_tabuleiro(i + 2, j + 2):
                    if (tabuleiro[i + 1][j + 1] == 'b' or tabuleiro[i + 1][j + 1] == 'B') and tabuleiro[i + 2][j + 2] == '.':
                        return True

                if dentro_do_tabuleiro(i + 2, j - 2):
                    if (tabuleiro[i + 1][j - 1] == 'b' or tabuleiro[i + 1][j - 1] == 'B') and tabuleiro[i + 2][j - 2] == '.':
                        return True
    return False


def movimento_diagonal(linha_origem, coluna_origem, linha_destino, coluna_destino):
    if abs(linha_destino - linha_origem) == abs(coluna_destino - coluna_origem):
        return True
    else:
        return False


def comer_inimigos_dama(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino, peca):
    if peca == 'B':
        inimigos = ['p', 'P']
    else:
        inimigos = ['b', 'B']

    passo_linha = 1 if linha_destino > linha_origem else -1
    passo_coluna = 1 if coluna_destino > coluna_origem else -1

    i = linha_origem + passo_linha
    j = coluna_origem + passo_coluna

    while i != linha_destino and j != coluna_destino:
        if tabuleiro[i][j] in inimigos:
            tabuleiro[i][j] = '.'

        i += passo_linha
        j += passo_coluna


# jogadores
jogador1 = input('Qual o nome do primeiro jogador? ').strip()
jogador2 = input('Qual o nome do segundo jogador? ').strip()

# regras
mostrarRegras = input('Você sabe as regras do jogo (s/n)? ').strip().lower()

if mostrarRegras == 's':
    print('Ok, vamos começar!')
else:
    print('Regras básicas:')
    print('- b anda para cima')
    print('- p anda para baixo')
    print('- B e P são damas')
    print('- se puder capturar, é obrigatório capturar')
    print('- ganha quem eliminar todas as peças do adversário')


# quem começa
import random
jogadores = [jogador1, jogador2]

def decisao():
    while True:
        escolha = input('Como você quer decidir quem começa?\n1 = Sorteio\n2 = Eu escolho\n').strip()

        if escolha == '1':
            numero = random.randint(0, 1)
            print(f'O jogador sorteado foi {jogadores[numero]}... Boa sorte!')
            return jogadores[numero]

        elif escolha == '2':
            while True:
                turno_atual = input(f'Quem começa? {jogador1} ou {jogador2}? ').strip()

                if turno_atual == jogador1 or turno_atual == jogador2:
                    return turno_atual
                else:
                    print('Digite um nome válido.')

        else:
            print('Escolha inválida. Digite 1 ou 2.')


turno_atual = decisao()

print(f'{jogador1} usa b e {jogador2} usa p.')

# jogo
while True:
    print('\n-------------------')
    print(f'Agora é a vez de: {turno_atual}')
    mostrar_tabuleiro(tabuleiro)

    jogada_valida = False

    if turno_atual == jogador1:
        print(f'Vez de {jogador1}')

        captura_obrigatoria = existe_captura_para_b(tabuleiro)
        captura_obrigatoria_dama = existe_captura_para_B(tabuleiro)

        if captura_obrigatoria:
            print('Você tem uma captura obrigatória!')
        elif captura_obrigatoria_dama:
            print('Você tem uma captura obrigatória com a dama!')

        # escolher origem
        while True:
            linha_origem = int(input('Linha da peça: '))
            coluna_origem = int(input('Coluna da peça: '))

            if not dentro_do_tabuleiro(linha_origem, coluna_origem):
                print('Essa posição não existe. Tente de novo.')
                continue

            if tabuleiro[linha_origem][coluna_origem] == 'b' or tabuleiro[linha_origem][coluna_origem] == 'B':
                break
            else:
                print('Essa peça não é sua, tente de novo.')

        # peça normal branca
        if tabuleiro[linha_origem][coluna_origem] == 'b':
            while True:
                linha_destino = int(input('Linha destino: '))
                coluna_destino = int(input('Coluna destino: '))

                if not dentro_do_tabuleiro(linha_destino, coluna_destino):
                    print('Essa posição não existe. Tente de novo.')
                    continue

                if tabuleiro[linha_destino][coluna_destino] != '.':
                    print('Destino ocupado! Tente de novo.')
                    continue

                dif_linha = linha_destino - linha_origem
                dif_coluna = coluna_destino - coluna_origem

                if dif_linha >= 0:
                    print('Você não pode ir para trás! Digite outro destino...')
                    continue

                if captura_obrigatoria and abs(dif_linha) != 2:
                    print('Você é obrigado a capturar!')
                    continue

                if dif_linha == -1 and abs(dif_coluna) == 1:
                    tabuleiro[linha_destino][coluna_destino] = 'b'
                    tabuleiro[linha_origem][coluna_origem] = '.'
                    jogada_valida = True
                    break

                elif dif_linha == -2 and abs(dif_coluna) == 2:
                    linha_meio = (linha_origem + linha_destino) // 2
                    coluna_meio = (coluna_origem + coluna_destino) // 2

                    if tabuleiro[linha_meio][coluna_meio] == 'p':
                        tabuleiro[linha_destino][coluna_destino] = 'b'
                        tabuleiro[linha_origem][coluna_origem] = '.'
                        tabuleiro[linha_meio][coluna_meio] = '.'
                        jogada_valida = True
                        break
                    else:
                        print('Não existe peça inimiga para capturar no meio. Tente de novo.')

                else:
                    print('Movimento inválido! Tente de novo.')

        # dama branca
        elif tabuleiro[linha_origem][coluna_origem] == 'B':
            while True:
                linha_destino = int(input('Linha destino: '))
                coluna_destino = int(input('Coluna destino: '))

                if not dentro_do_tabuleiro(linha_destino, coluna_destino):
                    print('Essa posição não existe. Tente de novo.')
                    continue

                if tabuleiro[linha_destino][coluna_destino] != '.':
                    print('Destino ocupado! Tente de novo.')
                    continue

                if not movimento_diagonal(linha_origem, coluna_origem, linha_destino, coluna_destino):
                    print('Movimento inválido, ande em diagonal!!')
                    continue

                if captura_obrigatoria_dama:
                    if abs(linha_destino - linha_origem) == 2 and abs(coluna_destino - coluna_origem) == 2:
                        linha_meio = (linha_origem + linha_destino) // 2
                        coluna_meio = (coluna_origem + coluna_destino) // 2

                        if tabuleiro[linha_meio][coluna_meio] == 'p' or tabuleiro[linha_meio][coluna_meio] == 'P':
                            tabuleiro[linha_destino][coluna_destino] = 'B'
                            tabuleiro[linha_origem][coluna_origem] = '.'
                            tabuleiro[linha_meio][coluna_meio] = '.'
                            jogada_valida = True
                            break
                        else:
                            print('Não existe peça inimiga para capturar no meio.')
                            continue
                    else:
                        print('Você era obrigado a capturar com a dama!')
                        continue
                else:
                    tabuleiro[linha_destino][coluna_destino] = 'B'
                    tabuleiro[linha_origem][coluna_origem] = '.'
                    comer_inimigos_dama(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino, 'B')
                    jogada_valida = True
                    break

    else:
        print(f'Vez de {jogador2}')

        captura_obrigatoria = existe_captura_para_p(tabuleiro)
        captura_obrigatoria_dama = existe_captura_para_P(tabuleiro)

        if captura_obrigatoria:
            print('Você tem uma captura obrigatória!')
        elif captura_obrigatoria_dama:
            print('Você tem uma captura obrigatória com a dama!')

        # escolher origem
        while True:
            linha_origem = int(input('Linha da peça: '))
            coluna_origem = int(input('Coluna da peça: '))

            if not dentro_do_tabuleiro(linha_origem, coluna_origem):
                print('Essa posição não existe. Tente de novo.')
                continue

            if tabuleiro[linha_origem][coluna_origem] == 'p' or tabuleiro[linha_origem][coluna_origem] == 'P':
                break
            else:
                print('Essa peça não é sua, tente de novo.')

        # peça normal preta
        if tabuleiro[linha_origem][coluna_origem] == 'p':
            while True:
                linha_destino = int(input('Linha destino: '))
                coluna_destino = int(input('Coluna destino: '))

                if not dentro_do_tabuleiro(linha_destino, coluna_destino):
                    print('Essa posição não existe. Tente de novo.')
                    continue

                if tabuleiro[linha_destino][coluna_destino] != '.':
                    print('Destino ocupado! Tente de novo.')
                    continue

                dif_linha = linha_destino - linha_origem
                dif_coluna = coluna_destino - coluna_origem

                if dif_linha <= 0:
                    print('Você não pode ir para trás! Digite outro destino...')
                    continue

                if captura_obrigatoria and abs(dif_linha) != 2:
                    print('Você é obrigado a capturar!')
                    continue

                if dif_linha == 1 and abs(dif_coluna) == 1:
                    tabuleiro[linha_destino][coluna_destino] = 'p'
                    tabuleiro[linha_origem][coluna_origem] = '.'
                    jogada_valida = True
                    break

                elif dif_linha == 2 and abs(dif_coluna) == 2:
                    linha_meio = (linha_origem + linha_destino) // 2
                    coluna_meio = (coluna_origem + coluna_destino) // 2

                    if tabuleiro[linha_meio][coluna_meio] == 'b':
                        tabuleiro[linha_destino][coluna_destino] = 'p'
                        tabuleiro[linha_origem][coluna_origem] = '.'
                        tabuleiro[linha_meio][coluna_meio] = '.'
                        jogada_valida = True
                        break
                    else:
                        print('Não existe peça inimiga para capturar no meio. Tente de novo.')

                else:
                    print('Movimento inválido! Tente de novo.')

        # dama preta
        elif tabuleiro[linha_origem][coluna_origem] == 'P':
            while True:
                linha_destino = int(input('Linha destino: '))
                coluna_destino = int(input('Coluna destino: '))

                if not dentro_do_tabuleiro(linha_destino, coluna_destino):
                    print('Essa posição não existe. Tente de novo.')
                    continue

                if tabuleiro[linha_destino][coluna_destino] != '.':
                    print('Destino ocupado! Tente de novo.')
                    continue

                if not movimento_diagonal(linha_origem, coluna_origem, linha_destino, coluna_destino):
                    print('Movimento inválido, ande em diagonal!!')
                    continue

                if captura_obrigatoria_dama:
                    if abs(linha_destino - linha_origem) == 2 and abs(coluna_destino - coluna_origem) == 2:
                        linha_meio = (linha_origem + linha_destino) // 2
                        coluna_meio = (coluna_origem + coluna_destino) // 2

                        if tabuleiro[linha_meio][coluna_meio] == 'b' or tabuleiro[linha_meio][coluna_meio] == 'B':
                            tabuleiro[linha_destino][coluna_destino] = 'P'
                            tabuleiro[linha_origem][coluna_origem] = '.'
                            tabuleiro[linha_meio][coluna_meio] = '.'
                            jogada_valida = True
                            break
                        else:
                            print('Não existe peça inimiga para capturar no meio.')
                            continue
                    else:
                        print('Você era obrigado a capturar com a dama!')
                        continue
                else:
                    tabuleiro[linha_destino][coluna_destino] = 'P'
                    tabuleiro[linha_origem][coluna_origem] = '.'
                    comer_inimigos_dama(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino, 'P')
                    jogada_valida = True
                    break

    # promoção para dama
    damaB(tabuleiro)
    damaP(tabuleiro)

    # contar peças
    cont_b, cont_p = contar_pecas(tabuleiro)

    # verificar vitória
    if cont_p == 0:
        mostrar_tabuleiro(tabuleiro)
        print(f'\n{jogador1} ganhou!! Jogo encerrado.')
        break
    elif cont_b == 0:
        mostrar_tabuleiro(tabuleiro)
        print(f'\n{jogador2} ganhou!! Jogo encerrado.')
        break

    # troca de turno
    if jogada_valida:
        if turno_atual == jogador1:
            turno_atual = jogador2
        else:
            turno_atual = jogador1
