def binary_search(arr, k):
    l = 0
    r = len(arr) - 1

    while (r-l) > 1:
        m = (l + r) // 2
        if arr[m] > k:
            r = m - 1
        else:
            l = m
    
    if arr[r] <= k:
        return r
    if arr[l] <= k:
        return l
    return -1

arr = [2,5,9,11,16,17]
k = 1
print(binary_search(arr, k))