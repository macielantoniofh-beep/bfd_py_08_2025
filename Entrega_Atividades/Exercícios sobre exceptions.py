#01 Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.
try:
    usuariox = int(input("Informe um número"))
except ValueError:
    print("O número precia ser inteiro")
# 02 Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.
try:
    user1 = int(input("Informe o Primeiro número"))
    user2 = int(input("Informe o Segundo número"))
    mult = user1 * user2
    print(mult)
except ValueError:
    print("Caractere Invalido")
#03 Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Isso não é um número inteiro válido. Por favor, tente novamente.")
else:
    print(f"A conversão foi bem-sucedida! Você digitou o número: {numero}")
#04 Implemente um programa que abra um arquivo chamado dados.txt 
# (não precisa existir). Use try e finally para garantir que uma mensagem 
# de "Encerrando programa" seja sempre exibida.
try:
    arquivo = open("dados.txt","r")
    print(arquivo.read())
except NameError:
    print("Inexistente")
finally:
    print("Encerrando programa")
    arquivo.close()
try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo 'dados.txt' não foi encontrado.")
finally:
    print("Encerrando programa.")

#05 Crie uma função dividir(a, b) que lance (raise) uma exceção 
# ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b
print(dividir(10, 1))
try:
    print(dividir(10, 0))
except ZeroDivisionError as e:
    print(f"Erro: {e}")
#06 Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.
class IdadeInvalidaError(Exception):
    pass
idade = int(input("Informe a idade: "))
def cadastrar_idade(idade):
    if idade <= 0:
        raise IdadeInvalidaError("Não pode ser negativa")
    else:
        return f"Sua idade é {idade} anos"
print(cadastrar_idade(idade))
#07
try:
    user1 = int(input("Informe o Primeiro número "))
    user2 = int(input("Informe o Segundo número "))
    div = user1 / user2
    print(div)
except ZeroDivisionError:
    print("segundo número não pode ser zero")
except ValueError:
    print("Informe apenas números")
#08 Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
# try para a conversão,
# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".
try:
    user1 = int(input("Informe um número "))
except ValueError:
    print("Informe apenas números")
else:
    if user1 % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar")
finally:
    print("Fim do programa!")
#9Crie uma função sacar(saldo, valor) que:
# Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
# Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
class SaldoInsuficienteError(Exception):
    pass
def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente!")
    return saldo - valor
saldo_atual = 100
valor_saque = 50
try:
    novo_saldo = sacar(saldo_atual, valor_saque)
    print(f"Saque realizado com sucesso. Novo saldo: R${novo_saldo:.2f}")
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")