def exercicio09():
    nomes = []
    nomes.append("Vitor")
    nomes.append("Clara")
    nomes.append("Mauro")
    nomes.append("Garcia")
    nomes.append("Jonas")
    print(f"Nomes:")
    for i in range(0, 5):
        print(f"-", nomes[i])


def exercicio10():
    frutas = []
    for i in range(0,5):
        fruta: str = input("Digite uma fruta: ")
        frutas.append(fruta)
    print("Lista de frutas:")
    for i in range(0,5):
        print("-", frutas[i])


def exercicio11():
    numeros = []
    soma = 0
    for i in range(0, 5):
        numero: int = int(input("Digite um número: "))
        numeros.append(numero)
    for i in range(0, 5):
        soma = soma + numeros[i]
    print("Números digitados:", numeros)
    print("Soma total:", soma)


def exercicio12():
    numeros = []
    pares = ""
    for i in range(0, 6):
        numero: int = int(input("Digite um número: "))
        numeros.append(numero)
    print("Números digitados:", numeros)
    for i in range(0, 6):
        if numeros[i] % 2 == 0:
            pares = pares + str(numeros[i]) + ", "
    print("Números pares:", pares)


def exercicio13():
    notas = []
    for i in range(0, 4):
        nota: float = float(input("Digite uma nota: "))
        notas.append(nota)
    soma = 0
    for i in range(0, 4):
        soma = soma + notas[i]
    media = soma / 4
    round(media)
    print("Números digitados:", notas)
    print("Média total:", media)


exercicio13()