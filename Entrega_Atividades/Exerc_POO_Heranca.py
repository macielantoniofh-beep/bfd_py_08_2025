#1Crie uma classe Usuario com atributos nomee email. Depois, crie uma aula Clienteque herde de Usuario. Crie uma instância de um cliente e acesse todos os atributos.
# e 2# Implemente um método exibir_informacoes()na classe Usuarioe herde esse método em Cliente. Mostre como chamar o método herdado a partir de um objeto Cliente.
class Usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        return f"Exibindo informações"
class Cliente(Usuario):
    def __init__(self,nome,email,compras):
        super().__init__(nome,email)
        self.compras = compras
    def __str__(self):
        return f"O usuario {self.nome}, tem o contato de email {self.email}, e também é cliente com a frequencia de {self.compras} compras efetuadas."

user1 = Cliente("Antonio","antonio@tom.com",10)
print(user1)
user1.exibir_informacoes()




# 3Na classe Usuario, crie um método saudacao()que retorna "Olá, usuário". Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". Mostre como funciona a chamada.
# 4Na classe Cliente, adicione ou atributo saldo. Adicione um método construtor em Clienteque inicialize também os atributos de Usuariouso super().
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def saudacao(self):
        return f"Olá, usuário {self.nome}."

class Cliente(Usuario):
    def __init__(self, nome, saldo):
        super().__init__(nome)
        self.saldo = saldo

    def saudacao(self):
        return f"Olá, cliente {self.nome}."


usuario1 = Usuario("Antonio")
print(f"Chamada do método na classe Usuario: {usuario1.saudacao()}")

cliente1 = Cliente("Fred", 500)
print(f"Chamada do método sobrescrito na classe Cliente: {cliente1.saudacao()}")

print(f"Saldo do cliente {cliente1.nome}: R${cliente1.saldo:.2f}")

# 5Crie uma classe Funcionarioque herda de Usuarioe, em seguida, crie uma classe Gerenteque herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.
class Funcionario(Usuario):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self.cargo = cargo

    def saudacao(self):
        return f"Olá, funcionário {self.nome}."

class Gerente(Funcionario):
    def __init__(self, nome, cargo, setor):
        super().__init__(nome, cargo)
        self.setor = setor

    def saudacao(self):
        return f"Olá, gerente {self.nome}."

gerente_departamento = Gerente("Raissa", "Gerente de Projeto", "TI")

print(f"Nome do gerente: {gerente_departamento.nome}")
print(f"Cargo: {gerente_departamento.cargo}")
print(f"Setor: {gerente_departamento.setor}")

print(gerente_departamento.saudacao())

# 6Crie uma classe Autenticacao com um método login(). Crie outra classe Permissaocom um método verificar_permissao(). Em seguida, crie uma aula Administradorque herda de ambas. Como usar os métodos herdados?
# 7Usando o exemplo anterior, adicione um método status()em Autenticacaoe também em Permissao. Se a classe Administradorherda das duas, qual versão status()será chamada? Use Administrador.__mro__para mostrar a ordem.

class Autenticacao:
    def login(self):
        return "Usuário autenticado."

class Permissao:
    def verificar_permissao(self):
        return "Permissão concedida."

class Administrador(Autenticacao, Permissao):
    pass

admin = Administrador()
print(admin.login())
print(admin.verificar_permissao())

class Autenticacao:
    def login(self):
        return "Usuário autenticado."

    def status(self):
        return "Status: Autenticado"

class Permissao:
    def verificar_permissao(self):
        return "Permissão concedida."
    
    def status(self):
        return "Status: Permissão"

class Administrador(Autenticacao, Permissao):
    pass


admin2 = Administrador()
print(admin2.status())

print(Administrador.__mro__)

