def validar_idade(idade: int):
    if idade < 0:
        raise ValueError("A idade não deve ser menor que zero")


def testar_validade_idade():
    try:
        validar_idade(-2)
        ("Olá mundo")
    except ValueError as erro:
        print(f"Erro: {erro}")
    print("Adeus, encerrado com sucesso")


class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        self.faltam = valor - saldo
        super().__init__(
            f"Saldo insuficiente: Saldo: R$ {self.saldo:.2f}, "
            f"Saque: R$ {self.valor:.2f} (faltam R$ {self.faltam:.2f})"
)


def sacar(saldo, valor):
    if not isinstance(valor, (float, int)):
        raise TypeError("Erro: O valor deve ser um número real ou inteiro")
    if valor <= 0:
        raise ValueError("O valor deve ser superior a R$ 0,00")
    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    saldo -= valor
    print("Saque realizado com sucesso")


def exemplo_tipos_erros():
    saldo: float = float(input("Digite o seu saldo: ").replace(",", "."))
    valor_saque: float = float(input("Digite o valor que quer sacar: ").replace(",", "."))
    try:
        sacar(saldo, valor_saque)
    except TypeError as erro:
        print("ERRO:", erro)
    except ValueError as erro:
        print("ERRO:", erro)
    except SaldoInsuficienteError as erro:
        print("ERRO:", erro)


exemplo_tipos_erros()