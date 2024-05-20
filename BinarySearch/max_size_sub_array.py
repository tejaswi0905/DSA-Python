def max_size_sub_array(arr, b):
    def predicate_function(arr, k, b, n):
        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += arr[right]
            if right >= k - 1:
                if cur_sum > b:
                    return False
                cur_sum -= arr[left]
                left += 1
        return True
    n = len(arr)
    l = 1
    r = n
    while (r - l) > 1:
        mid = (l + r) // 2
        print(r, l, mid, end = ' ')
        is_possible = predicate_function(arr, mid, b, n)
        print(is_possible)
        if is_possible == True:
            l = mid
        else:
            r = mid - 1

    if predicate_function(arr, r, b, n) == True:
        return r
    return l

result = max_size_sub_array([3,2,5,4,6,3,7,2], 20)
print(result)