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

        tema = escolhe_tema.lower()  # forçando a condição de string lower (minúscula)

        if tema == 'a':  # Não usei método lower ou upper por conta da saída
            # se condição acima for atendida, grava '0' na lista indice_tema
            indice_tema.append(0)
            opcao_tema = True  # interrompe o loop
            return indice_tema  # dá a saída da função escolha_tema

        elif tema == 'b':
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

        nivel = escolhe_nivel.lower()

        if nivel == 'a':
            indice_nivel.append(0)
            opcao_nivel = True
            return indice_nivel

        elif nivel == 'b':
            indice_nivel.append(1)
            opcao_nivel = True
            return indice_nivel

        elif nivel == 'c':
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
    if sum(indice_tema) == 0 and sum(indice_nivel) == 0:
        print(formatting.escolher_cor(
            'yellow', messages.geral_faceis_dicionario[palavra_secreta.lower()]))
    if sum(indice_tema) == 0 and sum(indice_nivel) == 1:
        print(formatting.escolher_cor(
            'yellow', messages.geral_medianas_dicionario[palavra_secreta.lower()]))
    if sum(indice_tema) == 0 and sum(indice_nivel) == 2:
        print(formatting.escolher_cor(
            'yellow', messages.geral_dificeis_dicionario[palavra_secreta.lower()]))
    if sum(indice_tema) == 1 and sum(indice_nivel) == 0:
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_faceis[palavra_secreta.lower()]))
    if sum(indice_tema) == 1 and sum(indice_nivel) == 1:
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_medianas[palavra_secreta.lower()]))
    if sum(indice_tema) == 1 and sum(indice_nivel) == 2:
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_dificeis[palavra_secreta.lower()]))

    print()
    return ["_" for letra in palavra_secreta]


tentativas = []

def letras_repetidas():
    if pede_chute() == tentativas:
        print('Você já digitou essa letra!!! ')
        tentativas.append(pede_chute())
         
        return tentativas




def pede_chute():
    formatting.forma_linha()
    print(palavra_secreta)
    # if sum(indice_tema) == 0 and sum(indice_nivel) == 1:
    #    print(messages.geral_medianas_dicionario[palavra_secreta])
    # if sum(indice_tema) == 0 and sum(indice_nivel) == 2:
    #    print(messages.geral_dificeis_dicionario[palavra_secreta])
    # else:
    #    print('nada')

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


def imprime_mensagem_vencedor(palavra_secreta):
    print(formatting.escolher_cor(
        'green', f"Parabéns {lista_jogadores[0].upper()} você ganhou!"))
    print(images.show_de_bola)
    print(images.vencedor_02)


def imprime_mensagem_perdedor(palavra_secreta):
    print()
    print(formatting.escolher_cor(
        'red', f"Puxa vida! {lista_jogadores[0].upper()} você foi enforcado!"))
    print(formatting.escolher_cor(
        'yellow', f'A palavra secreta era {palavra_secreta.upper()}'))
    print(images.game_over)


def reinicia_jogo():  # PARA O JOGO MODO SINGLEPLAYER

    reiniciar = False

    while reiniciar == False:
        formatting.forma_linha()
        texto = '''
Deseja jogar novamente??
Em caso positivo, digite S para continuar ou N para sair: '''
        reinicia_jogo = input(formatting.escolher_cor('yellow', texto))

        if reinicia_jogo == 's' or reinicia_jogo == 'S':
            print('vamos jogar de novo')
            resposta_sim = 's'
            reiniciar == True
            letras_digitadas.clear()
            tentativas.clear()
            indice_tema.clear()
            indice_nivel.clear()

            jogar()
            return resposta_sim

        elif reinicia_jogo == 'n' or reinicia_jogo == 'N':
            print('Até Logo!')
            exit()

        else:
            print('OPÇÃO INVALIDA. DIGITE S OU N')
            reiniciar == False


