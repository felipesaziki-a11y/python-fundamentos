class Autor():
    def __init__(self, nome: str, nacionalidade: str, ano_nascimento: int):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento
    
    def apresentar_dados(self):
        print(f"""Nome do autor: {self.nome}
Nacionalidade: {self.nacionalidade}
Ano de nascimento: {self.ano_nascimento}
""")

    def obter_descricao(self):
        descricao = (f"""{self.nome} - {self.nacionalidade}""")
        return descricao


class Livro():
    def __init__(self, titulo: str, quantidade_paginas: int, ano_publicacao: int, autor: str):
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.ano_publicacao = ano_publicacao
        self.obter_descricao() == autor
    
    def apresentar_dados(self):
        print(f"""Título: {self.titulo}
Quantidade de páginas: {self.quantidade_paginas}
Ano de publicação: {self.ano_publicacao}
Descrição do autor: {self.autor}
""")

def livros():
    autor = [
        Autor("Albert Camus", "Argelino", 1920),
        Autor("Franz Kafka", "Tcheco-alemão", 1920)
    ]
    livro = [
        Livro("O Estrangeiro", 120, 1940, "X"),
        Livro("Carta para meu pai", 120, 1940, "X")
    ]
    for autores in autor:
        autores.apresentar_dados()
        descricao = autores.obter_descricao()
        livro[autores] = Livro(autor=descricao)
    for livros in livro:
        livros.apresentar_dados()