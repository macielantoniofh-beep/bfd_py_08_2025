#1
def saudacao():
  print("Olá, bem-vindo ao Python!")
saudacao()

#2
def dobro(num1):
  return num1*2
resultado = dobro(7)
print(resultado)

#3
def soma(carros, motos):
  return carros + motos
resultado = soma(10, 20)
print(f"A soma dos veículos é: {resultado}")

#4
def mensagem(nome="visitante"):
  print(f"Olá, {nome}!")
mensagem("antonio")
mensagem()

#5
def operacoes(num1, num2):
  soma = num1 + num2
  subtracao = num1 - num2
  multiplicacao = num1 * num2
  return soma, subtracao, multiplicacao
result_operacoes = operacoes(6, 5)
s, sub, mult = operacoes(6, 5)
print(f"Resultado: {result_operacoes}")
print(f"Soma: {s}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")

#6
def media(*numeros):
  if not numeros:
    return 0
  return sum(numeros) / len(numeros)
print(f"A média é: {media(2, 4, 6)}")
print(f"A média é: {media(2, 4, 6, 8, 10)}")
print(f"A média é: {media(2, 4, 6, 8, 10, 12, 14)}")

#7
def dados_pessoais(**dados):
  for chave, valor in dados.items():
    print(f"{chave.replace('_', '').title()}: {valor}")
dados_pessoais(nome="antonio", idade=30, cidade="Jaboatão", bairro="Centro")

#8
def calculadora():
  def somar(a, b):
    return a + b
  def subtrair(a, b):
    return a - b
  def multiplicar(a, b):
    return a * b
  def dividir(a, b):
    return a / b
  operacao = input("Escolha a operação (+, -, *, /): ")
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  if operacao == '+':
    print(somar(num1, num2))
  elif operacao == '-':
    print(subtrair(num1, num2))
  elif operacao == '*':
    print(multiplicar(num1, num2))
  elif operacao == '/':
    print(dividir(num1, num2))
  else:
    print("Operação inválida.")
calculadora()

#9
def aplicar_operacao(num1, num2, operacao):
  return operacao(num1, num2)
def somar(a, b):
  return a + b
def multiplicar(a, b):
  return a * b
result_soma = aplicar_operacao(2, 3, somar)
result_multiplicacao = aplicar_operacao(2, 3, multiplicar)
print(f"A soma é : {result_soma}")
print(f"A multiplicação é : {result_multiplicacao}")