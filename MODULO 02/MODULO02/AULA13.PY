# Herança

#1 Criar pessoa com suas características e uma casse funcionário que herde pessoa.
class Pessoa:
    def __init__(self,nome,idade,transporte):
        self.nome = nome
        self.idade = idade
        self.transporte = transporte
class Funcionário(Pessoa):
    def __init__(self,matricula,função):
        super().__init__(nome,idade,transporte)
        self.matricula = matricula
        self.função = função

pessoa1 = Funcionário("Antonio",30,"uber","111-1","Gerente")

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.transporte)
print(pessoa1.matricula)
print(pessoa1.função)



#2 VocÊ tem uma empresa que usa computadores padronizados, contudo o departamaneto de IA, precisa de uma placa de video. ENtão, 
# crie uma classe computador, que tenha modelo, processador, quantidade de memoria e departamento.
# E uma classe que herde as características da Classe computador,mas adicione a placa de video.