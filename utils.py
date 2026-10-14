def find_peak(nums):
    l, r = 0, len(nums) - 2
    
    while l <= r:
        mid = (l + r + 1) // 2
        
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid - 1
    
    return l


def binary_search_inc(nums, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    return -1


def binary_search_dec(nums, l, r, target):
    while l <= r:
        mid = (l + r) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            r = mid - 1  
        else:
            l = mid + 1
    
    return -1


def solve(A, B):
    peak = find_peak(A)

    ansl = binary_search_inc(A, 0, peak, B)
    if ansl != -1:
        return ansl
    ansr = binary_search_dec(A, peak + 1, len(A) - 1, B)
    return ansr