def reinicia_jogo_2():  # PARA O JOGO MODO MULTIPLAYER

    reiniciar = False

    while reiniciar == False:
        formatting.forma_linha()
        texto = '''
Deseja jogar novamente??
Em caso positivo, digite S para continuar ou N para sair: '''
        reinicia_jogo = input(formatting.escolher_cor('yellow', texto))

        if reinicia_jogo == 's' or reinicia_jogo == 'S':
            print('vamos jogar de novo')
            resposta_sim = 's'
            reiniciar == True
            letras_digitadas.clear()
            tentativas.clear()
            indice_tema.clear()
            indice_nivel.clear()

            jogar_2()
            return resposta_sim

        elif reinicia_jogo == 'n' or reinicia_jogo == 'N':
            print('Até Logo!')
            exit()

        else:
            print('OPÇÃO INVALIDA. DIGITE S OU N')
            reiniciar == False


def desenha_forca(erros):  # PARA AMBOS OS MODOS DE JOGO

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
                print(formatting.escolher_cor('green', "WOW!! Você encontrou todas as letras formando a palavra '{}'".format(
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
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


def jogar_2():
    limpa_tela()
    print(images.multiplayer)
    formatting.forma_linha()
    main()


def seleciona_letras(segredo, palavra_em_branco, numero_de_vidas):  # original seleciona_letras

    # Para assegurar a funcionalidade do código caso os usuários digitem números ou caracteres especiais
    somente_letra = False

    while somente_letra == False:
        letra_advinhada = input(
            "Por favor, informe seu palpite, digite somente uma letra: ")

        if letra_advinhada.isalpha() == True:  # isalpha() retorna True caso a entrada seja uma string do alfabeto
            sinaliza_vidas = 0

            # converte a string para minúscula
            for i in [i for i, x in enumerate(segredo) if x == letra_advinhada.lower()]:
                sinaliza_vidas = 1
                # converte a string para minúscula
                palavra_em_branco[i] = letra_advinhada.lower()

            numero_de_vidas = valida_vidas(sinaliza_vidas, numero_de_vidas)

            print(numero_de_vidas)

            return palavra_em_branco, numero_de_vidas
        else:
            limpa_tela()

            print(images.atencao)
            print(formatting.escolher_cor(
                'yellow', 'POR FAVOR!!! DIGITE SOMENTE LETRAS MAIÚSCULAS OU MINÍSCULAS, SEM NÚMEROS OU CARACTERES ESPECIAIS!!!'))

            formatting.forma_linha()


def valida_vidas(sinaliza_vidas, vidas):

    if sinaliza_vidas > 0:  # Aqui checará se sinaliza_vidas é maior que 0, sendo, o jogador respondeu corretamente

        print("Número de vidas inalterado, vida(s) perdida(s): ", len(vidas))

        # limpa_tela()

        return vidas
    else:
        # Já se o contador sinaliza_vidas for menor que 0, indicará que o jogador errou a letra e então adicionará o erro:
        vidas.append("1")  # aqui

        print(f"Oh oh! Você perdeu {len(vidas)} vida(s)...")

        # limpa_tela()

        # Aqui ele começará a desenhar a forca à medida que se somam os erros das letras:
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

        return vidas


def check_win(vidas, em_branco, numero_jogador, game_status):
    print(numero_jogador)
    print(f'Checa acertos: {em_branco} ')
    # print(messages.tech_dicionario_dificeis[palavra_secreta])
    print()
    print()

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

        auxiliar_1 = escolhe_palavras(messages.tech_dificeis)
        palavra1 = auxiliar_1.lower()

        auxiliar_2 = escolhe_palavras(messages.tech_dificeis)
        palavra2 = auxiliar_2.lower()

        auxiliar_3 = escolhe_palavras(messages.tech_dificeis)
        palavra3 = auxiliar_3.lower()

        em_brancos1 = list(palavra1)
        em_brancos2 = list(palavra2)
        em_brancos3 = list(palavra3)

        numero_de_vidas = []  # LISTA VAZIA PARA ARMAZENAR VIDAS DO JOGADOR 1
        numero_de_vidas2 = []  # LISTA VAZIA PARA ARMAZENAR VIDAS DO JOGADOR 2
        numero_de_vidas3 = []  # LISTA VAZIA PARA ARMAZENAR VIDAS DO JOGADOR 3

        game_over = False

        for i in range(len(em_brancos1)):
            em_brancos1[i] = "_"
        formatting.forma_linha()
        print(
            f"{formatting.escolher_cor('blue', lista_jogadores[0].upper())}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos1, '\n')
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_dificeis[palavra1]))
        print()

        formatting.forma_linha()

        for i in range(len(em_brancos2)):
            em_brancos2[i] = "_"
        print(
<<<<<<< Updated upstream
            f"{lista_jogadores[1]}: Você terá que tentar advinhar a seguinte palavra. Digite somente uma letra por vez: ", em_brancos2)
=======
            f"{formatting.escolher_cor('green',lista_jogadores[1].upper())}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos2, '\n')
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_dificeis[palavra2]))
        print()

        formatting.forma_linha()
