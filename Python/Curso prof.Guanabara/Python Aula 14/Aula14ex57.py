sexo = input("Digite seu sexo [M/F]: ").strip().upper()

while sexo != "M" and sexo != "F":
    print("Opção inválida! Por favor, digite apenas M ou F.")
    sexo = input("Digite seu sexo [M/F]: ").strip().upper()

print(f"Sexo {sexo} registrado com sucesso. Obrigado!")