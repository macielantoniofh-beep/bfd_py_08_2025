#1
lista = [1, 2, 3, 4, 5]
dobro_da_lista = list(map(lambda x: x * 2, lista))
print(f"Nova lista: {dobro_da_lista}")
#2
lista2 = [10, 15, 20, 25, 30]
numeros_pares = list(filter(lambda x: x % 2 == 0, lista2))
print(f"Números pares: {numeros_pares}")
#3
from functools import reduce

lista3 = [1, 2, 3, 4, 5]
soma_total = reduce(lambda x, y: x + y, lista3)
print(f"Soma total: {soma_total}")
#4
lista_frutas = ["uva", "banana", "maçã", "laranja"]
ordem_comprimento = sorted(lista_frutas, key=lambda x: len(x))

print(f"Ordem por comprimento: {ordem_comprimento}")
#5
lista_nomes = ["ana", "pedro", "maria"]
nomes_maius = list(map(lambda x: x.capitalize(), lista_nomes))

print(f"Capitalizados: {nomes_maius}")

#6
from functools import reduce

lista_mult = [2, 3, 4, 5]
produto_total = reduce(lambda x, y: x * y, lista_mult)

print(f"O produtos dos itens é : {produto_total}")

#7
lista_frutas2 = ["banana", "uva", "maçã", "laranja"]
ordem_ultimo = sorted(lista_frutas2, key=lambda x: x[-1])

print(f"Ordem por último caractere: {ordem_ultimo}")
