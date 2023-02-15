import random

print("*********************")
print("JOGO DE ADIVINHAÇÃO!")
print("*********************")

secret_number = random.randrange(1,1000)
total_de_tentativas= 0
points= 1000
pontos_perdidos= 0
round= 0

print("Qual o nivel de dificuldade?")
print("(1)Eazy (2)Medium (3)Hard")
level= int(input("Defina o nivel: "))
if(level==1):
    total_de_tentativas = 30
    pontos_perdidos= 25
elif(level==2):
    total_de_tentativas= 20
    pontos_perdidos=50
else:
    total_de_tentativas = 10
    pontos_perdidos= 100
for round in range(total_de_tentativas):
    print("\nTentaivas, {} de, {}".format(round, total_de_tentativas))
    chute= int(input("Digite o número ente 1 e 1000:"))
    print("\nVocê digitou", chute)
    if(chute < 1 or chute > 1000):
        print("Você deve digitar um número entre 1 e 1000!")
        continue

    acertou = bool(chute == secret_number)
    maior = bool(chute > secret_number)
    menor = bool(chute < secret_number)

    if(acertou == True):
        print("Você acertou e fez {} pontos!".format(points))
        break
    else:
        points = points - pontos_perdidos
        if(maior):
            print("Você errou! O seu chute foi maior que o númerio secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
            print("Minimo {}".format(chute))
        round = round + 1

if(round == total_de_tentativas):
        print("O número secreto era: {}".format(secret_number))
        
print("FIM DE JOGO!")
input()