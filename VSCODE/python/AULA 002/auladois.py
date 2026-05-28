# pode votar? (Obrigatório, facultativo, não pode)
# Número par ou ímpar
# Número positivo, negativo ou zero
# Calculadora simples, tendo mais, menos, multiplicação e divisão
# Sistema de desconto

# pode votar? (Obrigatório, facultativo, não pode)
idade = int(input("Digite a sua idade: "))
if idade >= 60:
    print("Voto Não obrigatório")
elif idade == 16 or idade == 17:
    print("Voto facultativo")
elif idade >= 18:
    print("Voto obrigatório")
else:
    print("Você é menor de idade")


# Número par ou ímpar
num = int(input("Digite um numero: "))
if num % 2 == 0:
    print("Numero par")
else:
    print("Numero ímpar")


# Número positivo, negativo ou zero
numero = int(input("Digite um numero:"))
if numero > 0:
    print("numero postivo")
elif numero < 0:
    print("Numero negativo")
else:
    print("Numero zero, inválido")


# Calculadora simples, tendo mais, menos, multiplicação e divisão
numb1 = int(input("Digite o primeiro número: "))
numb2 = int(input("Digite o segundo número: "))
print("Escolha qual operação será usado: + , - , * , /")
operador = input("Digite qual operador lógico usar: ")
if operador == "+":
    resultado = numb1 + numb2
    print(f"O resultado da conta {numb1} {operador} {numb2} é igual a {resultado}")
elif operador == "-":
    resultado = numb1 - numb2
    print(f"O resultado da conta {numb1} {operador} {numb2} é igual a {resultado}")
elif operador == "*":
    resultado = numb1 * numb2
    print(f"O resultado da conta {numb1} {operador} {numb2} é igual a {resultado}")
elif operador == "/":
    resultado = numb1 / numb2
    print(f"O resultado da conta {numb1} {operador} {numb2} é igual a {resultado}")
else:
    print("Operador inválido!!")


# Sistema de desconto
valor = float(input("Digite o valor da compra: "))
if valor >= 100:
    desconto = (100 * 8) / 100
    final = valor - desconto
elif valor >= 250:
    desconto = (250 * 12) / 100
    final = valor - desconto
elif valor >= 750:
    desconto = (750 * 15) / 100
    final = valor - desconto
else:
    print("Valor inválido")
print(f"O valor da sua compra de {valor:.2f} reais com desconto será de: {final:.2f} reais")