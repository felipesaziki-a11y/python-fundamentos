# /try-execept
def exemplo_sem_tratamento():
    print("Divisão:", 10 / 0)
    # Lança a exceção ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão:", 10 / 0)
    except ZeroDivisionError:
        print("Não é possível dividir um número por 0")


if __name__ == "__main__":
    exemplo_sem_tratamento()
