class Cliente:
    def __init__(self, nome, valorConta):
        self.nome = nome
        self.valorConta = valorConta

    def __repr__(self):
        return f'{self.nome} - {self.valorConta}'