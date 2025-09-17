# Herança

#1 Criar classe pessoa com suas características e uma classe funcionário que herde pessoa e tenha novos atributos.
class Pessoa:
    def __init__(self,nome,idade,transporte):
        self.nome = nome
        self.idade = idade
        self.transporte = transporte
class Funcionário(Pessoa):
    def __init__(self,nome,idade,transporte,matricula,função):
        super().__init__(nome,idade,transporte)
        self.matricula = matricula
        self.função = função

pessoa1 = Pessoa("Jose",50,"onibus")
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.transporte)
func1 = Funcionário ("Antonio",30,"uber","111-1","Gerente")
print(func1.nome)
print(func1.idade)
print(func1.transporte)
print(func1.matricula)
print(func1.função)


#2 VocÊ tem uma empresa que usa computadores padronizados, contudo o departamaneto de IA, precisa de uma placa de video. ENtão, 
# crie uma classe computador, que tenha modelo, processador, quantidade de memoria e departamento.
# E uma classe que herde as características da Classe computador,mas adicione a placa de video.

class Computador:

    def __init__(self, modelo, processador, memoria_ram, departamento):
        self.modelo = modelo
        self.processador = processador
        self.memoria_ram = memoria_ram
        self.departamento = departamento
    def __str__(self):
        return (f"Modelo: {self.modelo}\n"
                f"Processador: {self.processador}\n"
                f"Memória RAM: {self.memoria_ram}GB\n"
                f"Departamento: {self.departamento}")

class ComputadorUP(Computador):

    def __init__(self, modelo, processador, memoria_ram, departamento, placa_de_video):
        super().__init__(modelo, processador, memoria_ram, departamento)
        self.placa_de_video = placa_de_video
        #print(f"Computador ({self.modelo}) para o departamento de {self.departamento} com placa de vídeo {self.placa_de_video} criado com sucesso.")
    def __str__(self):
        return super().__str__() + f"\nPlaca de Vídeo: {self.placa_de_video}"


computador_pad = Computador("HP EliteDesk 800 G6", "Intel Core i7", 16, "Demais Setores")
print(computador_pad)
computador_up = ComputadorUP("Lenovo ThinkStation P620", "AMD Ryzen Threadripper PRO", 64, "Inteligência Artificial", "NVIDIA GeForce RTX 4090")
print(computador_up)