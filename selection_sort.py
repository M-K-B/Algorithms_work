A = [4,65,3,3,4,5,64,6,7,88,54,4,3,32,12]


def selection_sort(A):
    for i in range(0, len(A)-1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        if min != i:
            A[i], A[min] = A[min], A[i]
    return A

print(selection_sort(A))