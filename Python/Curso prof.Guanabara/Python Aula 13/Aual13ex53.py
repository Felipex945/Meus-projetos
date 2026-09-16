nome = input("Digite uma frase: ") .upper()
sem_espacos = nome.replace(" ", "") 
inverso=""
for letra in range(len(sem_espacos) -1, -1, -1):
    inverso += sem_espacos[letra]

print(f"O inverso de {sem_espacos} é {inverso}.")

if inverso == sem_espacos:
    print("Essa frase é um palíndromo.")
else:    
    print("Essa frase não é um palíndromo.")