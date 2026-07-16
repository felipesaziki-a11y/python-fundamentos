from typing import Dict

def exercicio01():
    pacientes: Dict[str, str|float|int|bool] = {}
    pacientes["nome_paciente"] = "Pedro"
    pacientes["idade"] = 12
    print(pacientes.keys())
    print("Pacientes:", pacientes["nome_paciente"], ",", pacientes["idade"], "anos")


def exercicio02():
    aluno: Dict[str, str|int] = {}
    aluno["nome"] = "Raul"
    aluno["idade"] = 16
    aluno["turma"] = "1C"
    aluno["curso"] = "Língua estrangeira - Inglês"
    print("Chaves de aluno:")
    for i in aluno:
        print(i)


def exercicio03():
    produto: Dict[str, str|float|int] = {}
    produto["produto"] = "Beterraba"
    produto["preco"] = 5.40
    produto["estoque"] = 6
    produto["categoria"] = "Hortifruti"
    print("Valores de produto:")
    for i in produto.values():
        print(i)


def exercicio04():
    funcionario: Dict[str, str|float] = {
        "nome": "Pedro",
        "cargo": "Consultor",
        "salario": 4_800.99,
        "setor": "RH"
    }
    print("Valores de funcionario:")
    for i, a in funcionario.items():
        print(i, ":", a)


def exercicio05():
    livro: Dict[str, str|int] = {}
    livro["titulo"] = input("Digite o título do livro: ")
    livro["autor"] = input("Digite o nome do autor do livro: ")
    livro["ano_publicacao"] = int(input("Digite o ano de publicação do livro: "))
    livro["quantidade_paginas"] = int(input("Digite a quantidade de páginas do livro: "))
    print("Dados do livro:")
    for i, a in livro.items():
        print(i, ":", a)


def exercicio06():
    jogos1: Dict[str, str|int|float] = {
        'nome_jogo': 'Limbus Company',
        'genero': 'Roguelike',
        'ano_lancamento': 2022,
        'preco': 0.00
    }
    jogos2: Dict[str, str|int|float] = {
        'nome_jogo': 'Ender Lilies',
        'genero': 'Metroidvania',
        'ano_lancamento': 2018,
        'preco': 25.99
    }
    print("Dados dos jogos:")
    for chave, valor in jogos1.items():
        print(chave, ":", valor)
    print("-------------------------------------")
    for chave, valor in jogos2.items():
        print(chave, ":", valor)


exercicio06()