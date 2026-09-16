a = float ( input("Informe o primerio lado: ") )
b = float ( input("Informe o segundo: ") )
c = float ( input("Informe o último: ") )

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Sim, é possível formar um triângulo com essas medidas.")
else:
    print("Não, é impossível formar um trângulo com essas medidas.")