class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.size = 0

    def inserir(self, valor):
        if self.size == self.tamanho:
            self.inicio = (self.inicio + 1) % self.tamanho  # Substitui o elemento mais antigo
        else:
            self.size += 1
        self.fila[self.fim] = valor
        self.fim = (self.fim + 1) % self.tamanho  # Move o índice fim

    def ler(self):
        # Cria uma lista para armazenar os elementos na fila circular
        elementos = []
        # Se a fila não estiver vazia, percorre os índices da fila circular
        for i in range(self.size):
            index = (self.inicio + i) % self.tamanho  # Acesse a posição correta considerando a circularidade
            elementos.append(self.fila[index])
        return elementos
