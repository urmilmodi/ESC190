class graph:
    def __init__(self):
        self.data = []

    def addVertex(self, n):
        if n < 0:
            return -1
        for i in range(0, n, 1):
            self.data += [[]]
        return len(self.data)
    
    def addEdge(self, from_idx, to_idx, directed, weight):
        if from_idx < 0 or to_idx < 0 or not isinstance(directed, bool) or weight == 0 or from_idx > len(self.data) - 1 or to_idx > len(self.data) - 1:
            return False
        
        self.data[from_idx] += [[to_idx, weight]]
        if not directed:
            self.data[to_idx] += [[from_idx, weight]]
        
        return True

    def traverse(self, start, typeBreadth):
        if not (start == None or (start > -1 and start < len(self.data) - 1)):
            return []
        
        if start == None:
            if typeBreadth: # Breadth
                rv = []
                for v in range(0, len(self.data), 1):
                    t = []
                    for r in rv:
                        t += r
                    
                    if not v in t:
                        rv += [self.breadth(v)]
                        
                        for element in t:
                            if self.connectivity(v, element)[0]:
                                rv[-1] += [element]

            else: # Depth
                rv = [self.depth(0, [])]
                for v in range(0, len(self.data), 1):
                    t = []
                    for r in rv:
                        t += r
                
                    if not v in t:
                        rv += [self.depth(v, [])]

                        for element in t:
                            if self.connectivity(v, element)[0]:
                                rv[-1] += [element]
            return rv
        else:
            if typeBreadth: # Breadth
                return self.breadth(start)
            
            else: # Depth
                return self.depth(start, [])
    
    def depth(self, start, visited):

        if start in visited:
            return []
        
        visited += [start]

        rv = [start]
        
        for v in self.data[start]:
            rv += self.depth(v[0], visited)

        return rv

    def breadth(self, start):
        
        height = len(self.depth(start, [])) # max depth
        rv = []
        for level in range(1, height + 1, 1):
            rv += self.breadthlevel(start, level, list(rv))
        return rv

    def breadthlevel(self, start, level, visited):

        if start in visited and level == 1:
            return []
        visited += [start]
        if level == 1:
            return [start]
        else:
            rv = []
            for v in self.data[start]:
                rv += self.breadthlevel(v[0], level - 1, visited)
        
        return rv

    def connectivity(self, vx, vy):
        if vx in range(0, len(self.data), 1) and vx in range(0, len(self.data), 1):
            return [self.helpconnectivity(vx, vy, []), self.helpconnectivity(vy, vx, [])]
        else:
            return []

    def helpconnectivity(self, vx, vy, visited):
        
        rv = True if vx == vy else False
        
        if vx in visited:
            return rv
        
        visited += [vx]

        if not rv:
            for v in self.data[vx]:
                if self.helpconnectivity(v[0], vy, visited):
                    rv = True
                    break
        
        return rv

    def path(self, vx, vy):
        if vx in range(0, len(self.data), 1) and vy in range(0, len(self.data), 1):
            return [self.helppath(vx, vy, []), self.helppath(vy, vx, [])]
        else:
            return []

    def helppath(self, vx, vy, visited):

        rv = [vy] if vx == vy else []

        if vx in visited:
            return rv
        
        visited += [vx]

        if not vy in rv:
            x = None
            for v in [i[0] for i in self.data[vx]]:
                x = self.helppath(v, vy, visited)
                if vy in x:
                    rv = list(x)
                    break
        
        if vy in rv:
            if vx != vy:
                rv = [vx] + rv
        
        else:
            rv = []

        return rv