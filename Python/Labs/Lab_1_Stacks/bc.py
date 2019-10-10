from stackLib import LIFO

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