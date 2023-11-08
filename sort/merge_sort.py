def merge(A, p, q, r):
    size_left = q - p + 1
    size_right = r - q

    left = [0] * (size_left + 1)
    right = [0] * (size_right + 1)

    for i in range(size_left):
        left[i] = A[p + i]

    for j in range(size_right):
        right[j] = A[q + j + 1]

    left[size_left] = float('inf')
    right[size_right] = float('inf')

    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1

        else:
            A[k] = right[j]
            j += 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)



