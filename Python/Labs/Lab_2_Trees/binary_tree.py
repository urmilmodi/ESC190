from Queues import Queue

class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        if (type(x) == tree):
            self.store[1] = self.store[1] + [x]
        else:
            self.store[1] = self.store[1] + [tree(x)]
        return True

    def getMain(self):
        return self.store[0]

    def getChildren(self):
        return self.store[1]

    def Print_DepthFirst(self):
        self.PrintSpacing("")
        return True

    def PrintSpacing(self, spacing):
        print(spacing + str(self.store[0]))
        for i in self.getChildren():
            i.PrintSpacing(spacing + "   ")
        return True

    def Get_LevelOrder(self):
        x = Queue()
        x.enqueue(self.store)
        z = []
        y = x.dequeue()
        while (y != False):
            z += [y[0]]
            for i in y[1]:
                x.enqueue(i.store)
            y = x.dequeue()
        return z

    def height(self):
        height = 1
        y = []
        for i in self.getChildren():
            y += [i.height()]
        if (len(y) > 0):
            return height + max(y)
        return height

    def ConvertToBinaryTree(self):
        x = binary_tree(self.getMain())
        self.Convert(x)
        return x

    def Convert(self, Main):
        interator = Main
        if (self.getChildren() == []):
            return True
        for i in range(0, len(self.getChildren()), 1):
            temptree = binary_tree(self.getChildren()[i].getMain())
            self.getChildren()[i].Convert(temptree)
            if (i == 0):
                interator.AddLeft(temptree)
                interator = interator.getLeft()
            else:
                interator.AddRight(temptree)
                interator = interator.getRight()
        return True
        
class binary_tree:
    def __init__(self, x):
        self.store = [x, None, None]
    
    def AddLeft(self, x):
        if (type(x) == binary_tree):
            self.store[1] = x
        else:
            self.store[1] = binary_tree(x)
        return True

    def AddRight(self, x):
        if (type(x) == binary_tree):
            self.store[2] = x
        else:
            self.store[2] = binary_tree(x)
        return True

    def getMain(self):
        return self.store[0]

    def getLeft(self):
        return self.store[1]
    
    def getRight(self):
        return self.store[2]

    def Print_DepthFirst(self):
        return self.printSpace("")

    def printSpace(self, spacing):
        if (self.getMain() != None):
            print(spacing + str(self.getMain()))
        if (self.getLeft() != None):
            self.getLeft().printSpace(spacing + "   ")
        if (self.getRight() != None):
            self.getRight().printSpace(spacing + "   ")
        return True

    def Get_LevelOrder(self):
        if (self == None):
            return False
        h = self.height()
        x = []
        for i in range (1, h + 1, 1):
            x += self.GivenLevel(i)
        return x
        
    def GivenLevel(self, level):
        if level == 1:
            return [self.getMain()]
        elif level > 1:
            if (self.getLeft() != None and self.getRight() != None):
                return list(self.getLeft().GivenLevel(level - 1)) + list(self.getRight().GivenLevel(level - 1))
                
            elif (self.getLeft() != None):
                return list(self.getLeft().GivenLevel(level - 1))
            
            elif (self.getRight() != None):
                return list(self.getRight().GivenLevel(level - 1))
            
            else:
                return []
        
    def height(self):
        lheight = 0
        rheight = 0
        if (self.getLeft() != None):
            lheight = self.getLeft().height()
        
        if (self.getRight() != None):
            rheight = self.getRight().height()
        
        if (lheight > rheight):
            return lheight + 1
        else:
            return rheight + 1
    
    def ConvertToTree(self):
        if (self.getRight() == None):
            x = tree(self.getMain())
            x.AddSuccessor(self.getLeft().getMain())
            self.getLeft().Convert(x)
            return [True, x]
        else:
            return [False]
    
    def Convert(self, Main):
        y = self
        while (y != None):
            if (y.getLeft() == y.getRight() == None):
                break
            Main.AddSuccessor(y.getRight().getMain())
            if (y.getLeft() != None):
                temp = None
                for i in range (0, len(Main.getChildren()), 1):
                    if (Main.getChildren()[i].getMain() == y.getRight().getMain()):
                        temp = Main.getChildren()[i - 1]
                if (temp != None):
                    temp.AddSuccessor(y.getLeft().getMain())
                    y.getLeft().Convert(temp)
            y = y.getRight()
        return Main