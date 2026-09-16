from time import sleep
idade = int(input("Digite sua idade: "))

print("CALCULADO...")
sleep(2)

if idade < 18:
    print("Segundo sua idade, não está na hora de se alistar!")
elif idade == 18:
    print("Está na hora de se alistar!")
else:
    print("Já passou da hora de se alistar!")