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


def exemplo_com_multiplos_tratamentos():
    numero1_digitado = "cinquenta"
    numero2_digitado = "vinte"
    try:
        resultado: int = int(numero1_digitado) / int(numero2_digitado)
        print(resultado)
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    except ValueError:
        print("Número digitado é inválido")

    print(".")


def exemplo_mensagem_erro():
    try:
        aluno = {"nome": "Pedro", "nota1": 7.7}
        media_aluno = aluno["media"]
        print(media_aluno)
    except KeyError as erro:
        print("Mensagem de erro tentar acessar a chave:", erro)


# Ponto de entrada da aplicação, deve ter um único da aplicação inteira
if __name__ == "__main__":
    exemplo_mensagem_erro()