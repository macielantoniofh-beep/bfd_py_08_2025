# Exercícios de listas
# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["Grandes sertões veredas","Vidas secas","Os Sertões"]
print(livros)
# # 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
livros.pop(1)
print(livros)
# # 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("Torto Arado")
livros.append("Capitães da Areia")
print(livros)
# # 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1,"Duna")
print(livros)
# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
livro_esp = "Silêncio dos inocentes"
if livro_esp in livros:
    livros.remove(livro_esp)
    print(f"O item '{livro_esp}' foi removido com sucesso.")
else:
    print(f"Livro não encontrado")
# # 6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.
números = [1,2,3,2,4,2,5]
análise = números.count(2)
print(f"O 2 aparece {análise} vezes na lista.")
# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"
for i in livros:
    print(f"O livro {i} é interessante")
# 8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]
for idade in idades:
    if idade >= 18:
        print(idade)
# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma = 0
for itens in valores:
    soma += itens
print(soma)
# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

notas = []
print("Insira as 3 notas do Aluno 1:")
notas_aluno1 = []
for i in range(3):
    nota = float(input(f"Nota {i+1}:"))
    notas_aluno1.append(nota)
notas.append(notas_aluno1)
print("\nInsira as 3 notas do Aluno 2:")
notas_aluno2 = []
for i in range(3):
    nota = float(input(f"Nota {i+1}:"))
    notas_aluno2.append(nota)
notas.append(notas_aluno2)
print(f"\nLista de notas completa: {notas}")
print("\nCalculando as médias...")
media_aluno1 = sum(notas[0]) / len(notas[0])
print(f"Média do Aluno 1: {media_aluno1:.2f}")
media_aluno2 = sum(notas[1]) / len(notas[1])
print(f"Média do Aluno 2: {media_aluno2:.2f}")

# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
# [ ] - para posições vazias
# tor - para a torre
# cav - para o cavalo
# bis - para o bispo
# rai - para a rainha
# rei - para o rei
# pea - para o peão
# Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)

line1 = {"a":"tor","b":"cav","c":"bis","d":"rai","e":"rei","f":"bis","g":"cav","h":"tor"}
line2 = {"a":"pea","b":"pea","c":"pea","d":"pea","e":"pea","f":"pea","g":"pea","h":"pea"}
line3 = {"a":[   ],"b":[   ],"c":[   ],"d":[   ],"e":[   ],"f":[   ],"g":[   ],"h":[   ]}
line4 = {"a":[   ],"b":[   ],"c":[   ],"d":[   ],"e":[   ],"f":[   ],"g":[   ],"h":[   ]}
line5 = {"a":[   ],"b":[   ],"c":[   ],"d":[   ],"e":[   ],"f":[   ],"g":[   ],"h":[   ]}
line6 = {"a":[   ],"b":[   ],"c":[   ],"d":[   ],"e":[   ],"f":[   ],"g":[   ],"h":[   ]}
line7 = {"a":"pea","b":"pea","c":"pea","d":"pea","e":"pea","f":"pea","g":"pea","h":"pea"}
line8 = {"a":"tor","b":"cav","c":"bis","d":"rai","e":"rei","f":"bis","g":"cav","h":"tor"}
print(line8)
print(line7)
print(line6)
print(line5)
print(line4)
print(line3)
print(line2)
print(line1)