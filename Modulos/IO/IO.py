"""arquivo = open('text.txt')

print(arquivo.read())
print(arquivo.read())  # O cursor do arquivo está no final, por isso ele não lê essa linha
arquivo.seek(0)  # O comando seek(0) faz o cursor voltar apara o início do arquivo, permitindo a leitura.
print(arquivo.read())
arquivo.seek(0)
print(arquivo.readline())
arquivo.seek(0)
print(' ---- Readlines  ---- ')
print(arquivo.readlines())

arquivo.close()"""

with open('arquivo/text.txt', mode='a') as arquivo:  # Usando esse método, não é necessário fechar o arquivo no final, pois ele é aberto
    # como uma variável.
    # Usando o mode, podemos mudar entre apenas ler e/ou escrever
    texto = arquivo.write('Sou uma nova linha inserida a partir do python :)')
    print(texto) # Nesse momento, o arquivo vai sobrescerver o início do texto para evitar isso, é melhor usar apenas o mode =w

with open('arquivo/sad.txt', mode='w') as arquivo2: # Até o momento esse arquivo não existia, assim, ele foi criado.
    texto2 = ':('
    print(texto2)