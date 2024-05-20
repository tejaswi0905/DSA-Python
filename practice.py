nums = [1,2,3,4,5,6]

# [1, 2, 3] [2, 3, 4], [2,3,4] [3,4,5]

def sum_of_arrays(arr, k):
    # k = 3
    window_sum = 0
    answer_array = []
    left = 0

    # right - left = size of the window. k - 1

    for right in range(len(arr)):
        window_sum += arr[right]

        if right - left >= k - 1:
            answer_array.append(window_sum // k)
            window_sum -= arr[left]
            left += 1 # we do this to keep the window size.
    return answer_array

print(sum_of_arrays(nums, 3))



    
    



    