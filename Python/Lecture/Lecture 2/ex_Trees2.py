class Queue:
    def __init__(self):
        self.data = None

    def enqueue(self, x):
        self.data += [x]
        return True
    
    def dequeue(self):
        x = self.data[0]
        self.data = self.data[1:len(x)]
        return x

    def isempty(self):
        if self.data == []:
            return True
        return False
    
def traverse_breadth(T):
     x=Queue()
     x.enqueue(T)
     while x.isempty() == False:
          r=x.dequeue()
          print(r[0])
          for i in r[1:len(r)]:
               x.enqueue(i)