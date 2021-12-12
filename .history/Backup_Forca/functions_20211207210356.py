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


def escolha_tema():  # Função para selecionar o tema específico, localizado no arquivo messages.py
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
    palavra_secreta = caminho()


palavra_secreta = caminho()


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
    print(images.vencedor_02)

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

    limpa_tela()
    imprime_mensagem_abertura()
    escolha_tema()
    limpa_tela()
    formatting.forma_linha()
    escolha_nivel()
    limpa_tela()
    caminho()

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
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print(formatting.escolher_cor('green', "PARABÉNS!! Você encontrou todas as letras formando a palavra '{}'".format(
                    palavra_secreta.upper())))
        else:
            erros += 1
            print(letras_acertadas)
            print(formatting'Ainda faltam acertar {} letras'.format(letras_faltando))
            print('Você ainda tem {} tentativas'.format(7-erros))
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")


if(__name__ == '__main__'):
    jogar()
