class Coda():
    def __init__(self):
        self.coda=[]

    def enqueue(self,elemento):
        self.coda.append(elemento)

    def dequeue(self):
        if (len(self.coda)!=0):
            return self.coda.enqueue()
        else:
            None

    def print(self):
        print(self.coda)

class Pila():
    def __init__(self):
        self.pila=[]

    def push(self,elemento):
        self.pila.append(elemento)

    def pop(self):
        if (len(self.pila)!=0):
            return  self.pila.pop()
        else:
            None
            
    def print(self):
        print(self.pila)
