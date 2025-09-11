# #1 #2
# class Pessoa:
# #     nome = "antonio"
# #     idade = 30
# #     apresentar = "Olá, meu nome é João e tenho 25 anos."
# # voce = Pessoa()
# # print(voce)
# # print(voce.nome, voce.idade, voce.apresentar, sep="\n")
#     def __init__(self,nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def apresentação(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
# pessoa1 = Pessoa("Antonio", 30)
# pessoa2 = Pessoa("João", 25)

# print(f"Nome: {pessoa1.nome}, Idade:{pessoa1.idade}")
# print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")

# pessoa1.apresentação()
# pessoa2.apresentação()
# #3
# class Carro:
#     def __init__(self,marca, modelo,ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#     def __str__(self):
#         return f" {self.marca} {self.modelo} {self.ano}"
# Veículo1 = Carro("\nVW", "\nGol", "\n2020")
# Veículo2 = Carro("\nGM", "\nCorsa", "\n2012")
# Veículo3 = Carro("\nFiat","\nPalio","\n2016")
# print(Veículo1)
# print(Veículo2)
# print(Veículo3)
# #4
# Veículo4 = Carro("\nVW","\nGol","\n2018")
# print("\nAntes")
# print(Veículo4)
# Veículo4.modelo = "\nGol Copa"
# print("\nDepois - Correção modelo")
# print(Veículo4)

# #5 #6
# class ContaBancaria:
#     def __init__(self, titular, saldo=0):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, valor):
#         if valor > 0:
#             self.saldo += valor
#             print(f"O Depósito de {valor} reais realizado na conta do cliente {self.titular} com sucesso.")
#         else:
#             print("O valor precisa ser maior que 0.")

#     def sacar (self,valor):
#         if valor <= 0:
#             print("O valor precisa ser maior que 0.")
#             return True
#         elif valor > self.saldo:
#             print("Saldo insuficiente para realizar o saque.")
#             return False
#         else:
#             self.saldo -= valor
#             print(f"O Saque de {valor} reais realizado na conta do cliente {self.titular} com sucesso.")
    
# conta1 = ContaBancaria("Antonio",0)

# conta1.depositar(100)
# conta1.sacar(101)

# # 7 e 8

# class Aluno:
#     def __init__(self, nome, nota):
#         self.nome = nome
#         self.nota = nota

#     def __str__(self):
#         return f"Aluno: {self.nome} - Nota: {self.nota}"

# class Turma:
#     def __init__(self):
#         self.alunos = []

#     def adicionar_aluno(self, aluno):
#         self.alunos.append(aluno)
#         print(f"\n{aluno.nome} foi adicionado(a) à turma.")

#     def listar_alunos(self):
#         print("\n--- Lista de Alunos na Turma ---")
#         if not self.alunos:
#             print("Nenhum aluno na turma.")
#         else:
#             for aluno in self.alunos:
#                 print(aluno)

# aluno1 = Aluno("Antonio", 10)
# aluno2 = Aluno("João", 9.5)

# minha_turma = Turma()

# minha_turma.adicionar_aluno(aluno1)
# minha_turma.adicionar_aluno(aluno2)

# minha_turma.listar_alunos()

# #9
# class Cachorro:
#     especie = "Canis familiaris"

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# cachorro1 = Cachorro ("bob",2)

# print(f"CLASSE {Cachorro.especie}")
# print(f"OBJETO {cachorro1.especie}")

# REVISAO OBJETO


#ATRIBUTO PRIVADO - ACESSA SOMENTE DENTRO DA FUNÇÃO  PARA PRIVADO __ SO NA FRENTE DA FUNÇÃO
#SETTERS - FUNÇÃO DEFINIR VALOR
#GETTERS - PEGAR O VALOR

# def get_saldo(self):
#     return self.__saldo
# def set_saldo(self,valor):
#     if valor < 0:
#         print("Saldo não pode ser negativo")
#     else:
#         self.__saldo = valor
# se deixou privado e nao precisa alterar a informação, nao precisa da ferramenta.
#encapsulamento - protegendo os dados fora da função

#UML - BÁSICO

#UML DIAGRAM EDITOR
#drauml.net/draw
#+ informação publica
# - Informação privada
#void é vazio - nao vai retornar nada




#1 NA CLASSE, CONTABANCARIA, CONVERTA SALDO PARA UMA ATRIBUTO PRIVADO. 
#CRIE UM METODO SETTER E UM GETTER PARA ACESSAR E MODIFICAR ESSE ATRIBUTO.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
        self.operações = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"O Depósito de {valor} reais realizado na conta do cliente {self.titular} com sucesso.")
        else:
            print("O valor precisa ser maior que 0.")

    def sacar (self,valor):
        if valor <= 0:
            print("O valor precisa ser maior que 0.")
            return True
        elif valor > self.__saldo:
            print("Saldo insuficiente para realizar o saque.")
            return False
        else:
            self.__saldo -= valor
            print(f"O Saque de {valor} reais realizado na conta do cliente {self.titular} com sucesso.")
    def extrato(self):
        for operacao in self.operações:
            print(operacao)
        print(f"O saldo:{self.__saldo}")

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,valor):
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
            self.__saldo = valor

conta1 = ContaBancaria("Antonio",0)

conta1.depositar(100)
conta1.sacar(99)
conta1.extrato()

#2 CRIE UMA CLASSE, PESSOA, QUE TENHA OS ATRIBUTOS: NOME, DATA DE NASCIMENTO, CPF, IDENTIDADE. 
# DEIXE OS ATRIBUTOS CPF E IDENTIDADE COMO PRIVADO E MONTE OS MÉTODOS SETTERS E GETTER PARA 
# ACESSAR E EDITAR OS VALORES

class Pessoa:
    def __init__(self,Nome,Data_de_Nascimento,CPF,RG):
        self.Nome = Nome
        self.Data_de_Nascimento = Data_de_Nascimento
        self.__CPF = CPF
        self.__RG = RG
    def __str__(self):
        return f"Nome: {self.Nome}\n Data de Nascimento: {self.Data_de_Nascimento}\n CPF: {self.__CPF}\n RG:{self.__RG}"

    def get_CPF(self):
        return self.__CPF
    def get_RG(self):
        return self.__RG
    def set_CPF(self,numero):
        self.__CPF = numero
    def set_RG(self,numero):
        self.__RG = numero

pessoa1 = Pessoa("José","25/12/2000","001.002.004-20","10.345.234")
pessoa1.get_CPF()
pessoa1.get_RG()
pessoa1.set_CPF("000.004.004-50")
pessoa1.set_RG("11.345.234")
print(pessoa1)
