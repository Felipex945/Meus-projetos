n1 = float(input("Digite um número: "))
n2 = float(input("Digite o segundo: "))
somar = n1 + n2
multi = n1 * n2
maior_valor = max(n1, n2)
entrada = 0

while entrada != 5:
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair")
    entrada = int(input("Digite uma das opções: "))
    if entrada == 1:
        print(f"A soma do número {n1} + {n2} = {somar}")
    elif entrada == 2:
        print(f"A multiplicação entre os número {n1} e {n2} é {multi}")
    elif entrada == 3:
        print(f"O maior número entre os dois é {maior_valor}")
    elif entrada == 4:
        n1 = float(input("Digite um número novamente: "))
        n2 = float(input("Digite o segundo: "))
print("Finalizado!")