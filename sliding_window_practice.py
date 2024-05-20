a = [2,1,5,1,3,2]
k = 3
def max_sum_of_array(arr,k):
    windows_sum = 0
    answer_array = []
    left = 0

    for right in range(len(a)):
        windows_sum += arr[right]

        if right - left >= k-1:
            answer_array.append(windows_sum)
            windows_sum -= arr[left]
            left+=1
    return max(answer_array)

print(max_sum_of_array(a,k))

