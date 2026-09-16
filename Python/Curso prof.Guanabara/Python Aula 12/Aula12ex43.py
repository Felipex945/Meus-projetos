peso = float(input("Digite seu peso: "))
altura = float(input("Informe sua altura (ex:1.70): "))

imc = peso / (altura ** 2)

print(f"Seu imc é {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso! Cuidado!")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal, continue assim!")
elif 25 <= imc < 30:
    print("Você está no sobrepeso, tome cuidado!")
elif 30 <= imc < 40:
    print("Você está na obesidade! Sua saúde está em risco!")
else:
    print("VOCÊ ESTÁ EM OBESIDADE MÓRBIDA! PROCURE TRATAMENTO IMEDIATAMENTE!")