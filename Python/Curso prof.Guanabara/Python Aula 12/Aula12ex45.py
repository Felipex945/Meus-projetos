import random
escolha = str(input("Escolha entre pedra, papel e tesoura: "))
jokenpo = ['pedra', 'papel', 'tesoura']

pc_jogada = random.choice(jokenpo)
print(f"Eu joguei {pc_jogada}")

if escolha == pc_jogada:
    print("Foi um empate!")
elif (escolha == "pedra" and pc_jogada == "tesoura") or \
     (escolha == "papel" and pc_jogada == "pedra") or \
     (escolha == "tesoura" and pc_jogada == "papel"):
    print("Você venceu! Parabéns!")
    
else:
    print("Eu venci! Mais sorte na próxima!")