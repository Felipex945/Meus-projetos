import random
from time import sleep

computador = random.randint(0, 10)

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar!")
print("-=-" * 20)

jogador = int(input("Em que número eu pensei? "))

while jogador != computador:
    print("Resposta incorreta! Tente novamente.")
    jogador = int(input("Em que número pensei? "))
print(f"Parabéns! você acertou. Eu escolhi o número {computador} também!")