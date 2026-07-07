import os
from pathlib import Path
import time


def exemplo_01():
    txt: str = ""
    for i in range(0, 5):
        if i != 4:
            print("Hey world")
            time.sleep(0.5)
        elif i == 4:
            os.system("cls")
            for i in range(0, 4):
                if i != 3:
                    txt = txt + "."
                    print(txt)
                elif i == 3:
                    print("Nah")
                time.sleep(1.3)
                os.system("cls")


def exemplo_02():
    diretorio_atual: Path = Path.cwd()
    nome_novo_diretorio = "Arquivos"
    caminho_novo_diretorio = diretorio_atual / nome_novo_diretorio

    if caminho_novo_diretorio.exists() == False:
        print("Criando pasta Arquivos")
        caminho_novo_diretorio.mkdir()

    for i in range(2000, 2027):
        nome_pasta_contas = "contas-celesc" + str(i)
        caminho_contas_celesc = caminho_novo_diretorio / nome_pasta_contas
        print(caminho_contas_celesc)
        caminho_contas_celesc.mkdir

        arquivo_caminho = caminho_contas_celesc / "arquivo.txt"
        with open(arquivo_caminho, "w+") as file:
            file.write("The fun never ends")
        print(caminho_contas_celesc)

    # for i in range(0, 10):
    #     with open("arquivo.txt", "w+") as arquivo:
    #         arquivo.write("Hello World")
    

def exemplo_03():
    filmes = []
    filmes.append("Consoles")
    filmes.append("Batman begins")
    filmes.append("O Pequenin")
    filmes.append("Vovózona")
    filmes.append("Gente grande")
    filmes.append("Click")

    filmes[2] = "O Pequenino"

    filmes.remove("Vovózona")
    print("Tamanho da lista de filmes: ", len(filmes))

    print("filmes")
    for i in range(0, len(filmes)):
        filme = filmes[i]
        print(filme)

    for filme in filmes:
        print(filme)


def solicitar_dados_armazenamento():
    numeros = []
    for i in range(0, 5):
        numero_sorte = int(input("Digite o número: "))
        numeros.append(numero_sorte)
    soma: int = 0
    for i in range(0, 5):
        soma = soma + numeros[i]
    quantidade_pares = 0
    for i in range(0, 5):
        if numeros[i] % 2 == 0:
            quantidade_pares = quantidade_pares + 1
    
    print("Quantidade de pares: " + str(quantidade_pares))
    print("Soma: " + str(soma))


solicitar_dados_armazenamento()