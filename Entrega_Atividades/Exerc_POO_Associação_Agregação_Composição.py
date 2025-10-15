'''
1 Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.

2 Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

3 Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.Departamento deve agregar funcionários já criados.

4 Crie as classes Time e Jogador. Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.

5 Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto.

6 Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.). Cada Comodo deve ser criado dentro da Casa.
'''
#
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Livro: '{self.titulo}' por {self.autor}"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.livro_favorito = None 

    def definir_livro_favorito(self, livro):
        self.livro_favorito = livro
        print(f"{self.nome} agora tem o livro '{livro.titulo}' como favorito.")

    def __str__(self):
        favorito = self.livro_favorito.titulo if self.livro_favorito else "Nenhum"
        return f"Pessoa: {self.nome} | Livro Favorito: {favorito}"

print("--- 1. Associação (Pessoa e Livro) ---")
livro1 = Livro("1984", "George Orwell")
pessoa1 = Pessoa("Alice")

pessoa1.definir_livro_favorito(livro1)

print(livro1)
print(pessoa1)



#

class Onibus:
    def __init__(self, placa, rota):
        self.placa = placa
        self.rota = rota

    def movimentar(self, destino):
        return f"Ônibus de placa {self.placa} (Rota: {self.rota}) está indo para {destino}."

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def ir_para_universidade(self, onibus: Onibus):
        movimento = onibus.movimentar("a Universidade")
        return f"{self.nome} (Matrícula {self.matricula}) embarcou no ônibus. {movimento}"


onibus_da_linha_100 = Onibus("ABC-1234", "Linha 100")
aluno_joao = Aluno("João", "10")

mensagem_viagem = aluno_joao.ir_para_universidade(onibus_da_linha_100)
print(mensagem_viagem)

#
class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome} ({self.cargo})"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []  

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
        print(f"-> {funcionario.nome} adicionado ao departamento {self.nome}.")

    def listar_funcionarios(self):
        print(f"\n--- Funcionários do Departamento de {self.nome} ({len(self.funcionarios)}): ---")
        for func in self.funcionarios:
            print(f"- {func}")

func1 = Funcionario("Maria", "Analista")
func2 = Funcionario("Carlos", "Gerente")

dep_ti = Departamento("Tecnologia da Informação")
dep_ti.adicionar_funcionario(func1)
dep_ti.adicionar_funcionario(func2)
dep_ti.listar_funcionarios()

del dep_ti
print(f"\nApós deletar o Departamento: func1 ainda existe? Sim, é: {func1}")

#

class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"Nome: {self.nome}, Posição: {self.posicao}"

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = [] 

    def contratar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

    def mostrar_elenco(self):
        print(f"\n--- Elenco do Time {self.nome} ({len(self.jogadores)} jogadores) ---")
        for jogador in self.jogadores:
            print(f"- {jogador}")

j1 = Jogador("alan", "Ataque")
j2 = Jogador("raul", "Defesa")

time_futebol = Time("sport")
time_futebol.contratar_jogador(j1)
time_futebol.contratar_jogador(j2)
time_futebol.mostrar_elenco()

#

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        print(f"--> Motor {self.tipo} CRIADO.")

    def ligar(self):
        return "Vrummm! Motor ligado."

    def __del__(self):
        print(f"--> Motor {self.tipo} DESTRUÍDO.")

class Carro:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor) 
        print(f"Carro {self.modelo} CRIADO.")

    def ligar_carro(self):
        return f"{self.modelo}: {self.motor.ligar()}"

    def __del__(self):
        print(f"Carro {self.modelo} DESTRUÍDO.")

meu_carro = Carro("Ford", "Fusion", "2.0 Turbo")
print(meu_carro.ligar_carro())

del meu_carro


#

class Comodo:
    def __init__(self, nome, tamanho_m2):
        self.nome = nome
        self.tamanho_m2 = tamanho_m2
        print(f"--> Cômodo '{self.nome}' ({self.tamanho_m2}m²) criado.")

    def __str__(self):
        return f"Cômodo: {self.nome} ({self.tamanho_m2}m²)"
        
    def __del__(self):
        print(f"--> Cômodo '{self.nome}' DESTRUÍDO.")


class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.sala = Comodo("Sala de Estar", 30)
        self.cozinha = Comodo("Cozinha", 15)
        self.quartos = [Comodo("Quarto Principal", 18), Comodo("Quarto Hóspedes", 12)]
        print(f"Casa no endereço '{self.endereco}' CRIADA.")

    def listar_comodos(self):
        print(f"\nComodos da Casa em {self.endereco}:")
        print(f"- {self.sala}")
        print(f"- {self.cozinha}")
        for q in self.quartos:
             print(f"- {q}")

    def __del__(self):
        print(f"Casa no endereço '{self.endereco}' DESTRUÍDA.")


minha_casa = Casa("Rua das Flores, 100")
minha_casa.listar_comodos()

del minha_casa