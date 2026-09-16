salario = float( input("Digite o seu salário: ") )
salario_maior = salario * (10 / 100)
salario_menor = salario * (15 / 100)

salario_definido = salario_maior + salario
salario_definido2 =  salario_menor + salario

if salario > 1250:
    print(f"Com aumento de 10% seu salário foi para R${salario_definido:.2f}")
else:
    print(f"Com aumento de 15% seu salário foi para R${salario_definido2:.2f}")