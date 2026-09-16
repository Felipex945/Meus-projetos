a = float(input("Digite o valor do primerio lado: "))
b = float(input("Informe o valor do segundo: "))
c = float(input("O terceiro: "))
  
if (a + b > c) and (a + c > b) and (b + c > a):
    print("É possível formar um triângulo com essas medidas!")
    
    if a == b == c:
     print("Esse triângulo é equilátero!")
    elif a == b or b == c or a == c:
     print("Esse triângulo é isósceles")
    else:
     print("Esse triângulo é escaleno!")


else:
    print("Não é possível formar um triângulocom as medidas fornecidas!")