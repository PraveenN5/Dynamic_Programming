def insertionSort(L):
    if len(L) <= 1:
        return L
    
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key

    return L
    