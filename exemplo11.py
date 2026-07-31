def exemplo_sem_erro():
    try:
        resultado = 10 / 2
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Nâo foi possível dividir valor por 0")
    finally:
        print("FINALLY: Executei sem erro")


def exemplo_com_erro():
    try:
        resultado = 10 / 0
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Nâo foi possível dividir valor por 0")
    finally:
        print("FINALLY: Executei mesmo com erro")

if __name__ == "__main__":
    exemplo_com_erro()