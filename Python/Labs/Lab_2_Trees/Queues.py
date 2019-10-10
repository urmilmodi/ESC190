class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        self.data += [value]
        return True

    def dequeue(self):
        if (self.data == []):
            return False
        x = self.data[0]
        del self.data[0]
        return x

    def isempty(self):
        if (self.data == []):
            return True
        return False