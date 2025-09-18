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


# 5Crie uma classe Funcionarioque herda de Usuarioe, em seguida, crie uma classe Gerenteque herda de Funcionario. Mostre como instanciar um gerente e acessar seus atributos.


# 6Crie uma classe Autenticacaocom um método login(). Crie outra classe Permissaocom um método verificar_permissao(). Em seguida, crie uma aula Administradorque herda de ambas. Como usar os métodos herdados?


# 7Usando o exemplo anterior, adicione um método status()em Autenticacaoe também em Permissao. Se a classe Administradorherda das duas, qual versão status()será chamada? Use Administrador.__mro__para mostrar a ordem.
