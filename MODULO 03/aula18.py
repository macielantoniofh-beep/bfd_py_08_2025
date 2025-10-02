'''
Classe abstrata
Interfaces

01 classe abstrata Pessoa - com metodos Falar, Andar e Comer
subclasses Funcionário e Aluno - herdando métodos Pessoa
Instancie um objeto para cada subclasse

02 Usando o anterior, converta a classe Pessoa em uma interface

'''

#01
from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        print("Falando")
    @abstractmethod
    def andar(self):
        print("Andando")
    @abstractmethod
    def comer(self):
        print("comendo")
class Funcionario(Pessoa):
    def falar(self):
        return super().falar()
    def andar(self):
        return super().andar()
    def comer(self):
        return super().comer()
class Aluno(Funcionario):
    ...

antonio = Aluno()
antonio.falar()
antonio.andar()
antonio.comer()

#2
from abc import ABC, abstractmethod
class Pessoa(ABC):
    @abstractmethod
    def falar(self):
        ...
    @abstractmethod
    def andar(self):
        ...
    @abstractmethod
    def comer(self):
        ...
class Funcionario(Pessoa):
    def falar(self):
        print("Falando")
    def andar(self):
        print("Andando")
    def comer(self):
        print("Comendo")
class Aluno(Funcionario):
    def falar(self):
        return super().falar()
    def andar(self):
        return super().andar()
    def comer(self):
        return super().comer()

antonio = Aluno()
antonio.falar()
antonio.andar()
antonio.comer()

'''
SOLID  **** determinação das classes - separação conforme
5 principios 


'''
