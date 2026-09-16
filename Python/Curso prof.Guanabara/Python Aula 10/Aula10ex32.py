ano = int( input("Digite o ano: ") )
ano_bissexto = ano % 4
if ano_bissexto == 0:
    print("Esse ano é bissexo!")
else:
    print("Esse ano não é bissexto!")