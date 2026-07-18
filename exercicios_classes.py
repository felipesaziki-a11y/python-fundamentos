class Tenis:
    def __init__(self, modelo: str, tamanho: float, marca: str, valor: float):
        self.modelo = modelo
        self.tamanho = tamanho
        self.marca = marca
        self.valor = valor
    
    def apresentar_dados(self):
        print(f"""Modelo: {self.modelo}
Tamanho: {self.tamanho}
Marca: {self.marca}
Valor: R$ {self.valor}
""")


def exemplo_tenis():
    nike_preto = Tenis("Nike Preto", 40, "Nike", 56.99)
    adidas_branco = Tenis("Adidas Branco", 37, "Adidas", 66.99)
    mizuno_azul_preto = Tenis("Mizuno Azul-Preto", 35, "Mizuno", 35.99)
    nike_preto.apresentar_dados()
    adidas_branco.apresentar_dados()
    mizuno_azul_preto.apresentar_dados()


class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def apresentar_dados(self):
        media = self.calcular_media()
        situacao = self.apresentar_situacao()
        print(f"""Nome: {self.nome}
Primeira nota: {self.nota1}
Segunda nota: {self.nota2}
Média final: {media}
Situação: {situacao}
""")
    
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def apresentar_situacao(self):
        return "Aprovado" if self.calcular_media() >= 7 else "Reprovado"

        
def alunos():
    alunos = [
        Aluno("Pedro Aureira", 7.5, 7.8),
        Aluno("Josef Manikin", 8.6, 9.0),
        Aluno("Karlos 'Karlinhos' Ferreira", 5.6, 4.5),
    ]
    for aluno in alunos:
        aluno.apresentar_dados()


class Triangulo:
    def __init__(self, base: int, altura: int, lado1: int, lado2: int, lado3: int):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def apresentar_dados(self):
        equilatero = self.verificar_equilatero()
        area = self.calcular_area()
        if equilatero == True:
            print(f"""Área: {area} m²
Triângulo Equilátero
""")
        elif equilatero == False:
            print(f"""Área: {area} m²
Triângulo Não-Equilátero
""")

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def verificar_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado2 and self.lado2 == self.lado3:
            equilatero = True
        elif self.lado1 != self.lado2 or self.lado1 != self.lado2 or self.lado2 != self.lado3:
            equilatero = False
        return equilatero


class Quadrado:
    def __init__(self, lado: int):
        self.lado = lado
    
    def apresentar_dados(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"""Área: {area} m²
Perímetro: {perimetro} m
""")
    
    def calcular_area(self):
        return self.lado * self.lado
    
    def calcular_perimetro(self):
        return self.lado * 4


class Retangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    
    def apresentar_dados(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"""Base: {self.base} m
Altura: {self.altura} m
Área: {area} m²
Perímetro: {perimetro} m
""")
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (self.base * 2) + (self.altura * 2)


class Circulo:
    def __init__(self, raio: int):
        self.raio = raio

    def apresentar_dados(self):
        area = self.calcular_area()
        circunferencia = self.calcular_circunferencia()
        print(f"""Raio: {self.raio} m
Área: {area} m²
Circunferência: {circunferencia} m
""")

    def calcular_area(self):
        return 3.14 * (self.raio * self.raio)
    
    def calcular_circunferencia(self):
        return 2 * 3.14 * self.raio

def triangulos():
    triangulos = [
        Triangulo(5, 6, 2, 2, 3),
        Triangulo(3, 3, 3, 3, 3),
    ]
    for triangulo in triangulos:
        triangulo.apresentar_dados()


def quadrados():
    quadrados = [
        Quadrado(6),
        Quadrado(7)
    ]
    for quadrado in quadrados:
        quadrado.apresentar_dados()


def retangulos():
    retangulos = [
        Retangulo(7, 10),
        Retangulo(2, 9)
    ]
    for retangulo in retangulos:
        retangulo.apresentar_dados()


def circulos():
    circulos = [
        Circulo(6),
        Circulo(9)
    ]
    for circulo in circulos:
        circulo.apresentar_dados()


class Personagem():
    def __init__(self, nome: str, vida: int, ataque: int):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def apresentar_dados(self):
            print(f"""Nome: {self.nome}
Vida: {self.vida}
Ataque: {self.ataque}
""")
        
    
    def atacar(self, outro_personagem):        
        outro_personagem.vida = outro_personagem.vida - self.ataque
        print(f"""{self.nome} atacou {outro_personagem.nome}!
Vida atual de {outro_personagem.nome}: {outro_personagem.vida}""")


def personagens():
    personagens = [
        Personagem("Gregor", 35, 23),
        Personagem("Head Hooligan", 55, 17)
    ]
    for personagem in personagens:
        personagem.apresentar_dados()
    personagens[0].atacar(personagens[1])

personagens()