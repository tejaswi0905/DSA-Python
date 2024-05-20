arr = [2,1,5,2,3,2, 8]

def smallest_sub_array(arr, k):
    l = 0
    answer = float("inf")
    window_sum = 0

    for r in range(len(arr)):
        window_sum += arr[r]

        while window_sum >= k:
            cur_len = r - l + 1
            answer = min(answer, cur_len)
            window_sum -= arr[l]
            l += 1
    return answer

print(smallest_sub_array(arr, 7))
