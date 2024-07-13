def celing(arr, k):
    l = 0
    r = len(arr) - 1

    while ((r - l) > 1):
        m = (l + r) // 2
        if arr[m] < k:
            l= m + 1
        else:
            r = m

    if arr[l] >= k:
        return l
    if arr[r] >= k:
        return r
    return -1

# arr = [-5,2,3,6,9,10,11,14,15]
# answer_ceil = celing(arr, 5)
# print(answer_ceil, end = ' ')

def floor(arr, k):
    l = 0
    r = len(arr) - 1

    while ((r - l) > 1):
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

# answer_floor = floor(arr, -6)
# print(answer_floor)


def freq_start(arr, k):
    l = 0
    r = len(arr) - 1

    while ((r - l) > 1):
        m = (l + r) // 2
        if arr[m] > k:
            r = m - 1
        elif arr[m] < k:
            l = m + 1
        else:
            r = m
    if arr[l] == k:
        return l
    if arr[r] == k:
        return r
    else:
        return -1

# print(freq_start([1,2,3,4,4,4,5,6,7], 10))

def freq_last(arr, k):
    l = 0
    r = len(arr) - 1

    while ((r - l) > 1):
        m = (l + r) // 2
        if arr[m] > k:
            r = m - 1
        elif arr[m] < k:
            l = m + 1
        else:
            l = m
    if arr[r] == k:
        return r
    elif arr[l] == k:
        return l
    else:
        return -1
# print(freq_last([1,2,3,4,4,4,5,6,7], 10))


def lower_bound(arr, k):
    l = 0
    r = len(arr) - 1

    while (r - l) > 1:
        mid = (r + l) // 2
        if arr[mid] > k:
            r = mid - 1
        else:
            l = mid
    if arr[r] <= k:
        return r
    if arr[l] <= k:
        return l
    return -1

print(lower_bound([1,2,3,4,4,5,6,7], 0))


