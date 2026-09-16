num = int(input("Digite o número: "))
opcao = int(input("Digite 1 para conversão binária, 2 para octal ou 3 para hexadecimal: "))
binário = bin(num)
octal = oct(num)
hexadecimal = hex(num)

if opcao == 1:
     print(f"O número convertido para binário é {binário}")
if opcao == 2:
     print(f"Esse número convertido para octal é {octal}")
if opcao == 3:
     print(f"Esse número convetido para hexadecimal é {hexadecimal}")