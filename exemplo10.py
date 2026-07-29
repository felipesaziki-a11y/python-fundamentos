# /try-execept
# def exemplo_sem_tratamento():
#     print("Divisão:", 10 / 0)
#     print("A")
    # Lança a exceção ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão:", 10 / 0)
    except ZeroDivisionError:
        print("Não é possível dividir um número por 0")
    print("Tudo normar")


def exemplo_com_tratamento_conversao():
    numero_digitado: str = "dois"
    try:
        numero: int = int(numero_digitado)
        print("Número digitado:", numero)
    except ValueError:
        print("Texto digitado não é um número válido")
    print(".")



# Ponto de entrada da aplicação, deve ter um único da aplicação inteira
if __name__ == "__main__":
    exemplo_com_tratamento_conversao()