arr = [3, 1, 5, 4, 2]


def cyclic_sort(arr):
    n = len(arr)

    for i in range(n):
        cur = arr[i] - 1
        while cur != i:
            arr[cur], arr[i] = arr[i], arr[cur]
            cur = arr[i] - 1
    return arr


print(cyclic_sort(arr))
