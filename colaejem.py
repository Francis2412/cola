#Definicion de las estructuras de datos 

class Node:
    def __init__(self, data:int):
        self.data = data
        self.next = None

    def print(self):
        print(f"[{self.data}]")

class cola:
    def __init__(self, node:Node):
        self.front= None
        self.back= None

    def enqueue(self,new:Node):
        if self.front==None:
            self.front=new
            self.back=new
        else:
            self.back.next = new
            self.back=new

    def dequeue(self)->Node:
        if self.front ==None:
            return None
        else:
            node = Node()
            if node.next != None:
                self.front= self.front.next
            else:
                self.front == None
                self.back == None
            return node

    def clear(self)->list(Node):
        lista = []
        while self.front != None:
            n = self.dequeue()
            lista.append(Node(n.data))

        return lista