class Nodo:
    def __init__( self, dado=0, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo

class Cliente():
    def __init__(self, nome, valorConta):
        self.nome = nome
        self.valorConta = valorConta

    def __repr__(self):
        return f'{self.nome} - {self.valorConta}'

class Nodo:
    def __init__(self, dado=0, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

class Cliente():
    def __init__(self, nome, valorConta):
        self.nome = nome
        self.valorConta = valorConta

    def __repr__(self):
        return f'{self.nome} - {self.valorConta}'