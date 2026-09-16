km = float(input("Digite quantos kilômeros foram rodados: ") )
ate_200km = km * 0.5
ultrapasso = km * 0.45
if km > 200:
    print(f"O valor da viagem foi: R${ultrapasso:.2f}")
else:
    print(f"O valor da viagem foi: R${ate_200km:.2f}")