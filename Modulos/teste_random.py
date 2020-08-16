from random import randint
from sys import argv

numero = randint(1, 100)
print(numero)


def chute():
    global numero
    tentativa = int(input('Qual é o número certo? '))
    if tentativa == numero:
        print('Parabéns! Você acertou')
        if input(f'\nQuer jogar de novo? (s/n)') == 'n':
            print(f' \nOK! Até a próxima!')
        else:
            numero = randint(1, 100)
            chute()
    else:
        print('Tente novamente!')
        chute()


chute()
