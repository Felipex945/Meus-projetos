pesos = []
for c in range(1, 6):
    peso = float(input(f"Peso da {c}ª pessoa: "))
    pesos+=[peso]
print(f"O maior peso foi: {max(pesos)}")
print(f"O menor peso foi: {min(pesos)}")