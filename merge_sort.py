L = [5,6,4,3,34,43,4,553,3]


def merge_sort(L):
    if len(L) <= 1:
         return L

    a = L[0: int(len(L) / 2)]
    b = L[ int(len(L) / 2): len(L)]
    a = merge_sort(a)
    b = merge_sort(b)

    return merge(a, b)

def merge(a,b):
    out = []
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
        k += 1
    while i < len(a):
        out.append(a[i]) 
        i += 1
        k += 1
    while j < len(b):
        out.append(b[j])  
        j += 1
        k += 1
    return out 

print(merge_sort(L))
