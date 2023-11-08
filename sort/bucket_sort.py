# Bucket Sort
def insertionSortForBucket(L):
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

def bucketSort(A):
    n = len(A)
    B = [[] for i in range(n)]
    for i in range(n):
        index = min(int(n * A[i]), n - 1)  # Clamp the index to be within [0, n-1]
        B[index].append(A[i])

    for i in range(n):
        insertionSortForBucket(B[i])

    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1

    return A

