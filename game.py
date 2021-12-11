# Imports
from datetime import datetime
import random


# Retorna o horário definido no sistema do usuário.
def mostra_hora_abertura():
    hora = datetime.now()
    hora_format = hora.strftime('%H:%M')
    return hora_format
hora_agora = mostra_hora_abertura()


# Retorna a saldação de acordo com o horário definido no sistema do usuário.
def mostra_saldacao():
    if hora_agora < '12':
        return 'Bom Dia'
    elif hora_agora < '18':
        return 'Boa Tarde'
    return 'Boa Noite'
retorna_saldacao = mostra_saldacao()


# Retorna para o usuário a abertura do jogo
def mostra_abertura():
    print('*' * 20)
    print('{} - {}\nBem-vindo ao jogo da Forca!'.format(retorna_saldacao, hora_agora))
    print('*' * 20)
mostra_abertura()


# Retorna as frutas em um arquivo .txt e randomiza os nomes.
def carrega_palavra():
    arquivo = open('palavras.txt', 'r', encoding='utf-8')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero_palavra = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero_palavra]
    return palavra_secreta.upper()

palavra_jogo = carrega_palavra()


# inicializa uma palavra do arquivo .txt
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

letras_acertadas = inicializa_letras_acertadas(palavra_jogo)


# Chute do usuário
def pede_chute():
    chute = input('Insira uma letra: ').strip().upper()
    if len(chute) > 1 or len(chute) < 1:
        print('Insira uma letra!')
    return chute


# marca o chute e o índice da letra de acordo com a palavra.
def marca_chute(chute, letras_acertadas, palavra_jogo):

    for index, letra in enumerate(palavra_jogo):
        if chute == letra:
            letras_acertadas[index] = letra

print(letras_acertadas)

enforcou, acertou = False, False
erros = 0

# jogo
while not enforcou and not acertou:
    chute = pede_chute()

    if chute in palavra_jogo:
        marca_chute(chute, letras_acertadas, palavra_jogo)
    else:
        erros += 1

    enforcou, acertou = erros == 7, '_' not in letras_acertadas
    print(letras_acertadas)

if acertou:
    print('Você ganhou!')
else:
    print('Você perdeu, {}!'.format(palavra_jogo))






