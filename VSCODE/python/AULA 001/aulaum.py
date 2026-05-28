# mostrar mensagem 'meu primeiro programa em python'
# Pedir nome e mostrar saudação
# Somar dois números e mostrar resultado 
# calcular média de 3 notas e mostrar resultado
# Mostrar o antecessor e sucessor de um número
# Converter metros para centímetros e milímetros

# mostrar mensagem 'meu primeiro programa em python'
print('Meu primeiro programa em Python')


# Pedir nome e mostrar saudação
nome  = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
print(f"Olá, seja bem-vindo {nome} e a sua idade é {idade} anos.")


# Somar dois números e mostrar resultado 
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = num1 + num2
print(f"O resultado é: {resultado}")

# calcular média de 3 notas e mostrar resultado
aluno = input("Digite o seu nome: ")
serie = int(input("Digite a sua série: "))
nota1 = float(input("Digite a sua n1: "))
nota2 = float(input("Digite a sua n2: "))
nota3 = float(input("Digite a sua PO: "))
resultados = (nota1 + nota2 + nota3) / 3
print(f"O resultado da sua média é: {resultados:.1f}")


# Mostrar o antecessor e sucessor de um número
numero = int(input("Digite um numero: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O numero digitado foi {numero} e o seu antecessor é {antecessor} e o seu sucessor é {sucessor}")


# Converter metros para centímetros e milímetros
# Converter metros para centímetros e milímetros
metros = float(input("Digite um valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"{metros}m equivale a {centimetros:.0f}cm e {milimetros:.0f}mm.")

