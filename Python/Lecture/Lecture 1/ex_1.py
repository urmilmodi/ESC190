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

def main(x):
    A = LIFO()
    r = True
    for i in range(0, len(x), 1):
        # {}
        if (x[i] == "{"):
            A.push(x[i])
        elif (x[i] == "}"):
            r = A.pop()
            if (r != "{"):
                return [False, i]
        
        #()
        elif (x[i] == "("):
            A.push(x[i])
        elif (x[i] == ")"):
            r = A.pop()
            if (r != "("):
                return [False, i]
        
        #[]
        elif (x[i] == "["):
            A.push(x[i])
        elif (x[i] == "]"):
            r = A.pop()
            if (r != "["):
                return [False, i]
    
    if(A.pop() == False):
        return [True,0]
    else:
        return [False, len(x) - 1]