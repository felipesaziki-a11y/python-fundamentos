import os
import time


def exemplo_string():
    nome_jogo_comeco: str = "limbus"
    nome_jogo_final: str = "company"
    nome_jogo: str = nome_jogo_comeco.title() + " " + nome_jogo_final.capitalize()
    print("Jogo legal:", nome_jogo)


def primeiro_exemplo():
    print("Hello world")
    carro: str = "Bugatti"
    quantidade_carro: int = 3
    preco_unitario_carro: float = 120000.99
    preco_total: float = quantidade_carro * preco_unitario_carro
    print("Carro comprado:", carro, "Quantidade comprada", quantidade_carro, "Preço total: R$", preco_total)


def exemplo_solicitar_dados():
    console: str = input("Digite o nome do console: [XBOX ou PS5]").upper().strip()
    quantidade: int = int(input("Digite a quantidade"))

    preco: float = 0
    if console == "XBOX":
        preco = 6000.00
    # elif é "else if"
    elif console == "PS5":
        preco = 7000.00
    else:
        print("Inválido")
        return
    print("Preço: R$", preco)
    print("Console:", console)
    print("Total: R$", preco * quantidade)
    

def exemplo_if_alunos():
    nota1: float = float(input("Digite a nota 1: "))
    nota2: float = float(input("Digite a nota 2: "))
    nota3: float = float(input("Digite a nota 3: "))
    media: float = (nota1 + nota2 + nota3) / 3
    os.system("cls")
    time.sleep(2)
    print("Média:", media)
    if media < 6:
        print("Status: Reprovado")
    elif media >= 6:
        print("Status: Aprovado")

def exemplos_while():
    def contar_ate_5():
        i = 0
        while i < 5:
            print(i)
            i += 1

    def contagem_regressiva():
        i = 5
        print("Contagem regressiva")
        while i >= 0:
            print(i)
            i -= 1

    def solicitar_dados():
        i = 0
        total_mensal_salario = 0
        while i < 3:
            jogador: str = input("Nome do jogador: ")
            posicao: str = input("Posição do jogador: ")
            salario_anual: float = float(input("Salário anual: "))
            salario_mensal = salario_anual / 12
            print("Jogador:", jogador, "ganha R$", salario_mensal, sep=" ", end="\n\n\n\n")
            total_mensal_salarios = total_mensal_salario + salario_mensal
            i += 1
        print("Total de mensal dos salários: ", total_mensal_salarios)
    def escrever_arquivo_copa_mundo():
        texto_arquivo = "Time1;Time2;Placar\n"
        i = 0
        while i < 3:
            time1: str = input("Time 1: ")
            time1_gols: int = int(input("Gols " + time1 + ": "))
            time2: str = input("Time 2: ")
            time2_gols: int = int(input("Gols " + time2 + ": "))
            placar = str(time1_gols) + "x" + str(time2_gols)
            texto_arquivo += f"{time1};{time2};{placar}\n"
            print("\n\n\n---------------------------------------------")


