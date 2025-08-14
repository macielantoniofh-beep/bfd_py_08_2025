# frutas.append("manga")
# frutas.insert(0, "limao")
# print(frutas[2])
# frutas += temperos
# print(frutas)
# frutas = ["maça", "abacate", "laranja","jaca","jaca"]
# temperos = ["pimenta","sal"]
#REMOVER ITENS
# del frutas[0]
# print(frutas.clear())

#### ORDENAR LISTAS
# frutas.sort(reverse=True)
# print(frutas)

# COPIAR LISTAS

# l1 = [1,2,3,3,3]
# idx = l1.index(3)
# contagem = l1.count(3)
# for num in range(contagem):
#     l1.pop(idx)
# print(l1)

########################
# 01

# Roupas = ["camisa","calça","bermuda","camiseta"]

#02

# Roupas.append("luva")
# Roupas.insert(3,"meia")
# Roupas.remove("calça")
# print(Roupas)

#03

# Peças = Roupas.copy()
# print(id(Peças))
# print(id(Roupas))

#04

# titulos = [10,20,30,40,50]
# tit = []
# for num in titulos:
#     tit.append(num*5)
# print(tit)

#05
# a1 = [1,2,3,4,5,6] ====> [4,5]
a1 = [1,2,3,4,5,6] 
print(a1)
a2 = a1[3:5]
print(a2)