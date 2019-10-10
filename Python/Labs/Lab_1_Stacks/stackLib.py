class LIFO:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        self.data += [value]
        return True

    def pop(self):
        if (self.data == []):
            return False
        x = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        return x