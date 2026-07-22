class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    

class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        # super() permite ter acesso a propriedades e funções da classe pai
        super().__init__(nome, sobrenome)
        self.cargo = cargo
    
    
def exemplo_funcionario():
    pessoa = Pessoa("Celsio", "Ramos")
    print("Nome completo:", pessoa.gerar_nome_completo())
    funcionario = Funcionario("Faro", "Faro", "A")
    print("Nome completo e cargo:", funcionario.gerar_nome_completo())


class Pessoa:
    def __init__(self, nome: str, numero_telefone: str, email: str):
        self.nome = nome
        self.numero_telefone = numero_telefone
        self.email = email
    
    def apresentar_dados(self):
        print(f"""Nome: {self.nome}
Número de Telefone: {self.numero_telefone}
E-mail: {self.email}
""")
    

class Professor(Pessoa):
    def __init__(self, nome: str, numero_telefone: str, email: str, salario: float):
        super().__init__(nome, numero_telefone, email)
        self.salario = salario

    def apresentar_dados(self):
        print(f"""Nome: {self.nome}
Número de Telefone: {self.numero_telefone}
E-mail: {self.email}
Salário: R${self.salario}
""")
        

class Aluno(Pessoa):
    def __init__(self, nome: str, numero_telefone: str, email: str, nota1: float, nota2: float, nota3: float):
        super().__init__(nome, numero_telefone, email)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
    
    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def apresentar_dados(self):
        media = self.calcular_media()
        print(f""""Nome: {self.nome}
Número de Telefone: {self.numero_telefone}
E-mail: {self.email}
Notas:
        • Nota 1: {self.nota1}
        • Nota 2: {self.nota2}
        • Nota 3: {self.nota3}
Média: {media}
""")
    

def pessoas():
    pessoas = [
        Pessoa("Fernando", "99 47 9929-8374", "fernando_legau@gmail.com")
    ]
    for pessoa in pessoas:
        pessoa.apresentar_dados()


def alunos():
    alunos = [
        Aluno("Fernando", "99 47 9929-8374", "fernando_legau@gmail.com", 9.9, 7.5, 7.8)
    ]
    for aluno in alunos:
        aluno.apresentar_dados()


def professores():
    professores = [
        Professor("Ricardo", "99 47 9899-2334", "ricardo_schultz@hotmail.com", 3_850.76)
    ]
    for professor in professores:
        professor.apresentar_dados()


professores()
alunos()