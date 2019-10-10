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

def hanoi(n, start, temp, final):
    if n > 0:
        hanoi(n - 1, start, final, temp)
        final.append(start.pop())
        hanoi(n - 1, temp, start, final)
        print(start,temp,final)
    return True