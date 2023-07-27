from sistemas import *
from operadores import *
from time import sleep


visor('CALCULADORA v1.0🤖', linhas=True, cor='cian')

while True:
    sleep(1)
    Op = showOp()
    sleep(0.5)
    if Op == 0:
        visor('Encerrando o Programa..', cor='yellow')
        break
    if Op == 1:
        somar()
    if Op == 2:
        subt()
    if Op == 3:
        div()
    if Op == 4:
        mult()
    if Op == 5:
        raiz()
    if Op == 6:
        fat()

visor('FIM! volte sempre', linhas=True, cor='red')

