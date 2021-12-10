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
            palavra_secreta = escolhe_palavras(
                messages.categoria_geral[0])
            saida = palavra_secreta
            return saida

        if sum(indice_tema) == 0:
            if sum(indice_nivel) == 1:
                palavra_secreta = escolhe_palavras(
                    messages.categoria_geral[1])
                saida = palavra_secreta
                return saida

        if sum(indice_tema) == 0:
            if sum(indice_nivel) == 2:
                palavra_secreta = escolhe_palavras(
                    messages.categoria_geral[2])
                saida = palavra_secreta
                return saida

    if sum(indice_tema) == 1:
        if sum(indice_nivel) == 0:
            palavra_secreta = escolhe_palavras(
                messages.categoria_tech[0])
            saida = palavra_secreta
            return saida

        if sum(indice_tema) == 1:
            if sum(indice_nivel) == 1:
                palavra_secreta = escolhe_palavras(
                    messages.categoria_tech[1])
                saida = palavra_secreta
                return saida

        if sum(indice_tema) == 1:
            if sum(indice_nivel) == 2:
                palavra_secreta = escolhe_palavras(
                    messages.categoria_tech[2])
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


def seleciona_letras(segredo, palavra_em_branco, numero_de_vidas):  # original seleciona_letras
    # user guesses a letter here
    letra_advinhada = input(
        "Por favor, informe seu palpite, digite somente uma letra: ".lower())
    sinaliza_vidas = 0  # set counter to 0 to begin recording number of correct guesses
    # if x is the guessed letter, replace em_branco space with x
    for i in [i for i, x in enumerate(segredo) if x == letra_advinhada]:
        sinaliza_vidas = 1  # guess is correct, so we add one to the counter
        palavra_em_branco[i] = letra_advinhada
    # call new function to compute number of vidas after completed loop
    numero_de_vidas = valida_vidas(sinaliza_vidas, numero_de_vidas)
    print(numero_de_vidas)
    return palavra_em_branco, numero_de_vidas

# This function counts the number of vidas needed to calculate the score and end the game


def valida_vidas(sinaliza_vidas, vidas):
    if sinaliza_vidas > 0:  # check if counter value > 0, if it is, user guessed correctly
        print("Número de vidas inalterado, vida(s) perdida(s): ", len(vidas))
        # print(vidas)
        return vidas
    else:
        # if counter value not >0, then user guessed incorrectly. add "1" to numero_de_vidas as counter for lost vidas
        vidas.append("1")
        print(f"Oh oh! Você perdeu {len(vidas)} vida(s)...")
        if len(vidas) == 1:
            print(formatting.escolher_cor('yellow', images.forca[0]))
        if len(vidas) == 2:
            print(formatting.escolher_cor('yellow', images.forca[1]))
        if len(vidas) == 3:
            print(formatting.escolher_cor('yellow', images.forca[2]))
        if len(vidas) == 4:
            print(formatting.escolher_cor('yellow', images.forca[3]))
        if len(vidas) == 5:
            print(formatting.escolher_cor('yellow', images.forca[4]))
        if len(vidas) == 6:
            print(formatting.escolher_cor('yellow', images.forca[5]))
        if len(vidas) == 7:
            print(formatting.escolher_cor('yellow', images.forca[6]))

        # print(vidas)
        return vidas
#


def check_win(vidas, em_branco, numero_jogador, game_status):
    print("Checa acertos: ", em_branco)
    contador_espacos = 0
    for i in range(len(em_branco)):
        if em_branco[i] == "_":
            pass
        else:
            contador_espacos += 1
    if contador_espacos == len(em_branco):
        print()
        print("VOCÊ VENCEU!!!")
        print("Número do jogador: ", numero_jogador)
        print(images.vencedor_01)
        game_status = True
        return game_status
    else:
        game_status = False
        return game_status


