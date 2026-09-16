import random
alunos = input("Digite o nome dos alunos: ") .split()
aleatorio = random.choice(alunos)
print("O nome sorteado foi: {}".format(aleatorio))
