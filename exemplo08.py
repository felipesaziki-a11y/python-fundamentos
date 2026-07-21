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


exemplo_funcionario()