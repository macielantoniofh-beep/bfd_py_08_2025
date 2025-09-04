#ERROS E EXCEÇÕES
#INDENTIFICAR E SOLUCIONAR

# GERALMENTE ERROS DE SYNTAX - USAR OS CARACTERES QUE TEM QUE SER
# TYPERERROR - EXCEÇÕES - QUE NAA SAO ERROS PROPRIAMENTE DITO

#TRABALHANDO PARALELO COM OUTRAS BIBLIOTECA - TEM ERROS PRÓPRIOS - OLHAR A DOCUMENTAÇÃO E CONSULTA

# TAB - INTENTAÇÃO  

#LIDANDO COM EXCEÇÕES
#TRY, EXCEPT, ELSE, FINALLY, RAISE

#SE USAR O TRY TEM QUE TER O EXCEPT

#É UMA FORMA DE DEVOLVER ALGUMA ORIENTAÇÃO NO ERRO OCORRIDO
#INFORMAÇÕES IMPROCEDENTES, CONGESTIONAMENTO, FALTA DE SINCRONIA DO BANCO DE DADOS, AFINS

#FOTO 18:50

#FINALLY RODA INDEPENDENTE ERRO
#PARA FECHAR A APLICAÇÃO E NAO OCUPA ESPAÇO NA MEMORIA  ----

#RAISE FOTO 19:04

#CRIANDO UM NOVO TIPO DE ERRO
#APLICAÇÃO ESPECIFICAR O ERRO QUE FOI DADO, COM MAIS CLAREZA.

#PARA QUESTAO DO ARQUIVO
#arquivo = open("arquivo.txt","r")
#print(arquivo.read())
#arquivo.close()


# --------------------
#EXERCÍCIO ERROS E EXCEÇÕES

#01 Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.
# try:
#     usuariox = int(input("Informe um número"))
# except ValueError:
#     print("O número precia ser inteiro")
#02 Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro.
# try:
#     user1 = int(input("Informe o Primeiro número"))
#     user2 = int(input("Informe o Segundo número"))
#     mult = user1 * user2
#     print(mult)
# except ValueError:
#     print("Caractere Invalido")
#03 Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
# try:
#     numero = int(input("Digite um número inteiro: "))
# except ValueError:
#     print("Isso não é um número inteiro válido. Por favor, tente novamente.")
# else:
#     print(f"A conversão foi bem-sucedida! Você digitou o número: {numero}")
#04 Implemente um programa que abra um arquivo chamado dados.txt 
# (não precisa existir). Use try e finally para garantir que uma mensagem 
# de "Encerrando programa" seja sempre exibida.
# try:
#     arquivo = open("dados.txt","r")
#     print(arquivo.read())
# except NameError:
#     print("Inexistente")
# finally:
#     print("Encerrando programa")
#     arquivo.close()
# try:
#     with open('dados.txt', 'r') as arquivo:
#         conteudo = arquivo.read()
# except FileNotFoundError:
#     print("O arquivo 'dados.txt' não foi encontrado.")
# finally:
#     print("Encerrando programa.")

#05 Crie uma função dividir(a, b) que lance (raise) uma exceção 
# ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.
# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Não é possível dividir por zero.")
#     return a / b
# print(dividir(10, 1))
# try:
#     print(dividir(10, 0))
# except ZeroDivisionError as e:
#     print(f"Erro: {e}")
#06 Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.
# class IdadeInvalidaError(Exception):
#     pass
# idade = int(input("Informe a idade: "))
# def cadastrar_idade(idade):
#     if idade <= 0:
#         raise IdadeInvalidaError("Não pode ser negativa")
#     else:
#         return f"Sua idade é {idade}"
# print(cadastrar_idade(idade))
#07
# try:
#     user1 = int(input("Informe o Primeiro número "))
#     user2 = int(input("Informe o Segundo número "))
#     div = user1 / user2
#     print(div)
# except ZeroDivisionError:
#     print("segundo número não pode ser zero")
# except ValueError:
#     print("Informe apenas números")
#08 Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:
# try para a conversão,
# else para verificar se é par ou ímpar,
# finally para exibir "Fim do programa".
# try:
#     user1 = int(input("Informe um número "))
# except ValueError:
#     print("Informe apenas números")
# else:
#     if user1 % 2 == 0:
#         print("O número é par!")
#     else:
#         print("O número é ímpar")
# finally:
#     print("Fim do programa!")
#9Crie uma função sacar(saldo, valor) que:
# Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
# Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
# class SaldoInsuficienteError(Exception):
#     if valor > saldo:
#         raise SaldoInsuficienteError(saldo, valor)
#     return saldo - valor