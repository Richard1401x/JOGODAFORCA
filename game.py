import random
from time import sleep


def escolher_palavra():
    palavras = ['abacaxi', 'laranja', 'manga', 'morango', 'kiwi', 'banana', 'pera']
    return random.choice(palavras)

def mostrar_forca(palavra, letras_corretas):
    espacos = ''
    for letra in palavra:
        if letra in letras_corretas:
            espacos += letra
        else:
            espacos += '_'
    return espacos

def desenhar_enforcamento(tentativas):
    if tentativas == 6:
        print("  ________")
        print("  |/")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|________")
    elif tentativas == 5:
        print("  ________")
        print("  |/   |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|________")
    elif tentativas == 4:
        print("  ________")
        print("  |/   |")
        print("  |    O")
        print("  |")
        print("  |")
        print("  |")
        print("__|________")
    elif tentativas == 3:
        print("  ________")
        print("  |/   |")
        print("  |    O")
        print("  |    |")
        print("  |")
        print("  |")
        print("__|________")
    elif tentativas == 2:
        print("  ________")
        print("  |/   |")
        print("  |    O")
        print("  |   /|")
        print("  |")
        print("  |")
        print("__|________")
    elif tentativas == 1:
        print("  ________")
        print("  |/   |")
        print("  |    O")
        print("  |   /|\\")
        print("  |")
        print("  |")
        print("__|________")
    else:
        print("  ________")
        print("  |/   |")
        print("  |    O")
        print("  |   /|\\")
        print("  |   /")
        print("  |")
        print("__|________")

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    sleep(4)
    print('Serão apenas 6 tentativas')
    sleep(3)
    print('iniciando o game, Boa sorte...')
    sleep(2)
    while True:
        print("\n" + mostrar_forca(palavra, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        desenhar_enforcamento(tentativas)

        if '_' not in mostrar_forca(palavra, letras_corretas):
            print(f"Parabéns! Você acertou a palavra: {palavra}")
            break
        elif tentativas == 0:
            print(f"Suas tentativas acabaram. A palavra era: {palavra}")
            break

        palpite = input("Digite uma letra: ")

        if palpite in palavra:
            if palpite not in letras_corretas:
                letras_corretas.append(palpite)
        else:
            tentativas -= 1
            print("Letra incorreta. Tente novamente.")

if __name__ == "__main__":
    jogo_da_forca()
