from time import sleep
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

print("CALCULANDO MÉDIA...")
sleep(2)

print("Sua média é {:.2f}".format(media))

if media < 5:
    print("REPROVADO!")
elif (media > 5) < 6.9:
    print("RECUPERAÇÃO!")
else:
    print("APROVADO!")