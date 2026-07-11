def exercicio05():
    nomes = []
    nomes.append("João")
    nomes.append("Clara")
    nomes.append("Pedro")
    nomes.append("Michael")
    nomes.append("Dória")
    print("Nomes:", nomes)


def exercicio06():
    frutas = []
    i = 0
    while i < 3:
        fruta: str = input("Digite o nome de três frutas: ")
        frutas.append(fruta)
        i += 1
    print("Frutas:", frutas)


def exercicio07():
    numeros = []
    i = 0
    while i < 4:
        numero: int = int(input("Digite quatro números inteiros: "))
        numeros.append(numero)
        i += 1
    print("Números:", numeros)


def exercicio08():
    notas = []
    nota1: float = float(input("Digite a primeira nota: "))
    nota2: float = float(input("Digite a segunda nota: "))
    nota3: float = float(input("Digite a terceira nota: "))
    nota4: float = float(input("Digite a quarta nota: "))
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    notas.append(nota4)
    print("Vetor original:", notas)
    print("Primeira nota:", notas[0])
    print("Primeira nota:", notas[3])
    notas[1] = 10.0
    notas.pop(3)
    media = (notas[0] + notas[1] + notas[2]) / 3
    print("Vetor final:", notas)
    print("Média final:", media)
    


exercicio06()