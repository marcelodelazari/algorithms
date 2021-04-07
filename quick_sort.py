def Partition(l, left, right):
    pivot = l[left]
    i = left

    for j in range(left + 1, right + 1):
        if l[j] <= pivot:
            i += 1
            l[j], l[i] = l[i], l[j]

    l[i], l[left] = l[left], l[i]

    return i

def Quicksort(l, left, right):
    if left < right:
        pivot = Partition(l, left, right)
        Quicksort(l, left, pivot - 1)
        Quicksort(l, pivot + 1, right)
