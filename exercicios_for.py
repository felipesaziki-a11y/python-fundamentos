import os


def exercicio01():
    for i in range(0,5):
        print("Bem vindo")


def exercicio02():
    for i in range(15, 31):
        print(i)


def exercicio03():
    numero: int = int(input("Digite um número: "))
    os.system("cls")
    for i in range(0, 11):
        if i != 0:
            print(numero, "*", i, "=", numero * i)


def exercicio04():
    soma: int = 0
    for i in range(0, 5):
        numero: int = int(input("Digite cinco números para calcular a soma: "))
        soma = soma + numero
    print("A soma é", soma)


exercicio04()