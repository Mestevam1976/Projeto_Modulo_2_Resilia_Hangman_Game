def forma_linha():  # Imprime linha com o caractere =
    print('=' * 110)

def p():  # Pula uma linha
    print('\n')

def escolher_cor(cor, texto):  # função para definir as cores das mensagens
    if cor == 'red':
        return f'\033[91m {texto} \033[0m'

    if cor == 'blue':
        return f'\033[94m {texto} \033[0m'

    if cor == 'yellow':
        return f'\033[93m {texto} \033[0m'

    if cor == 'green':
        return f'\033[92m {texto} \033[0m'