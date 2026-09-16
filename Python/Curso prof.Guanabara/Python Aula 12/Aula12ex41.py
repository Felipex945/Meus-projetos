idade = float(input("Informe sua idade: "))

if idade <= 9:
    print("Sua categoria é mirim!")
elif 9 < idade <= 14:
    print("Sua categoria é infantil")
elif 14 < idade <= 19:
    print("Sua categoria é júnior")
elif 19 < idade <= 20:
    print("Sua categoria é sênior")
else:
    print("Sua categoria é master")