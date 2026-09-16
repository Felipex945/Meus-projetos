import math
cateto = float( input("Digite o valor do cateto: ") )
catet = float ( input("Digite o valor do segundo: "))
hipotenusa = (catet ** 2) + (cateto ** 2)
valorfinal = math.sqrt(hipotenusa)
print("A hipotenusa é {:.2f}".format(valorfinal))
