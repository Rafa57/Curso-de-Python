# Faça um jogo para o usuário adivinhar a palavra secreta.
import os

palavra = 'carro'
letras_acertadas = ''
tentativas = 0

while True:
    
    
    entrada = input('Tente adivinhar a palavra secreta. Digite uma letra: ').lower()
    tentativas += 1
    
    if len(entrada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if entrada in palavra:
        letras_acertadas += entrada
    
    palavra_formada = ''
    for i in palavra:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += '_'
    print('Palavra: ', palavra_formada)
    
    if palavra_formada == palavra:
        os.system('cls')
        print('Parabéns! Você acertou a palavra secreta.')
        print(f'Tentativas: {tentativas}')
        letras_acertadas = ''
        tentativas = 0
