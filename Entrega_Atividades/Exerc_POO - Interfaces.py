'''
Criando uma interface

Crie uma interface chamada Pagamento com um método abstrato processar(valor). Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. Mostre como chamar processar() para cada uma.

Interface múltipla

Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.

Interface em herança múltipla

Crie uma interface Imprimivel com o método imprimir(). Crie outra interface Exportavel com o método exportar(). Implemente uma classe Relatorio que herde de ambas e implemente os métodos.

Forçando contrato

Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. O que acontece quando você tenta instanciá-la? Corrija o código.
'''

from abc import ABC, abstractmethod

class Pagamento(ABC):

    @abstractmethod
    def processar(self, valor: float):
        pass

class CartaoCredito(Pagamento):

    def processar(self, valor: float):
        return f"Processando pagamento de R${valor:.2f} via Cartão de Crédito. Cobrança enviada à operadora."

class Boleto(Pagamento):

    def processar(self, valor: float):
        return f"Processando pagamento de R${valor:.2f} via Boleto. Documento gerado para pagamento em 3 dias."

pagamento_cc = CartaoCredito()
pagamento_boleto = Boleto()

print(pagamento_cc.processar(100.50))
print(pagamento_boleto.processar(69.90))

#
class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        return "O Computador está iniciando... Bem-vindo!"
        
    def desligar(self):
        return "O Computador está sendo desligado com segurança."
    
meu_computador = Computador()

print(meu_computador.ligar())
print(meu_computador.desligar())

#

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        pass


class Relatorio(Imprimivel, Exportavel):
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self):
        return f"Imprimindo o relatório: '{self.titulo}'."
        
    def exportar(self):
        return f"Exportando o relatório: '{self.titulo}' para formato PDF."

relatorio_vendas = Relatorio("Relatório Anual de Vendas")

print(relatorio_vendas.imprimir())
print(relatorio_vendas.exportar())

#

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
        
    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoriaParcial(Repositorio):
    def salvar(self, objeto):
        print(f"Objeto {objeto} salvo na memória temporária.")
        
try:
    repo_parcial = RepositorioMemoriaParcial()
except TypeError as e:
    print(f"Erro gerado ao tentar instanciar RepositorioMemoriaParcial: {e}")

