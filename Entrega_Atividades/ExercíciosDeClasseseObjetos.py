#1 #2
class Pessoa:
    nome = "antonio"
    idade = 30
    apresentar = "Olá, meu nome é João e tenho 25 anos."
voce = Pessoa()
print(voce)
print(voce.nome, voce.idade, voce.apresentar, sep="\n")

#FALTA COLOCAR FUNÇÃO DE PARA POR O NOME

#3
class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f" {self.marca} {self.modelo} {self.ano}"
Veículo = Carro("\nVW", "\nGol", 2020)
print(Veículo)

