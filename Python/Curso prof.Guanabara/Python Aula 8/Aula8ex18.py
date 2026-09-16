import math
angulo = int( input("Digite o valor do ângulo: " ) )
angulo_rad = math.radians(angulo)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
print("O seno desse ângulo é {:.2f}, o cosseno é {:.2f} e o tangente é {:.2f}".format (seno, cosseno, tangente))
