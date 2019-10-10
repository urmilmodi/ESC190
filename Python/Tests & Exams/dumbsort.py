def dumbsort(L):
    M = []
    for j in range(0, len(L), 1):
        minv = minvalue(L, M)
        if not minv in M:
            M += [minv]
    return M

def minvalue(L, M):
    # Find the Max Value
    minv = L[0]
    for i in L:
        if minv < i:
            minv = i
    """
    You find the Max Value, so you know for a fact that it will cycle to the newest min value in the for loop
    """
    # The Min Value thats not in M
    for i in L:
        if minv > i and not i in M:
            minv = i
    return minv

print(dumbsort([-5,-2,-4,-6,-8,-9,-2]))
print(dumbsort([5,2,4,6,8,9,2]))