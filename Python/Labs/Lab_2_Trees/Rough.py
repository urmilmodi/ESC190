    
"""
    def Convert(self, Main):
        x = Main
        y = self
        while (True):
            if (y.getLeft() != None):
                temp = tree(y.getLeft().getMain())
                y.getLeft().Convert(temp)
                x.AddSuccessor(temp)
            if (y.getRight() != None):
                x.AddSuccessor(y.getRight().getMain())
            if (y.getLeft() == y.getRight() == None):
                break
            else:
                y = y.getRight()
        return x

"""


"""
    def getMain(self):
        return self.store[0]

    def getLeft(self):
        return self.store[1]
    
    def getRight(self):
        return self.store[2]

    def AddSuccessor(self, x):
        if (self == None):
            return False
        if (self.getLeft() == None):
            self.AddLeft(x)
            return True
        elif(self.getLeft() == None):
            self.AddRight(x)
            return True
        else:
            if (self.getLeft().getLeft() == None or self.getLeft().getRight() == None):
                self.getLeft().AddSuccessor(x)
            elif(self.getRight().getLeft() == None or self.getRight().getRight() == None):
                self.getRight().AddSuccessor(x)
            return True

    def AddLeft(self,x):
        if (type(x) is binary_tree):
            self.store[1] = x
        else:
            self.store[1] = binary_tree(x)
        return True

    def AddRight(self,x):
        if (type(x) is binary_tree):
            self.store[2] = x
        else:
            self.store[2] = binary_tree(x)
        return True

    def Get_LevelOrder(self):
        if (self.getMain() == None): # fix this shit
            return False
        h = self.height()
        x = []
        for i in range (1, h + 1, 1):
            x += self.GivenLevel(i)
        return x
        
    def GivenLevel(self, level):
        if self.getMain() == None: # fix this shit
            return False
        if level == 1:
            return [self.getMain()]
        elif level > 1:
            if (self.getLeft() != None and self.getRight() != None):
                return list(self.getLeft().GivenLevel(level - 1)) + list(self.getRight().GivenLevel(level - 1))
                
            elif (self.getLeft() != None):
                return list(self.getLeft().GivenLevel(level - 1))
            
            elif (self.getRight() != None):
                return list(self.getRight().GivenLevel(level - 1))
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
        if (self == None):
            return [False, None]
        x = self.Get_LevelOrder()
        y = tree(x[0])
        for i in range (1, len(x), 1):
            y.AddSuccessor(x[i])
        return [True, y]
"""
"""
    def Print_DepthFirst(self):

        if (self.store == None):
            return False
        h = self.height()
        x = []
        for i in range (1, h + 1, 1):
            x += ["Row " + str(i)]
            x += self.GivenLevel(i)
        return x
        
    def Get_LevelOrder(self):
        if (self.store == None):
            return False
        h = self.height()
        x = []
        for i in range (1, h + 1, 1):
            x += self.GivenLevel(i)
        return x

    def GivenLevel(self, level):
        if (self == None):
            return False
        if (level == 1):
            return [self.getmain()]
        elif level > 1:
            x = []
            for i in self.store[1]:
                x += [i.getmain()]
            return x
        
    def ConvertToBinaryTree(self):
        x = self.Get_LevelOrder()
        y = binary_tree(x[0])
        for i in range(1, len(x), 1):
            y.AddSuccessor(x[i])
        return y

        
    def Get_LevelOrder(self):
        if (self.store == None):
            return False
        h = self.height()
        x = []
        for i in range (1, h + 1, 1):
            x += self.GivenLevel(i)
        return x

    def GivenLevel(self, level):
        if (self == None):
            return False
        if (level == 1):
            return [self.getMain()]
        elif level > 1:
            x = []
            for i in self.getChildren():
                x += [i.getMain()]
            return x
"""
#print(x.ConvertToBinaryTree().Get_LevelOrder())
"""
    def ConvertTest(self, number):
        if (number < 0):
            return False
        if (number == 0 and self.getRight() != None):
            return False
        Left = True
        Right = True
        if (self.getLeft() != None):
            Left = self.getLeft().ConvertTest(number + 1)
        if (self.getRight() != None):
            Right = self.getRight().ConvertTest(number + 1)
        if (Left == True and Right == True):
            return True
"""