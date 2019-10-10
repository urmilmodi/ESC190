def sortr(L): 
  
    maxv = L[0]
    for i in L:
        if i > maxv:
            maxv = i

    exp = 1
    while maxv/exp > 0: 
        new = [0]*len(L) 
        tally = [0]*10
    
        for i in range(0, len(L), 1): 
            tally[int((L[i]/exp)%10)] += 1
    
        for i in range(1, 10, 1): 
            tally[i] += tally[i-1] 
    
        i = len(L) - 1
        while i > -1:
            new[tally[int((L[i]/exp)%10)] - 1] = L[i] 
            tally[int((L[i]/exp)%10)] -= 1
            i -= 1
        
        for i in range(0, len(L), 1): 
            L[i] = new[i]
        
        exp *= 10