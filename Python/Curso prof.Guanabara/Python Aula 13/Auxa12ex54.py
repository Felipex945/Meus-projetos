atual = 2026
totmaior = 0
totmenor = 0

for nascimento in range(1, 8):
    pess = int(input(f"Qual o ano de nascimento da {nascimento} pessoa? "))
    idade = atual - pess
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1

print(f"{totmaior} são maiores de idade e {totmenor} são menores de idade!")