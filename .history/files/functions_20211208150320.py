import random
import messages
import images
import formatting
from os import system, name  # importa informações sobre o sistema operacional em uso


def limpa_tela():  # Limpa a tela removendo do prompt as informações sobre a localização dos arquivos
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def escolhe_palavras(lista):

    # Função Random e método choice - escolhe algo específico, no caso a lista
    palavra = random.choice(lista)
    while '-' in palavra or ' ' in palavra:  # cria um laço que, inicialmente sem palavras em lista dá início
        palavra = random.choice(palavra)

    # o retorno "retorna" a palavra escolhida aleatório mas toda em MAIÚSCULA
    return palavra.upper()


indice_tema = []  # lista vazia para armazenar a escolha do tema, no caso o índice dele
indice_nivel = []
tema = []
dica = ' '
palavra_secreta = ' '
saida = ' '
lista_jogadores = []


def numero_jogadores():  # Função que estabelece a quantidade de jogadores (singleplayer ou multiplayer)

    correto = False  # inicializa o loop while na condição de falso, ou seja, sem ter o dado adequado na variável num_jogadores
    while correto == False:
        num_jogadores = input(
            'Olá! Por gentileza, favor informar a quantidade de jogadores 1, 2 ou 3:  ')
        if num_jogadores == '1':
            id_jogador = input('Por favor, informe seu primeiro nome: ')
            lista_jogadores.append(id_jogador)
            correto = True
            # O retorno é a quantidade de players armazenados na lista_jogadores
            return len(lista_jogadores)

        elif num_jogadores == '2':
            id_jogador_01 = input(
                'Por favor, jogador nº 1, favor informar seu primeiro nome: ')
            lista_jogadores.append(id_jogador_01)
            id_jogador_02 = input(
                'Por favor, jogador nº 2, favor informar seu primeiro nome: ')
            lista_jogadores.append(id_jogador_02)
            correto = True
            return len(lista_jogadores)

        elif num_jogadores == '3':
            id_jogador_01 = input(
                'Por favor, jogador nº 1, favor informar seu primeiro nome: ')
            lista_jogadores.append(id_jogador_01)
            id_jogador_02 = input(
                'Por favor, jogador nº 2, favor informar seu primeiro nome: ')
            lista_jogadores.append(id_jogador_02)
            id_jogador_03 = input(
                'Por favor, jogador nº 3, favor informar seu primeiro nome: ')
            lista_jogadores.append(id_jogador_03)
            correto = True
            return len(lista_jogadores)

        else:
            print('Favor digitar somente 1, 2 ou 3!!!')
            correto = False


def modo_de_jogo():
    if len(lista_jogadores) == 1:
        modo_jogo = 'SINGLE PLAYER'
        jogar()  # Fase com definição das dificuldades

    elif len(lista_jogadores) == 2 or len(lista_jogadores) == 3:
        modo_jogo = 'MULTIPLAYER'
        jogar_2()  # Fase direta com dificuldade única


def escolha_tema():  # Função para selecionar o tema específico, localizado no arquivo messages.py
    formatting.forma_linha()
    opcao_tema = False  # condição inicial que dá start ao loop do comando while

    while opcao_tema == False:  # condição que mantém o loop em funcionamento, logo, o loop cessa quando True

        escolhe_tema = input('''
Escolha abaixo o tema de sua preferência:

[a] Tema Geral
[b] Tema Tech

Digite a ou b: ''')

        if escolhe_tema == 'a' or escolhe_tema == 'A':  # Não usei método lower ou upper por conta da saída
            # se condição acima for atendida, grava '0' na lista indice_tema
            indice_tema.append(0)
            opcao_tema = True  # interrompe o loop
            return indice_tema  # dá a saída da função escolha_tema

        elif escolhe_tema == 'b' or escolhe_tema == 'B':
            indice_tema.append(1)
            opcao_tema = True
            return indice_tema

        else:
            print('Favor digitar somente as letras "a" ou "b"! ')
            opcao_tema = False


