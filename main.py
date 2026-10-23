from queque import Node
from queque import Cola
import os 

def main():
    Cola=None
    opcion = 0
    
    while opcion!=6:
        print("********Operaciones Sobre Pila***********")
        print("1. Crear Cola Vacia")
        print("2. Encolar")
        print("3. Desencolar")
        print("4. Visualizar Frente / Fondo")
        print("5. Vaciar Cola")
        print("6. Salir")
        print("*****************************************")
        opcion = int(input("SELECCIONE UNA OPCION: "))
        
        match opcion:
            case 1:
                cola = Cola()
            case 2:
                dato = int(input("Digite el valor del nodo: "))    
                nodo = Node(dato)
                cola.enqueue(nodo)
            case 3:
                
            case 4:
                nodo = cola.dequeue()
                if (nodo==Node):
                    print("La cola esta vacia....!")
                
    main()
