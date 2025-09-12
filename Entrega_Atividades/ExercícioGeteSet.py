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
        return f" Nome: {self.Nome}\n Data de Nascimento: {self.Data_de_Nascimento}\n CPF: {self.__CPF}\n RG:{self.__RG}"

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