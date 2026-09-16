import random
nomes = input("Digite os nomes do alunos: ").split ()
random.shuffle(nomes)
print("Os nomes sorteados foram {}".format(nomes))