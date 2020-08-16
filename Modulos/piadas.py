import pyjokes


while True:
    piada = pyjokes.get_joke('en', 'neutral')
    print(piada)
    resp = input('Que mais uma? (s/n) ')
    if resp == 'n':
        print('Obrigado, até a próxima!!')
        break

