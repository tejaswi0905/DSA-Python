def find(arr):
    if len(arr) == 1:
        return True
    answer = arr[0] <= arr[1] and find(arr[1:])
    return answer

print(find([1,2,3,4]))