def countSort(A, exp):
    n = len(A)
    B = [0 for i in range(n)]
    C = [0 for i in range(10)]

    # Counting the number of occurrences of each digit.
    for i in range(n):
        C[(A[i]//exp)%10] += 1

    # Calculating the cumulative sum of the counts.
    for i in range(1, 10):
        C[i] += C[i-1]

    # Sorting the array according to the digit.
    for i in range(n-1, -1, -1):
        B[C[(A[i]//exp)%10]-1] = A[i]
        C[(A[i]//exp)%10] -= 1
    # Copying the sorted array to the original array.
    for i in range(n):
        A[i] = B[i]

    return A


def radixSort(A):
    max_element = max(A)
    exp = 1
    while max_element // exp > 0:
        countSort(A, exp)
        exp *= 10

    return A
