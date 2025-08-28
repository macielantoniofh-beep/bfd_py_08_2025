#1 Crie um dicionário simples - Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", e preencha com valores fictícios.
aluno = {"nome":"juca", "idade": 15, "nota": 10}
print(aluno)
#2 Acessando valores Dado o dicionário: Imprima o nome do produto e a quantidade em estoque.
produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print("Nome do produto:", produto["nome"])
print("Quantidade em estoque:", produto["estoque"])
#3 Adicionando novos pares chave-valor Dado o dicionário: -- Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa = {"nome": "Carlos", "idade": 30}
pessoa.update({"cidade": "São Paulo"})
print(pessoa)
#4 Removendo elementos Dado o dicionário: Remova a chave "ano" do dicionário.
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
carro.pop("ano")
print(carro)
#5 Verificando existência de uma chave Verifique se a chave "telefone" existe no dicionário:
contato = {"nome": "Ana", "email": "ana@email.com"}
if not contato.get("telefone"):
    print("Não contém")
#6 Contando frequência de palavras Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.
palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
contagem = {}
for palavra in palavras:
    if palavra in contagem:
      contagem[palavra] += 1
    else:
      contagem[palavra] = 1
print(contagem)
#7 Invertendo um dicionário Dado o dicionário:Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
d = {"a": 1, "b": 2, "c": 3}
dnew = {valor: chave for chave, valor in d.items()}
print(dnew)
#8 Dicionário com listas Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
notas_alunos = {"Zé": [10, 9, 10], "João": [9, 9, 9], "Juca": [8, 10, 8]}
for aluno, notas in notas_alunos.items():
  soma_notas = sum(notas)
  quantidade_notas = len(notas)
  media = soma_notas / quantidade_notas
  print(f"A média do(a) aluno(a) {aluno} é: {media:.2f}")
#9 Mesclando dois dicionários Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
Objetos = {"Zé":"carro","Juca":"moto"}
Objetos2 = {"João":"avião","lucas":"caminhão"}
Objetos.update(Objetos2)
print(Objetos)
#10 Ordenando dicionário por valor Dado o dicionário: Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
pontuacoes_ordenadas = sorted(pontuacoes.items(), key=lambda item: item[1], reverse=True)
for nome, pontuacao in pontuacoes_ordenadas:
  print(f"{nome}: {pontuacao}")