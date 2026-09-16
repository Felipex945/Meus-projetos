
preco_original = float(input("Preço do produto: R$ "))

print("""
FORMAS DE PAGAMENTO
[ 1 ] À vista (dinheiro ou cheque)
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão
""")

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = preco_original * 0.90  
    print(f"Sua compra de R${preco_original:.2f} vai custar R${total:.2f} com 10% de desconto.")

elif opcao == 2:
    total = preco_original * 0.95  
    print(f"Sua compra de R${preco_original:.2f} vai custar R${total:.2f} com 5% de desconto.")

elif opcao == 3:
    total = preco_original
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.")
    print(f"O valor total permanece R${total:.2f}.")

elif opcao == 4:
    total = preco_original * 1.20  
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print(f"Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS.")
    print(f"Sua compra de R${preco_original:.2f} vai custar R${total:.2f} no final.")

else:
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")