# # from biblioteca_b4 import biblioteca
# def update_livro(id_livro, novos_dados):
#     for livro in biblioteca:
#         if livro["ID"] == id_livro:
#             livro.update(novos_dados)
#             print(f"Livro com ID {id_livro} atualizado com sucesso!")
#             return 
#     print(f"Erro: Livro com ID {id_livro} não encontrado.")
# print("--- Antes da atualização ---")
# print(biblioteca[2])
# update_livro(3, {"Nome": "Dom Casmurro (Edição Especial)", "Editora": "Melhoramentos"})
# print("\n--- Depois da atualização ---")
# print(biblioteca[2])
# print("-" * 30)
# update_livro(99, {"Nome": "Livro Inexistente"})

# A sua lista de livros
biblioteca = [
    {
        "ID": 1,
        "Nome": "Harry Potter e a Pedra Filosofal",
        "Autor": "J. K. Rowling",
        "Editora": "Rocco",
        "Ano": 2000,
        "Gênero": "Fantasia",
        "Sinopse": "Harry Potter descobre que é um bruxo e começa sua jornada em Hogwarts, onde enfrenta desafios e descobre segredos sobre seu passado."
    },
    {
        "ID": 2,
        "Nome": "O Senhor dos Anéis: A Sociedade do Anel",
        "Autor": "J. R. R. Tolkien",
        "Editora": "HarperCollins",
        "Ano": 1954,
        "Gênero": "Fantasia",
        "Sinopse": "Frodo Bolseiro herda o Um Anel e parte em uma jornada com seus companheiros para destruí-lo antes que caia em mãos erradas."
    },
    {
        "ID": 3,
        "Nome": "Dom Casmurro",
        "Autor": "Machado de Assis",
        "Editora": "Garnier",
        "Ano": 1899,
        "Gênero": "Romance",
        "Sinopse": "Bentinho narra sua juventude e seu relacionamento com Capitu, levantando dúvidas sobre amor, ciúme e traição."
    },
    {
        "ID": 4,
        "Nome": "1984",
        "Autor": "George Orwell",
        "Editora": "Companhia Editora Nacional",
        "Ano": 1949,
        "Gênero": "Distopia",
        "Sinopse": "Winston Smith vive em um regime totalitário onde o Grande Irmão controla tudo. Ele busca liberdade em um mundo de vigilância constante."
    },
    {
        "ID": 5,
        "Nome": "O Pequeno Príncipe",
        "Autor": "Antoine de Saint-Exupéry",
        "Editora": "Agir",
        "Ano": 1943,
        "Gênero": "Fábula",
        "Sinopse": "Um piloto perdido no deserto encontra um pequeno príncipe de outro planeta, que compartilha reflexões sobre amizade, amor e vida."
    },
    {
        "ID": 6,
        "Nome": "A Revolução dos Bichos",
        "Autor": "George Orwell",
        "Editora": "Companhia Editora Nacional",
        "Ano": 1945,
        "Gênero": "Sátira política",
        "Sinopse": "Animais de uma fazenda se rebelam contra os humanos, mas descobrem que a luta pelo poder pode corromper até os ideais mais nobres."
    },
    {
        "ID": 7,
        "Nome": "Orgulho e Preconceito",
        "Autor": "Jane Austen",
        "Editora": "Publicações Europa-América",
        "Ano": 1813,
        "Gênero": "Romance",
        "Sinopse": "Elizabeth Bennet enfrenta pressões sociais e sentimentos conflitantes ao conhecer o orgulhoso Sr. Darcy."
    },
    {
        "ID": 8,
        "Nome": "A Menina que Roubava Livros",
        "Autor": "Markus Zusak",
        "Editora": "Intrínseca",
        "Ano": 2005,
        "Gênero": "Drama",
        "Sinopse": "Narrado pela Morte, o livro conta a história de Liesel, uma menina que encontra conforto nos livros durante a Segunda Guerra Mundial."
    },
    {
        "ID": 9,
        "Nome": "O Código Da Vinci",
        "Autor": "Dan Brown",
        "Editora": "Sextante",
        "Ano": 2003,
        "Gênero": "Suspense",
        "Sinopse": "Robert Langdon investiga um assassinato no Louvre e descobre segredos ocultos da Igreja e da história da humanidade."
    },
    {
        "ID": 10,
        "Nome": "Cem Anos de Solidão",
        "Autor": "Gabriel García Márquez",
        "Editora": "Record",
        "Ano": 1967,
        "Gênero": "Realismo mágico",
        "Sinopse": "A saga da família Buendía em Macondo, explorando gerações marcadas por amor, tragédia e destino."
    }
]
#menção a biblioteca
def update_livro(id_livro, novos_dados):
    for livro in biblioteca:
        if livro["ID"] == id_livro:
            livro.update(novos_dados)
            print(f"Livro com ID {id_livro} atualizado com sucesso!")
            return 
    print(f"Erro: Livro com ID {id_livro} não encontrado.")
print("\nAntes")
print(biblioteca[2])
update_livro(3, {"Nome": "Dom Casmurro (Edição Especial)", "Editora": "Melhoramentos"})
print("\nDepois")
print(biblioteca[2])