# MATRIZ - UM CONJUNTO DE NUMERO ORGANIZADO BIDIMENSIONAL - ESTRUTURA - UMA LISTA DENTRO DA OUTRA
#como imprimir a matriz embaixo da outra
# matriz=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print(matriz[1][1])
#TRIDIMENSIONAL
# matriz=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print(matriz)
# tridimensional = [[[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]]]
# print(tridimensional)
# tridimensional = [[[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]]]
# print(tridimensional[1][1][2])
# tridimensional = [[[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]],
#                   [[1,2,3],[4,5,6],[7,8,9]]]
# tridimensional[1][1][2] = 33

#COMPREENSAO DE LISTA
# lista1 = []
# for i in range(10):
#     lista1.append(i)
# print(lista1)

# lista1 = []
# for i in range(10):
#     lista1.append(i*2)
# print(lista1)
# lista2 = [i for i in range(10) if i%2==0]
# print(lista2)

# lista1 = []
# for i in range(10):
#     lista1.append(i*2)
# print(lista1)
# lista2 = [[i for i in range(3)] for x in range(3)]
# print(lista2)

# lista3 = [0 for i in range(3)]
# print(lista3)
# lista4 = []
# for i in range(3):
#     lista1.append(0)
# print(lista4)

#MESMO CAMINHO

# lista1 = []
# for i in range(10):
#     lista1.append(i)
# print(lista1)
# lista2 = [[i for i in range(3)] for x in range(3)]
# print(lista2)

#quebra os caracteres e vira lista
# nome ="ANTONIO"
# print(list(nome))


#COLECOES
#TUPLAS  = TUPLE  --- PARECIDA COM A LISTA, NAO CONSEGUE ALTERAR OS ELEMENTOS , mais leve e economiza espaço
#definido tanto parenteses, como com a virgula
# tuple = ()
# print(type(tuple))
# tuple = 1,
# print(type(tuple))
###exemplo
# tupla1 = (1,2,3,4)
# for num in tupla1:
#     print(num+5)
# print(tupla1)
# tupla1 = ("casa","caju","lapis")
# print(tupla1.index("caju"))
# tupla1 = ("casa","caju","lapis")
# print(tupla1.count("lapis"))

#conjunto set

# teste = {"antonio","antonio"}
# print(teste)


#conjunto dicionario
# teste = {"nome":"antonio"} CHAVE E O VALOR -  PODE TER VARIOS ITENS
# print(type(teste))
# listdic = {["nome":"antonio", 
#          "IDADE": 31,
#          "endereço": "Av 0",
#          "turma": ("turma 34", "turma 36"]}
# print(listdic)

#adicionar um elemento ao conjunto
# teste = {1,2}
# teste.add(3)
# print(teste)

# teste = {1,2}
# teste.clear()
# print(teste)
# teste = {1,2}
# teste2 = teste.copy()
# print(teste)
# print(teste2)
### foto diferença

# print(conjunto.discard("e o item que quer")) PARA RETIRAR ITEM
#print(conjunto)

# print(conjunto.intersection("e o item que quer"))  = print(conjunto1 & conjunto2)
#print(conjunto1 | conjunto2) uniao dos conjuntos
#print(conjunto)

##### conjunto é mais leve que a lista, mas quando tem repetição pode ocorrer erros
