real = float( input("Digite seu dinheiro em reais: ") )
dolar = real / 3.27
if dolar <= 1:
	print("Você pode comprar {} dólar".format(dolar))
else:
    print("Você pode comprar {} dólares".format(dolar))