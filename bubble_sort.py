A = [7,84,4,53,3,35434,2234,53,23,2,44,3,32,21,23,3,22,3,45,6,7,5,56,75,3,56,54,3,45,4,44,55,4]

def bubble_sort(A):
    
    sort = True

    while sort is True:
        sort = False
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                sort = True
                A[i], A[i+1] = A[i+1], A[i]
    return A


print(bubble_sort(A))