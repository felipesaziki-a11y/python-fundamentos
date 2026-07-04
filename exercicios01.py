import os
import time


def exercicio_01_mensagens():
    print("Bem-vindo(a)!")
    print("Este aluno está aprendendo Python")
    print("Python é utilizado para desenvolver programas")


def exercicio_02_variáveis():
    nome: str = "Gerson"
    idade: int = 30
    cidade: str = "Blumenau"
    print("NOME:", nome)
    print("IDADE:", idade)
    print("CIDADE:", cidade)


def exercicio_03_input_nome():
    nome: str = input("Digite um nome: ")
    print("Olá", nome, "seja bem-vindo(a)")


def exercicio_04_dados_pessoais():
    nome: str = input("Digite seu nome: ")
    bairro: str = input("Digite o bairro onde mora: ")
    cidade: str = input("Digite a cidade aonde mora: ")
    print(nome, "mora no bairro", bairro, ", na cidade de", cidade)


def exercicio_05_idade_int():
    idade: int = int(input("Digite sua idade: "))
    print("Você tem", idade, "anos")


def exercicio_06_idade_proximo_ano():
    nome: str = input("Digite seu nome: ")
    idade: int = int(input("Digite sua idade: "))
    print(nome, ", você fará", idade + 1, "anos no ano que vem")


def exercicio_07_dobro_numero():
    numero: int = int(input("Digite um número para ver seu dobro: "))
    print("O dobro de", numero, "é", numero * 2)


def exercicio_08_maioridade():
    idade: int = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade")
    elif idade < 18:
        print("Você é menor de idade")


def exercicio_09_numero_positivo():
    numero: int = int(input("Digite um número: "))
    if numero >= 0:
        print(numero, "é um número positivo")
    elif numero < 0:
        print(numero, "é um número negativo")
    else:
        print("Erro")


def exercicio_10_entrada_evento():
    nome: str = input("Digite seu nome: ")
    idade: int = int(input("Digite sua idade: "))
    if idade >= 16:
        print(nome, "você pode entrar no evento")
    elif idade < 16:
        print(nome, "você foi proibido(a) de entrar no evento")


def exercicio_11_verificar_nota():
    nota: float = float(input("Digite a nota do aluno: "))
    if nota >= 7.0:
        print("Este aluno está aprovado")
    else:
        print("Este aluno está em recuperação")


def exercicio_12_verificar_saldo():
    saldo: float = float(input("Digite seu saldo: R$"))
    compra: float = float(input("Digite o valor total da compra: R$"))
    if saldo >= compra:
        print("Compra aprovada")
    else:
        print("Compra negada")


def exercicio_13_aprovacao_nota_frequencia():
    nota: float = float(input("Digite a nota do aluno: "))
    frequencia: int = int(input("Digite a frequência do aluno: "))
    if nota >= 7 and frequencia >= 75:
        print("Este aluno está aprovado")
    else:
        print("Este aluno está em recuperação")


def exercicio_14_entrada_gratuita():
    idade: int = int(input("Digite sua idade: "))
    if idade <= 6 or idade >= 60:
        print("Entrada gratuita aprovada")
    else:
        print("Entrada gratuita negada, por favor pagar o valor apresentador")
        print("R$1900,00")


def exercicio_15_login_simples():
    i = 0
    while i < 1:
        usuario: str = input("Digite seu nome: ")
        senha: str = input("Digite sua senha: ")
        confirmacao: str = input("Digite sua senha de novo: ")
        if confirmacao == senha:
            i += 1
        else:
            print("Sua senha não é a mesma")
    os.system("cls")
    time.sleep(1)
    msg: str = "login feito com sucesso"
    login_usuario: str = input("Digite seu nome: ")
    login_senha: str = input("Digite sua senha: ")
    if login_usuario == usuario and login_senha == senha:
        print(msg)
    elif login_usuario != usuario or login_senha != senha:
        print("Um erro ocorreu. Bloqueando conta")
    time.sleep(0.5)
    os.system("cls")


def exercicio_16_mensagem_varias_vezes():
    i = 0
    msg: str = ""
    while i < 100:
        msg = msg + "01"
        print(msg)
        time.sleep(0.025)
        i += 1
    time.sleep(0.1)
    os.system("cls")


def exercicio_17_numeros_pares():
    i = 1
    while i <= 50:
        if i % 2 == 0:
            print(i)
        time.sleep(0.05)
        i += 1
    time.sleep(1)
    os.system("cls")


def exercicio_18_repetir_mensagem():
    i = 0
    msg: str = input("Digite uma mensagem: ")
    end: int = int(input("Digite a quantidade de ciclos: "))
    os.system("cls")
    while i < end:
        print (msg)
        time.sleep(0.2)
        i += 1
    os.system("cls")


def exercicio_19_somar_1_ate_n():
    i = 0
    numero: int = 0
    end: int = int(input("Digite um número : "))
    while i <= end:
        numero = numero + i
        i += 1
    print(numero)


def exercicio_20_senha_while():
    i = 0
    senha_original: str = input("Digite uma senha: ")
    os.system("cls")
    while i < 1:
        senha: str = input("Digite-a novamente: ")
        while senha != senha_original:
            os.system("cls")
            print("Senha incorreta")
            senha: str = input("Digite-a novamente: ")
        i += 1
    os.system("cls")
    print("Acesso liberado")


def exercicio_triangulo():
    lado1: int = int(input("Escreva a medida do lado 1: "))
    lado2: int = int(input("Escreva a medida do lado 2: "))
    lado3: int = int(input("Escreva a medida do lado 3: "))
    if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Escaleno")
    elif lado1 != lado2 and lado3 or lado2 != lado1 and lado3 or lado3 != lado1 and lado2:
        print("Isóceles")
    elif lado1 == lado2 and lado2 == lado1 and lado1 == lado3:
        print("Equilátero")
    else:
        print("Erro. Não é possível ser um triângulo")


exercicio_triangulo()