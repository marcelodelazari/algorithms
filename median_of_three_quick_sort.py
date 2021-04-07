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