def main():

    if len(lista_jogadores) == 3:  # CAMINHO PARA TRÊS JOGADORES SIMULTÂNEOS

        # ESCOLHA DA PALAVRA DA CATEGORIA TECH DIFICIEIS
        palavra1 = escolhe_palavras(messages.tech_dificeis)
        palavra2 = escolhe_palavras(messages.tech_dificeis)
        palavra3 = escolhe_palavras(messages.tech_dificeis)
        em_brancos1 = list(palavra1)

        em_brancos2 = list(palavra2)
        em_brancos3 = list(palavra3)

        numero_de_vidas = []  # LISTA VAZIA PARA ARMAZENAR VIDAS DO JOGADOR 1
        numero_de_vidas2 = []  # LISTA VAZIA PARA ARMAZENAR VIDAS DO JOGADOR 2
        numero_de_vidas3 = []  # LISTA VAZIA PARA ARMAZENAR VIDAS DO JOGADOR 3
        game_over = False

        

        for i in range(len(em_brancos1)):
            em_brancos1[i] = "_"
        print(f"{lista_jogadores[0]}: Você terá que tentar advinhar a seguinte palavra. Digite somente uma letra por vez: ",
              em_brancos1)
     
        for i in range(len(em_brancos2)):
            em_brancos2[i] = "_"
        print(
            f"{lista_jogadores[1]}: Você terá que tentar advinhar a seguinte palavra. Digite somente uma letra por vez: ", em_brancos2)

        for i in range(len(em_brancos3)):
            em_brancos3[i] = "_"
        print(
            f"{lista_jogadores[2]}: Você terá que tentar advinhar a seguinte palavra. Digite somente uma letra por vez: ", em_brancos3)


        while len(numero_de_vidas) < 7 and len(numero_de_vidas2) < 7 and len(numero_de_vidas3) < 7 and game_over == False:
            player = 1
            em_brancos1, numero_de_vidas = seleciona_letras(
                palavra1, em_brancos1, numero_de_vidas)
            game_over = check_win(
                numero_de_vidas, em_brancos1, player, game_over)

            player = 2
            em_brancos2, numero_de_vidas2 = seleciona_letras(
                palavra2, em_brancos2, numero_de_vidas2)
            game_over = check_win(
                numero_de_vidas2, em_brancos2, player, game_over)

            player = 3
            em_brancos3, numero_de_vidas = seleciona_letras(
                palavra3, em_brancos3, numero_de_vidas3)
            game_over = check_win(
                numero_de_vidas3, em_brancos3, player, game_over)

        if numero_de_vidas > numero_de_vidas2 or numero_de_vidas > numero_de_vidas3:  # Refazer lógica de saída
            print("Player 2 win")
        elif numero_de_vidas2 > numero_de_vidas or numero_de_vidas2 > numero_de_vidas3:
            print("Player 1 win")
        elif numero_de_vidas3 > numero_de_vidas:
            print("Player 1 win")
        elif numero_de_vidas3 > numero_de_vidas2:
            print("Player 1 win")

        else:
            print("Tie")

        print(em_brancos1)
        print(em_brancos2)
        print(em_brancos3)

    if len(lista_jogadores) == 2:  # CAMINHO PARA DOIS JOGADORES SIMULTÂNEOS

        auxiliar_1 = escolhe_palavras(messages.tech_dificeis)
        palavra1 = auxiliar_1.lower()
        # print(palavra1)
        auxiliar_2 = escolhe_palavras(messages.tech_dificeis)
        palavra2 = auxiliar_2.lower()
        # print(palavra2)

        em_brancos1 = list(palavra1)
        # print(em_brancos1)
        em_brancos2 = list(palavra2)

        numero_de_vidas = []  # array for two player vidas for player 1
        numero_de_vidas2 = []  # array for two player vidas for player 2

        game_over = False

        for i in range(len(em_brancos1)):

            em_brancos1[i] = "_"
        print(
            f"{lista_jogadores[0]}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos1, '\n')
        print()

        # print em_brancos2
        for i in range(len(em_brancos2)):
            em_brancos2[i] = "_"
        print(
            f"{lista_jogadores[1]}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos2, '\n')
        print()

        while len(numero_de_vidas) < 7 and len(numero_de_vidas2) < 7 and game_over == False:
            player = lista_jogadores[0]
            em_brancos1, numero_de_vidas = seleciona_letras(palavra1, em_brancos1, numero_de_vidas)
            game_over = check_win(numero_de_vidas, em_brancos1, player, game_over)

            player = lista_jogadores[1]
            em_brancos2, numero_de_vidas2 = seleciona_letras(palavra2, em_brancos2, numero_de_vidas2)
            game_over = check_win(numero_de_vidas2, em_brancos2, player, game_over)

        if numero_de_vidas > numero_de_vidas2:
            print(f"{lista_jogadores[1]} VOCÊ VENCEU!!!")
            print(images.vencedor_02)

        elif numero_de_vidas2 > numero_de_vidas:
            print(f"{lista_jogadores[0]} VOCÊ VENCEU!!!")
            print(images.vencedor_02)

        else:
            print("PARABÉNS AOS DOIS: DEU EMPATE!")

        print(em_brancos1)
        print(em_brancos2)


limpa_tela()
imprime_mensagem_abertura()
numero_jogadores()
# print(lista_jogadores)
modo_de_jogo()