>>>>>>> Stashed changes

        for i in range(len(em_brancos3)):
            em_brancos3[i] = "_"
        print(
<<<<<<< Updated upstream
            f"{lista_jogadores[2]}: Você terá que tentar advinhar a seguinte palavra. Digite somente uma letra por vez: ", em_brancos3)
=======
            f"{formatting.escolher_cor('yellow',lista_jogadores[2].upper())}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos2, '\n')
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_dificeis[palavra3]))
        print()

        formatting.forma_linha()
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
=======
        # ESCOLHA DA PALAVRA DA CATEGORIA TECH DIFICIEIS

>>>>>>> Stashed changes
        auxiliar_1 = escolhe_palavras(messages.tech_dificeis)
        palavra1 = auxiliar_1.lower()

        auxiliar_2 = escolhe_palavras(messages.tech_dificeis)
        palavra2 = auxiliar_2.lower()

        em_brancos1 = list(palavra1)
        # print(em_brancos1)
        em_brancos2 = list(palavra2)

        numero_de_vidas = []  # lista para registrar as vidas perdidas do jogador 1
        numero_de_vidas2 = []  # lista para registrar as vidas perdidas do jogador 2

        game_over = False

        for i in range(len(em_brancos1)):

            em_brancos1[i] = "_"
        print(
<<<<<<< Updated upstream
            f"{lista_jogadores[0]}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos1, '\n')
=======
            f"{formatting.escolher_cor('blue', lista_jogadores[0].upper())}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos1, '\n')
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_dificeis[palavra1]))
>>>>>>> Stashed changes
        print()
        # print(messages.tech_dicionario[palavra1])
        print(formatting.forma_linha())

        # print em_brancos2
        for i in range(len(em_brancos2)):
            em_brancos2[i] = "_"
        print(
<<<<<<< Updated upstream
            f"{lista_jogadores[1]}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos2, '\n')
=======
            f"{formatting.escolher_cor('green',lista_jogadores[1].upper())}: Você terá que tentar advinhar a seguinte palavra. \nDigite somente uma letra por vez: \n", "\n", em_brancos2, '\n')
        print(formatting.escolher_cor(
            'yellow', messages.tech_dicionario_dificeis[palavra2]))
>>>>>>> Stashed changes
        print()
        print(formatting.forma_linha())

        while len(numero_de_vidas) < 7 and len(numero_de_vidas2) < 7 and game_over == False:
            player = lista_jogadores[0]
            em_brancos1, numero_de_vidas = seleciona_letras(
                palavra1, em_brancos1, numero_de_vidas)
            game_over = check_win(
                numero_de_vidas, em_brancos1, player, game_over)

            player = lista_jogadores[1]
            em_brancos2, numero_de_vidas2 = seleciona_letras(
                palavra2, em_brancos2, numero_de_vidas2)
            game_over = check_win(
                numero_de_vidas2, em_brancos2, player, game_over)

        if numero_de_vidas > numero_de_vidas2:
            limpa_tela()
            print(f"{lista_jogadores[1]} VOCÊ VENCEU!!!")
            print(images.vencedor_02)
            game_over = True

        elif numero_de_vidas2 > numero_de_vidas:
            limpa_tela()
            print(f"{lista_jogadores[0]} VOCÊ VENCEU!!!")
            print(images.vencedor_02)
            game_over = True

        else:
            print("PARABÉNS AOS DOIS: DEU EMPATE!")

<<<<<<< Updated upstream
        print(em_brancos1)
        print(em_brancos2)


limpa_tela()
imprime_mensagem_abertura()
numero_jogadores()
modo_de_jogo()
=======
        print(lista_jogadores[0], em_brancos1,
              'A palavra secreta era: ', palavra1)
        print(lista_jogadores[1], em_brancos2,
              'A palavra secreta era: ', palavra2)
        reinicia_jogo_2()
>>>>>>> Stashed changes
