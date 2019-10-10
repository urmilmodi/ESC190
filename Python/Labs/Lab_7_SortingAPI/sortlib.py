import math

def selection_sort(u):
    for i in range(0, len(u), 1):

        minv = min(u[i:len(u)])
        if (minv != u[i]):
            u[u.index(minv, i, len(u))] = u[i]
            u[i] = minv
    return True

def heapify(u):
    reheapify(u, len(u) - 1)
    return True

def reheapify(u, end):
    for i in range(end, -1, -1):
        j = i
        while j != 0:
            if u[j] > u[math.floor(j/2)]:
                u[j], u[math.floor(j/2)] = u[math.floor(j/2)], u[j]
                j = math.floor(j/2)
            else:
                break
    return True

def heap_sort(u):
    for i in range(len(u) - 1, -1, -1):
        reheapify(u, i)
        u[0], u[i] = u[i], u[0]

    return True

def merge_sort(u):
    if len(u) > 1:
        middle = len(u)//2
        L = u[:middle]
        R = u[middle:]
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                u[k] = L[i]
                i += 1
            else:
                u[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L): 
            u[k] = L[i]
            i += 1
            k += 1
          
        while j < len(R): 
            u[k] = R[j]
            j += 1
            k += 1

    return True

def quick_sort(u,ini,fin):
    if ini < fin:
        pIndex = partition(u,ini,fin)
        quick_sort(u, ini, pIndex - 1)
        quick_sort(u, pIndex + 1, fin)
    return True

def partition(u,ini,fin):
    pIndex = ini - 1
    pivot = u[fin]
    for i in range(ini, fin, 1):
        if u[i] < pivot:
            pIndex += 1
            temp = u[i]
            u[i] = u[pIndex]
            u[pIndex] = temp
    pIndex += 1
    temp = u[fin]
    u[fin] = u[pIndex]
    u[pIndex] = temp
    return pIndex