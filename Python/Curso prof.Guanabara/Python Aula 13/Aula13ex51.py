print("===================")
print("10 termos de uma PA")
print("===================")


termo = int(input("Digite o primerio termo: "))
razao = int(input("Digite a razão: "))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print(f"{c}", end=' -> ')
print("Acabou")