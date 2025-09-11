#1 #2
class Pessoa:
#     nome = "antonio"
#     idade = 30
#     apresentar = "Olá, meu nome é João e tenho 25 anos."
# voce = Pessoa()
# print(voce)
# print(voce.nome, voce.idade, voce.apresentar, sep="\n")
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentação(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
pessoa1 = Pessoa("Antonio", 30)
pessoa2 = Pessoa("João", 25)

print(f"Nome: {pessoa1.nome}, Idade:{pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")

pessoa1.apresentação()
pessoa2.apresentação()
#3
class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f" {self.marca} {self.modelo} {self.ano}"
Veículo1 = Carro("\nVW", "\nGol", "\n2020")
Veículo2 = Carro("\nGM", "\nCorsa", "\n2012")
Veículo3 = Carro("\nFiat","\nPalio","\n2016")
print(Veículo1)
print(Veículo2)
print(Veículo3)
#4
Veículo4 = Carro("\nVW","\nGol","\n2018")
print("\nAntes")
print(Veículo4)
Veículo4.modelo = "\nGol Copa"
print("\nDepois - Correção modelo")
print(Veículo4)

#5 #6
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O Depósito de {valor} reais realizado na conta do cliente {self.titular} com sucesso.")
        else:
            print("O valor precisa ser maior que 0.")

    def sacar (self,valor):
        if valor <= 0:
            print("O valor precisa ser maior que 0.")
            return True
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return False
        else:
            self.saldo -= valor
            print(f"O Saque de {valor} reais realizado na conta do cliente {self.titular} com sucesso.")
    
conta1 = ContaBancaria("Antonio",0)

conta1.depositar(100)
conta1.sacar(101)

# 7 e 8

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"\n{aluno.nome} foi adicionado(a) à turma.")

    def listar_alunos(self):
        print("\n--- Lista de Alunos na Turma ---")
        if not self.alunos:
            print("Nenhum aluno na turma.")
        else:
            for aluno in self.alunos:
                print(aluno)

aluno1 = Aluno("Antonio", 10)
aluno2 = Aluno("João", 9.5)

minha_turma = Turma()

minha_turma.adicionar_aluno(aluno1)
minha_turma.adicionar_aluno(aluno2)

minha_turma.listar_alunos()

#9
class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

cachorro1 = Cachorro ("bob",2)

print(f"CLASSE {Cachorro.especie}")
print(f"OBJETO {cachorro1.especie}")

