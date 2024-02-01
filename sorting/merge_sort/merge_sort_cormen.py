def merge(A, p, q ,r):
    n1 = q - p + 1
    n2 = r - q
    L = list(range(1, n1))
    R = list(range(1, n2))
    for i in range(n1):
        L[i] = A[p + i - 1]
        print(f"L[i]: {L[i]}")
    for j in range(n2):
        R[j] = A[q + j]
        print(f"R[j]: {R[j]}")

    L[n1] = 80000000000
    L[n2] = 80000000000
    i = 1
    j = 1
    
    for k in range (p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort(A, p, r):
    if p < r:
        q = ((p + r)//2)
        if q > 1:
            q = q - 1
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q ,r)

unsorted_list = [5, 9, 3, 4, 8, 1]
print(f"unsorted: {unsorted_list}")
merge_sort(unsorted_list, 1, len(unsorted_list))
print(f"sorted: {unsorted_list}")
