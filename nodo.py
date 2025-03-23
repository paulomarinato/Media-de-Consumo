class Nodo:
    def __init__(self, dado=None, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'
