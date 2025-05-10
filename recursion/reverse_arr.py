def reverse(arr):
    if len(arr) == 1:
        return arr
    new = [arr[-1]] + reverse(arr[:len(arr)-1])
    return new


def reverse_arr(arr):
    if len(arr) == 1:
        return arr   
    
    first_ele = arr[0]
    rest_arr = arr[1:]
    
    print(first_ele, rest_arr)
    
    reversed_arr = reverse_arr(rest_arr)
    reversed_arr.append(first_ele)
    
    print(reversed_arr)
    return reversed_arr

print(reverse_arr([1,2,3,4]))