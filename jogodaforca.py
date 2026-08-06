# jogo-da-forca
print("*********************************")
print("Bem vindo ao jogo da força")
print("*********************************")

palavrasecreta = "forte"
palavrasacertadas = ["_","_","_","_","_","_"]

enforcou = False
acertou = False
tentativas = 0
while(not enforcou and not acertou):
    Chute = input("Digite uma letra? ")
    chute = chute.strip()

    index = 0
    for letra in pallavrasecreta:
        if(chute.upper() == letra.upper()):
            print("Encontrei a letra {} na posição{}".format(letra,index))
        index = index + 1

    print("jogando")

print("fim do jogo")

else:
    tentativa += 1

    # controle de tentativas
    enforto = tentativas == total_tentativas
    efortou = "_" not in letras cartadas
    print("letrasacertadas: {}",format(letrascertadas))
    print("tentativasrestantes: {}",format(total_tentativa - tentativa))

    if(acerto):
        print("parabens, voce ganhou!")
        elif(enfornou):
            print("voce perdeu! A palavra era {}",format(palavrassecretas))

        
    print("fim do jogo")