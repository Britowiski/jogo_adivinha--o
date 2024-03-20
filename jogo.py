# Criação da Função
def jogo_palavra():
    palavra_secreta = "Cachorro"
    letras_acertadas = ''
    tentativas_acertos = 0
    letras_erradas = ''

    # Condição do While, enquanto for verdadeiro
    while True:
        letra_digitada = input("Digite uma letra: ")

        # Letra diferente de 1, não é permitido a entrada do input
        if len(letra_digitada) != 1:
            print("Digite apenas uma letra.")
            continue

        # Condição se a letra digitada estiver correta, será adicionada na memória da variável letras acertadas
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
        else:
            letras_erradas += letra_digitada  # Caso esteja errado, é adicionado na variável letras erradas, não podendo tentar a mesma letra
            tentativas_acertos += 1
            print("Letras erradas:\n", letras_erradas)

        palavra_formada = ''  # Essa variável irá receber as letras e será montada de forma horizontal e não vertical
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta  # Nessa condição será adicionada a letra a variável que está para mostrar as palavras em horizontal
            else:
                palavra_formada += '*'

        print('Palavra Formada:', palavra_formada)  # Aqui será atualizada a palavra conforme for acertando

        # Por fim, verifica se a palavra formada conforme as entradas é igual ao que foi colocado para ser acertado, caso sim, finaliza
        if palavra_formada == palavra_secreta:
            print("Você acertou!")
            print("A palavra secreta é:", palavra_secreta)
            print("O número de tentativas foi:", tentativas_acertos)
            letras_acertadas = ''
            tentativas_acertos = 0
            break

jogo_palavra()

# Finaliza fora da função, é perguntado ao usuário se gostaria de continuar, caso sim, chama a função novamente e inicia um novo jogo.
continuar = input("Você gostaria de continuar jogando?\n").lower()

if continuar == "sim":
    print("Okay, vamos continuar\n")
    tentativas_acertos = 0  # Reinicializa o número de tentativas
    jogo_palavra()
else:
    print("Okay, obrigado por jogar")
