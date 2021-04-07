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

def median_of_three_partition(l, left, right):
    mid = (left + right) // 2

    if l[right] < l[left]:
        l[left], l[right] = l[right], l[left]
    if l[mid] < l[left]:
        l[mid], l[left] = l[left], l[mid]
    if l[right] < l[mid]:
        l[right], l[mid] = l[mid], l[right]

    l[mid], l[right] = l[right], l[mid] #coloca o pivot no final

    pivot = l[right]
    i = left

    for j in range(left, right):
        if l[j] <= pivot:
            l[j], l[i] = l[i], l[j]
            i += 1

    l[right], l[i] = l[i], l[right]

    return i

def median_of_three_quicksort(l, left, right):
    if left < right:
        pivot = median_of_three_partition(l, left, right)
        median_of_three_quicksort(l, left, pivot - 1)
        median_of_three_quicksort(l, pivot + 1, right)

def threeway_partition(l, left, right):
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

def threeway_quicksort(l, left, right):
    if left < right:
        left_pivot, right_pivot = threeway_partition(l, left, right)
        threeway_quicksort(l, left, left_pivot - 1)
        threeway_quicksort(l, right_pivot + 1, right)
