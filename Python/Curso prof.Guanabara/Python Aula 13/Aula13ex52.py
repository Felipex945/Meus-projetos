import math
num = int(input("Digite um número inteiro número: "))
tot = 0
for c in range(1, int(math.sqrt(num)) + 1):
    if num % c == 0:
        print("\033[33m", end="")
        tot += 1
    else:
        print("\033[31m", end="")
    print('{}'.format(c) , end=' ')
print(f'\n\033[mO número {num} foi dividido {tot} vezes')
if tot == 2:
    print('E por isso que ele é primo')
else:
    print('Por isso que ele não é primo')