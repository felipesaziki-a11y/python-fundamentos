from abc import ABC, abstractmethod

# ABC indica que esta é uma classe abstrata.
# Ela serve apenas como modelo para outras classes.
class Animal(ABC):

    def __init__(self, nome):
        # Atributo comum que todos os animais terão.
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        # Método abstrato.
        # Não possui implementação aqui.
        # Toda classe que herdar Animal será obrigada
        # a criar sua própria versão deste método.
        pass


# Classe concreta que herda de Animal.
class Cachorro(Animal):

    def emitir_som(self):
        # Implementação específica para cachorro.
        return "Au au!"


# Outra classe concreta.
class Gato(Animal):

    def emitir_som(self):
        # Implementação específica para gato.
        return "Miau!"


# Criando objetos normalmente.
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

# print(f"{cachorro.nome}: {cachorro.emitir_som()}")
# print(f"{gato.nome}: {gato.emitir_som()}")


class Personagem(ABC):
    def __init__(self, nome: str, ataque: int, defesa: int):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa

    @abstractmethod
    def falar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, ataque, defesa):
        super().__init__(nome, ataque, defesa)
    
    def falar(self):
        return "Precisa de algo?"
    

class Mago(Personagem):
    def __init__(self, nome, ataque, defesa):
        super().__init__(nome, ataque, defesa)
    
    def falar(self):
        return "Preciso de sua ajuda."
    

def dialogo():
    guerreiro = Guerreiro("Julius", 6, 6)
    mago = Mago("Elise", 7, 3)
    print(f"""{guerreiro.nome} {guerreiro.ataque}/{guerreiro.defesa}: {guerreiro.falar()}""")
    print(f"""{mago.nome} {mago.ataque}/{mago.defesa}: {mago.falar()}""")

dialogo()