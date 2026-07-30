# jogo-da-forca
print("*********************************")
print("Bem vindo ao jogo da força")
print("*********************************")

palavrasecreta = "forte"
palavrasacertadas = ["_","_","_","_","_","_"]

enforcou = False
acertou = False

while(not enforcou and not acertou):
    Chute = input("Digite uma letra? ")
    chute = chute.strip()

    index = 0
    for letra in pallavrasecreta:
        if(chute.upper() == letra.upper())
            print("Encontrei a letra {} na posição{}".format(letra,index))
        index = index + 1

    print("jogando")

print("fim do jogo")