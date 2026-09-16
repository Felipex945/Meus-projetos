num = float( input("Digite o primeiro número número: ") )
num2 = float( input("Digite o segundo:") )
num3 = float( input("O terceiro: ") )

maior = num
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

menor = num
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")