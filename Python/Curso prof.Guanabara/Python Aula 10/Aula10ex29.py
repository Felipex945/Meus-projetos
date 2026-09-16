from time import sleep
vel = float( input("Digite a quantos km p/h você está indo: ") )
km = vel - 80
multa = km * 7
if vel > 80:
    print("Você está acima da velocidade permitida!")
    print("CALCULANDO MULTA...")
    sleep(2)
    print(f"O valor da multa a ser pago é R${multa:.2f}")
else:
    print("Você está dentro do limite! Boa viagem!")