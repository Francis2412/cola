from colaejem import Node
from colaejem import cola

def main():
    cola = cola()
    nodo = Node(100)
    cola.enqueue(nodo)
    nodo = Node(700)
    cola.enqueue(nodo)
    nodo = Node(500)
    cola.enqueue(nodo)
    nodo = Node(600)
    cola.enqueue(nodo)

    lista = cola.clear()
    for n in lista:
        n.print()

main()