from translate import Translator

tradutor = Translator(from_lang='pt-br', to_lang='en')
with open('arquivo/letra.txt', mode='r') as letra:
    texto = letra.read()
    texto = tradutor.translate(texto)
    print(texto)

with open('arquivo/lyrics.txt', mode='w') as traducao:
    traducao.write(texto)

