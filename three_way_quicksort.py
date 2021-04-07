def ThreewayPartition(l, left, right):
    pivot = l[left]
    i = left

    for j in range(left + 1, right + 1):
        if l[j] <= pivot:
            i += 1
            l[j], l[i] = l[i], l[j]

    l[i], l[left] = l[left], l[i]

    t = i
    while l[t] == pivot:
        t -= 1

    for j in range(t, left - 1, -1):
        if l[j] == pivot:
            l[j], l[t] = l[t], l[j]
            t -= 1

    return t + 1, i

def ThreewayQuicksort(l, left, right):
    if left < right:
        left_pivot, right_pivot = Threeway_Partition(l, left, right)
        Threeway_Quicksort(l, left, left_pivot - 1)
        Threeway_Quicksort(l, right_pivot + 1, right)
