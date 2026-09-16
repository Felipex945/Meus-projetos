valor_casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário mensal? R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30  

print(f'\nPara pagar uma casa de R$ {valor_casa:.2f} em {anos} anos,')
print(f'a prestação será de R$ {prestacao:.2f}.')

if prestacao <= limite:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO! A prestação excede 30% do seu salário.')