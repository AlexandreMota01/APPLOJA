# Sistema de Descontos Loja OnLine
# Autor : Alexandre Mota

# Entrada solicita que o usuário digite o valor da compra
# float () para numeros decimais


valor = float(input("Digite o Valor da Compra: "))

# Processamento

# Veriica se o valor é menor ou igual a R$ 200
if valor <= 200:

    # Define o desconto de 5% e exibe a mensagem
    desconto = 0.05
    print ("Você tem um desconto de 5%")

# Verifica se o valor é maior que R$ 200 e menor que R$ 300

elif valor < 300:

    # Define o desconto de 10% e exibe a mensagem
    desconto = 0.10
    print ("Você tem um desconto de 10%")

# Verifica se o valor é maior ou igual a R$ 300
else:
    # Define o desconto de 15% e exibe a mensagem
    desconto = 0.15 
    print ("Você tem um desconto de 15%")


# Cálculo do valor final da compra com desconto
valor_final = valor - (valor * desconto)


# Saída exibe o valor final da compra com desconto
print (f"O valor final da compra é: R$ {valor_final:.2f}")