# DICIONARIO
# 01
# cadastro ={}
# print(cadastro)
# cadastro.update({"nome": "Lucas"})
# cadastro.update({"idade": 25})
# cadastro.update({"email": "lucas@email.com"})
# print(cadastro)

# 02
# cliente = {"nome": "Amanda", "idade": 31}
# if not cliente.get("telefone"):
#     print("Não Informado")

#03
# Utilize um laço for para imprimir todas as chaves do dicionário abaixo.
# livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
# for itens in livro:
#     print(itens)

# 04
# Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True.
# livro.update({"disponível": True})
# print(livro)

# 05
# Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.
# print(livro.pop("ano"))
# print(livro)

#06
# Crie um dicionário compras com pelo menos 3 itens (nome do produto como chave e preço como valor). Em seguida, use .values() para calcular o total da compra.
# Compras = {"papel": 0.50 , "caneta":2 , "lapis":1.50}
# soma = 0
# for itens in Compras.values():
#     soma += itens
# print(soma)

#07
# Dado o dicionário:
# frutas = {"maçã": 3, "banana": 5, "laranja": 2}
# # Imprima as frutas que têm mais de 2 unidades usando um laço for.
# for fruta in frutas.items():
#     if fruta[1] >2:
#         print(fruta[0])
        
#08
# Verifique se a chave "senha" está presente no dicionário abaixo. Se não estiver, adicione-a com o valor "123456".
# usuario = {"login": "joaosilva"}
# if "senha" not in usuario:
#     usuario["senha"] = "123456"
# print(usuario)

#09
# Use o método .items() para iterar sobre o dicionário abaixo e imprima frases como "A capital de SP é São Paulo".
# capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}
# for i,x in capitais.items():
#     print(f"A capital de {i}, é {x}")


#10
# Dado o dicionário abaixo, atualize o valor da chave "estoque" somando 10 unidades ao valor atual.
# produto = {"nome": "Teclado", "estoque": 15}
# produto["estoque"] += 10
# print(produto)



# import numpy as np

# # Cria um tabuleiro de xadrez vazio usando list comprehension
# tabuleiro_vazio = [['[ ]' for _ in range(8)] for _ in range(8)]
# # Adiciona as peças brancas (minúsculas)
# tabuleiro_vazio[0] = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
# # Adiciona os peões brancos
# tabuleiro_vazio[1] = ['pea' for _ in range(8)]
# # Adiciona os peões pretos
# tabuleiro_vazio[6] = ['pea' for _ in range(8)]
# # Adiciona as peças pretas (maiúsculas)
# tabuleiro_vazio[7] = ['TOR', 'CAV', 'BIS', 'RAI', 'REI', 'BIS', 'CAV', 'TOR']
# # Imprime o tabuleiro usando a biblioteca numpy para melhor visualização
# print(np.matrix(tabuleiro_vazio))