# função para so receber número real
def lFloat(msg):
    '''

    :param msg: mensagem que vai ser exibida na hora de receber dados
    :return: numero float
    '''
    while True:
        try:
            n = float(input(msg))
        except (Exception, ZeroDivisionError):
            print('\033[31mERRO!! por favor digite um numero inteiro.\033[m\n')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario: \033[m')
            return 0
        else:
            return n

def lint(msg):
    '''

    :param msg: mensagem que vai ser exibida na hora de receber dados
    :return: numero float
    '''
    while True:
        try:
            n = int(input(msg))
        except (Exception):
            print('\033[31mERRO!! por favor digite um numero real.\033[m\n')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario: \033[m')
            return 0
        else:
            return n


# função de somar
def somar():
    from sistemas import visor, perg

    visor('  SOMA  ', linhas=True, cor='red')
    n1 = lFloat("1° Valor: ")
    n2 = lFloat('2° Valor: ')
    r = n1 + n2
    print(f'{n1} + {n2} = {r}')

    while True:
        resp = perg()
        if resp in 'S':
            add = lFloat(f'{r} + ')
            print(f'{r} + {add} =', end=' ')
            r = r + add
            print(r)
        if resp in 'N':
            visor('Encerrando...\n\n', cor='red')
            return r


# função de subtrair
def subt():
    from sistemas import visor, perg

    visor('  SUBTRAIR  ', linhas=True, cor='green')
    n1 = lFloat('1° Valor: ')
    n2 = lFloat('2° Valor: ')
    r = n1 - n2
    print(f'{n1} - {n2} = {r}')

    while True:
        resp = perg()
        if resp in 'S':
            add = lFloat(f'{r} - ')
            print(f'{r} - {add} =', end=' ')
            r = r - add
            print(r)
        if resp in 'N':
            visor('Encerrando...\n\n', cor='red')
            return r


# função de dividir
def div():
    from sistemas import visor, perg

    visor('  DIVISÃO  ', linhas=True, cor='yellow')
    n2 = n1 = 0
    while n2 == 0:
        n1 = lFloat('Dividendo: ')
        n2 = lFloat('Divisor: ')
        if n2 != 0:
            r = n1 / n2
            print(f'{n1} ÷ {n2} = {r}')
            break
        else:
            print(str('\033[31mDivisão por 0 Não Existe, tente novamente..\033[m\n'))
        
    while True:
        resp = perg()
        if resp in 'S':
            while True:
                add = lFloat(f'{r} ÷ ')
                if add != 0:
                    break
                else:
                    print("\033[31mNão e possivel dividir um Número com 0, tente denovo...\033[m")
            print(f'{r} ÷ {add} =', end=' ')
            r = r / add
            print(r)
        else:
            visor('Encerrando...\n\n', cor='red')
            return r


# função de multiplicar
def mult():
    from sistemas import visor, perg

    visor('  MULTPLICAÇÃO  ', linhas=True, cor='blue')
    n1 = lFloat('Numerador: ')
    n2 = lFloat('Multiplicador: ')
    r = n1 * n2
    print(f'{n1} × {n2} = {r}')

    while True:
        resp = perg()
        if resp in 'S':
            add = lFloat(f'{r} × ')
            print(f'{r} × {add} =', end=' ')
            r = r * add
            print(r)
        if resp in 'N':
            visor('Encerrando...\n\n', cor='red')
            return r


# função de fazer a raiz quadrada de um número
def raiz():
    from sistemas import visor, perg

    visor('  RAIZ QUADRADA  ', linhas=True, cor='purple')
    while True:
        x = lFloat('Número: ')
        r = x ** (1 / 2)
        print(f'²√{x} = {r}')
        resp = perg()
        if resp in 'N':
            break
        if resp in 'S':
            continue
        if resp in 'N':
            visor('Encerrando...\n\n', cor='red')
            return r


# função de fatoriar um número
def fat():
    from sistemas import visor, perg

    visor('  FATORIAL  ', linhas=True, cor='cian')
    while True:
        n = lint('Digite Um Valor Para Fatorizar: ')
        print(f'Calculando {n}! = ', end='')
        c = n
        f = 1
        while c > 0:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        print(f)
        resp = perg()
        if resp in 'S':
            continue
        if resp in 'N':
            visor('Encerrando...\n\n', cor='red')
            return f

