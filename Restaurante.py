"""

Codigo apresentado como base, para efeturar a implementação do projeto, 
pela disciplina de Estrutura de Dados, do curso de Desenvolvimento e Análise de Sistemas da Universidade de Vila Velha.

>> enchugando duplicação de código

class Nodo:
    def __init__(self, dado=0, proximoNodo=None):
        self.dado = dado
        self.proximo = proximoNodo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

    def setProximo(self, proximoNodo):
        self.proximo = proximoNodo

class Cliente:
    def __init__(self, nome, valorConta):
        self.nome = nome
        self.valorConta = valorConta

    def __repr__(self):
        return f'{self.nome} - {self.valorConta}'

       
 """