def escolha_nivel():  # Seletor do nível de dificuldade: fácil, mediano ou difícil
    opcao_nivel = False

    while opcao_nivel == False:

        escolhe_nivel = input('''
Escolha um dos níveis de dificuldade:

[a] Fácil
[b] Mediano
[c] Difícil

Digite a, b ou c: ''')

        if escolhe_nivel == 'a' or escolha_nivel == 'A':
            indice_nivel.append(0)
            opcao_nivel = True
            return indice_nivel

        elif escolhe_nivel == 'b' or escolhe_nivel == 'B':
            indice_nivel.append(1)
            opcao_nivel = True
            return indice_nivel

        elif escolhe_nivel == 'c' or escolhe_nivel == 'C':
            indice_nivel.append(2)
            opcao_nivel = True
            return indice_nivel

        else:
            print('Favor digitar somente as letras "a", "b" ou "c"! ')
            opcao_nivel = False


def caminho():
    if sum(indice_tema) == 0:
        if sum(indice_nivel) == 0:
            palavra_secreta = escolhe_palavras(messages.categoria_geral[0])
            saida = palavra_secreta
            return saida

        if sum(indice_tema) == 0:
            if sum(indice_nivel) == 1:
                palavra_secreta = escolhe_palavras(messages.categoria_geral[1])
                saida = palavra_secreta
                return saida

        if sum(indice_tema) == 0:
            if sum(indice_nivel) == 2:
                palavra_secreta = escolhe_palavras(messages.categoria_geral[2])
                saida = palavra_secreta
                return saida

    if sum(indice_tema) == 1:
        if sum(indice_nivel) == 0:
            palavra_secreta = escolhe_palavras(messages.categoria_tech[0])
            saida = palavra_secreta
            return saida

        if sum(indice_tema) == 1:
            if sum(indice_nivel) == 1:
                palavra_secreta = escolhe_palavras(messages.categoria_tech[1])
                saida = palavra_secreta
                return saida

        if sum(indice_tema) == 1:
            if sum(indice_nivel) == 2:
                palavra_secreta = escolhe_palavras(messages.categoria_tech[2])
                saida = palavra_secreta
                return saida


def imprime_mensagem_abertura():
    print(images.bem_vindo)
    formatting.forma_linha()


def inicializa_letras_acertadas(palavra_secreta):
    formatting.forma_linha()
    return ["_" for letra in palavra_secreta]


def pede_chute():
    formatting.forma_linha()
    chute = input("Qual seu palpite sobre uma letra? ")
    formatting.forma_linha()
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print(formatting.escolher_cor('green', "Parabéns, você ganhou!"))
    print(images.show_de_bola)
    print(images.vencedor_02)


def imprime_mensagem_perdedor(palavra_secreta):
    print()
    print(formatting.escolher_cor('red', "Puxa, você foi enforcado!"))
    print(formatting.escolher_cor(
        'yellow', "A palavra era {}".format(palavra_secreta)))
    print(images.game_over)


def desenha_forca(erros):

    if(erros == 1):
        print(formatting.escolher_cor('yellow', images.forca[0]))

    if(erros == 2):
        print(formatting.escolher_cor('yellow', images.forca[1]))

    if(erros == 3):
        print(formatting.escolher_cor('yellow', images.forca[2]))

    if(erros == 4):
        print(formatting.escolher_cor('yellow', images.forca[3]))

    if(erros == 5):
        print(formatting.escolher_cor('yellow', images.forca[4]))

    if(erros == 6):
        print(formatting.escolher_cor('yellow', images.forca[5]))

    if (erros == 7):
        print(formatting.escolher_cor('red', images.forca[6]))

    print()


def jogar():

    indice_nivel = []
    indice_tema = []

    limpa_tela()

    escolha_tema()
    # print(indice_tema)
    limpa_tela()
    formatting.forma_linha()
    escolha_nivel()
    # print(indice_nivel)
    limpa_tela()
    palavra_secreta = caminho()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            print()
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print(formatting.escolher_cor('green', "PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(
                    palavra_secreta.upper())))
        else:
            erros += 1
            print(letras_acertadas)
            print(formatting.escolher_cor(
                'yellow', 'Ainda faltam acertar {} letras'.format(letras_faltando)))
            print(formatting.escolher_cor(
                'blue', 'Você ainda tem {} tentativas'.format(7-erros)))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

