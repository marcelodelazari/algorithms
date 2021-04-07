def partition(l, left, right):
    pivot = l[left]
    i = left

    for j in range(left + 1, right + 1):
        if l[j] <= pivot:
            i += 1
            l[j], l[i] = l[i], l[j]

    l[i], l[left] = l[left], l[i]

    return i

def quicksort(l, left, right):
    if left < right:
        pivot = partition(l, left, right)
        quicksort(l, left, pivot - 1)
        quicksort(l, pivot + 1, right)
