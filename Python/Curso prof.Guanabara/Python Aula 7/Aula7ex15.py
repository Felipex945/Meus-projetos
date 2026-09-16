valor1 = float ( input("Digite quantos dias você alugou: ") )
valor2 =  float ( input("Digite quantos km foram rodados: ") )
carro = valor1 * 60
km = valor2 * 45
soma = carro + km
print("O preço do carro em dias é {} e em km é {}. O total a pagar é {}".format(carro, km, soma))