# if(__name__ == '__main__'):
    # jogar()


def jogar_2():
    limpa_tela()
    print(images.multiplayer)
    formatting.forma_linha()
    main()


def letter_picking(secret, blank_word, num_lives):
    # user guesses a letter here
    guessed_letter = input("Please guess a letter.")
    lives_flag = 0  # set counter to 0 to begin recording number of correct guesses
    # if x is the guessed letter, replace blank space with x
    for i in [i for i, x in enumerate(secret) if x == guessed_letter]:
        lives_flag = 1  # guess is correct, so we add one to the counter
        blank_word[i] = guessed_letter
    # call new function to compute number of lives after completed loop
    num_lives = validate_lives(lives_flag, num_lives)
    print(num_lives)
    return blank_word, num_lives

# This function counts the number of lives needed to calculate the score and end the game


def validate_lives(lives_flag, lives):
    if lives_flag > 0:  # check if counter value > 0, if it is, user guessed correctly
        print("Num lives unchanged", len(lives))
        print(lives)
        return lives
    else:
        # if counter value not >0, then user guessed incorrectly. add "1" to num_lives as counter for lost lives
        lives.append("1")
        print("You lost a life", len(lives))
        print(lives)
        return lives
#


def check_win(lives, blank, player_num, game_status):
    print("check_win", blank)
    count_space = 0
    for i in range(len(blank)):
        if blank[i] == "_":
            pass
        else:
            count_space += 1
    if count_space == len(blank):
        print("You win")
        print("player number: ", player_num)
        game_status = True
        return game_status
    else:
        game_status = False
        return game_status


def multi_player():
    num_lives = []  # array for two player lives for player 1
    num_lives2 = []  # array for two player lives for player 2
    num_lives3 = []


def main():

    word1 = caminho()
    word2 = caminho()
    word3 = caminho()
    blanks1 = list(word1)
    blanks2 = list(word2)
    blanks3 = list(word3)
    num_lives = []  # array for two player lives for player 1
    num_lives2 = []  # array for two player lives for player 2
    num_lives3 = []
    game_over = False
    # print blanks1
    for i in range(len(blanks1)):
        blanks1[i] = "_"
    print("Player 2: You are guessing the following:",
          blanks1)  # falta mudar lógica da mensagem
    # print blanks2
    for i in range(len(blanks2)):
        blanks2[i] = "_"
    print("Player 1: You are guessing the following:", blanks2)
    for i in range(len(blanks3)):
        blanks3[i] = "_"
    print("Player 3: You are guessing the following:", blanks3)
    while len(num_lives) < 6 and len(num_lives2) < 6 and len(num_lives3) < 6 and game_over == False:
        player = 1
        blanks, num_lives = letter_picking(word1, blanks1, num_lives)
        game_over = check_win(num_lives, blanks1, player, game_over)
        player = 2
        blanks, num_lives2 = letter_picking(word2, blanks2, num_lives2)
        game_over = check_win(num_lives2, blanks2, player, game_over)
        player = 3
        blanks, num_lives = letter_picking(word3, blanks3, num_lives3)
        game_over = check_win(num_lives3, blanks3, player, game_over)

    if num_lives > num_lives2 or num_lives > num_lives3:  # Refazer lógica de saída
        print("Player 2 win")
    elif num_lives2 > num_lives or num_lives2 > num_lives3:
        print("Player 1 win")
    elif num_lives3 > num_lives:
        print("Player 1 win")
    elif num_lives3 > num_lives2:
        print("Player 1 win")

    else:
        print("Tie")

    print(blanks1)
    print(blanks2)
    print(blanks3)


limpa_tela()
imprime_mensagem_abertura()
numero_jogadores()
# print(lista_jogadores)
modo_de_jogo()
