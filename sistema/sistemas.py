# função para validar se o dado é numero real
def validNum(mensagem):
    '''

    :param mensagem: mensagem que deseja ser exibida na hora de receber dados
    :return: numero float
    '''
    while True:
        try:
            num = float(input(mensagem))
        except Exception:
            print('\033[31mOpção Invalida..\033[m\n')
            continue
        else:
            return num


# função prática para exibição de textos
def visor(txt, linhas=False, cor='reset'):
    '''

    :param txt: Mensagem que você quer exibir
    :param linhas: caso deseje que o texto fique entre linhas
    :param cor: cor do texto
    :return: mensagem com cor e linhas de forma prática
    '''
    cores = {'reset': '\033[m',
             'red': '\033[31m',
             'green': '\033[32m',
             'yellow': '\033[33m',
             'blue': '\033[34m',
             'purple': '\033[35m',
             'cian': '\033[36m',
             'gray': '\033[37m',
             'negative': '\033[7m'}
    if linhas:
        tam = len(txt) + 6
        print(f'{cores[cor]}{"—" * tam}')
        print(f'{txt.center(tam)}')
        print(f'{"—" * tam}{cores["reset"]}')
    else:
        print(f'{cores[cor]}{txt}{cores["reset"]}')


# função criada para mostrar e escolher uma das opções da calculadora
def showOp():
    print('''
————————————————————————
\033[37mDigite [ 0 ] para sair\n
\033[31m1 → Somar[ + ]
\033[32m2 → Subtrair[ - ]
\033[33m3 → Dividir[ ÷ ]
\033[34m4 → Multiplicar[ × ]
\033[35m5 → Raiz Quadrada[ √ ]
\033[36m6 → Fatorizar[ ! ]\033[m
————————————————————————''')
    while True:
        resp = validNum('Digite:')
        if resp < 0 or resp > 6:
            print('\033[31mOpção Invalida..\033[m\n')
        else:
            return resp


# função criada para verificar se ele que continuar o ciclo
def perg():
    '''
    -> essa função foi criada para colocar nas while True
    você utilizara ela para ter alternativa de continuar ou não
    o ciclo

    :return: S ou N
    '''
    while True:
        resp = ' '
        try:
            resp = str(input('\nContinuar? [\033[32mS\033[m | \033[31mN\033[m]: ')).strip().upper()[0]
            if resp in 'SN':
                if resp in "S":
                    return resp
                else:
                    return resp
            else:
                print('\033[31mTente Denovo...\033[m')
        except (Exception, KeyboardInterrupt, UnboundLocalError):
            print('\033[31mTente Novamente...\033[m')
        



