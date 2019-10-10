#[ a [b [c d e f] g] [h [I [j [k l] m]]]] into List of [[a],[b,g],[c,d,e,f],[h],[I],[j,m],[K,L]]
# Try [[a][b,g,[c,d,e,f]],[h,[I,[j,m,[k,L]]]]] later

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
""" Not used Tree
class Tree:
    def __init__(self):
        self.main = []
        self.children = []
    
    def addmain(self, value):
        self.main = list(value)
        return True
    
    def getmain(self):
        return self.main
    
    def addchildren(self, value):
        self.children += [Tree()]
        self.children[len(self.children) - 1].addmain(value)
        return True

    def getchildren(self):
        return self.children
"""
def bc(x):
    A = LIFO()
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

def parse(x):
    if(bc(x)[0] == False):
        return False
    data = []
    if (x.count("[") == 0 and x.count("{") == 0 and x.count("(") != 0):
        data += ["(", ")"]
    elif (x.count("[") == 0 and x.count("{") != 0 and x.count("(") == 0):
        data += ["{","}"]
    elif (x.count("[") != 0 and x.count("{") == 0 and x.count("(") == 0):
        data += ["[", "]"]
    else:
        return False
    y = x
    i = 0
    j = 0
    while (i < len(x)):
        while (j < len(x)):
            if(bc(y[i:j + 1]) == True):
                y = y[i:j + 1]
                if ((y[i + 1:j]).count(data[0])):
                    z = (y[i + 1: j])[(y[i + 1:j]).index(data[0]) + 1:((y[i + 1:j])[::-1]).index(data[1])]
                    while (bc(x) == False):
                        z[0:len(z) - 1]
                    if (z.count(data[0]) > 0):
                        return [[(z.remove(z[z.index(data[0]):(z[::-1]).index(data[1]) + 1])).replace(" ", "")]] + parse((y[i+1:j])[(y[i+1:j]).index(z[len(z) - 1]):j])
                    else:
                        return [[z.replace(" ", "")]]
                else:
                    return [[y.replace(" ", "")]]
                
            j = j + 1
        i = i + 1

    



print(parse("[ a [b [c d e f] g] [h [I [j [k l] m]]]]"))