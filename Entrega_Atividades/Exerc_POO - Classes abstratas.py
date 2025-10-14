'''
Definição de classe abstrata

Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. Mostre o uso criando objetos e chamando o método falar().

Proibição de instanciamento

Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.

Múltiplos métodos abstratos

Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro(). Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.

Herança parcial

Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). Depois, crie uma subclasse Carro que implemente apenas o método mover(). O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

print(" 1. Definição de Classe Abstrata")
cachorro1 = Cachorro()
gato1 = Gato()

print(f"O cachorro fala: {cachorro1.falar()}")
print(f"O gato fala: {gato1.falar()}")

try:
    animal_generico = Animal() # Tenta criar uma instância de Animal
except TypeError as e:
    print(f"Erro gerado ao tentar instanciar Animal diretamente: {e}")

# 
class FormaGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        pass
        
    @abstractmethod
    def perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


meu_retangulo = Retangulo(largura=5, altura=10)

print(f"Largura: {meu_retangulo.largura}, Altura: {meu_retangulo.altura}")
print(f"Área do Retângulo: {meu_retangulo.area()}")
print(f"Perímetro do Retângulo: {meu_retangulo.perimetro()}")

#
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass
        
    @abstractmethod
    def parar(self):
        pass

class CarroParcial(Transporte):
    def mover(self):
        return "Carro se movendo com as rodas."

try:
    carro_parcial = CarroParcial()
except TypeError as e:
    print(f"Erro gerado ao tentar instanciar CarroParcial: {e}")