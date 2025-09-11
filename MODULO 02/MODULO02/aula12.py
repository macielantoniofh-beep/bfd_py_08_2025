# REVISAO OBJETO

#ATRIBUTO PRIVADO - ACESSA SOMENTE DENTRO DA FUNÇÃO  PARA PRIVADO __ SO NA FRENTE DA FUNÇÃO
#SETTERS - FUNÇÃO DEFINIR VALOR
#GETTERS - PEGAR O VALOR

def get_saldo(self):
    return self.__saldo
def set_saldo(self,valor):
    if valor < 0:
        print("Saldo não pode ser negativo")
    else:
        self.__saldo = valor
# se deixou privado e nao precisa alterar a informação, nao precisa da ferramenta.
#encapsulamento - protegendo os dados fora da função