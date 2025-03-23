from cliente import Cliente
from lista import Lista
from fila_circular import FilaCircular

clientes = [
    Cliente("c1", 1000), Cliente("c1", 900), Cliente("c1", 800), Cliente("c1", 700),
    Cliente("c1", 600), Cliente("c1", 500), Cliente("c1", 400), Cliente("c1", 300),
    Cliente("c1", 200), Cliente("c1", 100), Cliente("c2", 1000), Cliente("c2", 900),
    Cliente("c2", 800), Cliente("c2", 700), Cliente("c2", 600), Cliente("c2", 500),
    Cliente("c2", 400), Cliente("c2", 300), Cliente("c2", 200), Cliente("c3", 1000),
    Cliente("c3", 900), Cliente("c3", 800), Cliente("c3", 700), Cliente("c3", 600),
    Cliente("c3", 500), Cliente("c3", 400), Cliente("c3", 300), Cliente("c4", 1000),
    Cliente("c4", 900), Cliente("c4", 800), Cliente("c4", 700), Cliente("c4", 600),
    Cliente("c4", 500), Cliente("c4", 400), Cliente("c5", 1000), Cliente("c5", 900),
    Cliente("c5", 800), Cliente("c5", 700), Cliente("c5", 600), Cliente("c5", 500),
    Cliente("c6", 1000), Cliente("c6", 900), Cliente("c6", 800), Cliente("c6", 700),
    Cliente("c6", 600), Cliente("c7", 1000), Cliente("c7", 900), Cliente("c7", 800),
    Cliente("c7", 700), Cliente("c8", 1000), Cliente("c8", 900), Cliente("c8", 800),
    Cliente("c9", 1000), Cliente("c9", 900), Cliente("c10", 1000)
]

lista_clientes = Lista()

for cliente in clientes:
    lista_clientes.inserir(cliente)

medias = lista_clientes.calcular_media()
print("Médias por cliente:", medias)

medias_ordenadas = sorted(medias.values())

fila_circular = FilaCircular(len(medias_ordenadas))

for media in medias_ordenadas:
    fila_circular.inserir(media)

print("Médias ordenadas na fila circular:")
for media in fila_circular.ler():
    print(media)
