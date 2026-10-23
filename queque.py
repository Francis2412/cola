# Definición de las estructuras de datos
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

    def print_node(self):
        print(f"[{self.data}]")

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

class Cola:
    def __init__(self):
        self.front = None
        self.back = None
        
    def enqueue(self,new:Node):
        if self.front==None:
            self.front=new
            self.back=new
        else:
            self.back.next = new  
            self.back = new       
            
    def dequeue(self)->Node:
        node=self.front
        if self.front==None:
            return None
        else:
            node=Node()
            if self.front.next!=None:
                self.front=self.front.next
            else:
                self.front=None
                self.back=None
            return
    
    def clear(self)->list[Node]:
        lista =[]
        while self.front!=None:
            n = self.dequeue()
            lista.append(Node(n.data))
        return lista
     
    def peek(self)->tuple[Node,Node]:
        if self.front==None:
            return None
        else:
            front = self.front
            back = self.back
            return Node(front.data), Node(back.data)