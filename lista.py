from nodo import Nodo
from cliente import Cliente

class Lista:
    def __init__(self):
        self.head = None

    def inserir(self, cliente):
        novoNodo = Nodo(cliente)
        if not self.head:
            self.head = novoNodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novoNodo

    def calcular_media(self):
        media_por_cliente = {}
        atual = self.head
        while atual:
            cliente = atual.dado
            if cliente.nome not in media_por_cliente:
                media_por_cliente[cliente.nome] = {'soma': 0, 'count': 0}
            media_por_cliente[cliente.nome]['soma'] += cliente.valorConta
            media_por_cliente[cliente.nome]['count'] += 1
            atual = atual.proximo
        
        medias = {}
        for nome, dados in media_por_cliente.items():
            medias[nome] = dados['soma'] / dados['count']
        return medias
