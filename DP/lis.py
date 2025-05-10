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

def lis(nums):
    is_ending_arr = [float("-inf")]
    length = 1
    current_end = 0
    
    attached_to = [-1] * len(nums)


    for i in range(len(nums)):
        if nums[i] > is_ending_arr[-1]:
            is_ending_arr.append(nums[i])
            current_end = i
            length += 1
        else:
            pos_of_ele = lower_bound(is_ending_arr, nums[i])
            is_ending_arr[pos_of_ele + 1] = nums[i]
    return is_ending_arr




print(lis([11,-1,0,1,5,7,10,9,6,8,9,2,3]))


