'''
1 Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

2 Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

3 Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.

4 Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

5 Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.

6 Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.
'''
#1
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

class Livro:
    def __init__(self, nome: str, ano: int):
        self.nome = nome
        self.ano = ano
    
    def posse_livro(self, pessoa: Pessoa):
        print(f"A pessoa {self.nome}, esta em posse do livro {pessoa.nome} do {pessoa.idade}")



pes1 = Pessoa("João", 20)
liv1 = Livro("livro a", "2010",)
liv2 = Livro("livro b", "2012",)

pes1.posse_livro(liv1)
pes1.posse_livr(liv2)


#2

