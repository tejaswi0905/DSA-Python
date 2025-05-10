
'''
def quickSort(arr):
    if len(arr) < 1:
        return arr
    
    pivot = arr[-1]
    left = []
    right = []
    for i in arr:
        if i > pivot:
            right.append(i)
        elif i < pivot:
            left.append(i)
    leftMerge = quickSort(left)
    rightMerge = quickSort(right)
    return leftMerge + [pivot] + rightMerge
    
This is simply creating new lists and this is not advisable, Its better to update the current list instead of doing that!!    


    '''
    
    
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] < arr[pivot] and pivot - i >= 1:
            continue
        elif arr[i] < arr[pivot] and pivot - i <= 0:
            arr[i],arr[pivot] = arr[pivot],arr[i]
            pivot = i
        elif arr[i] > arr[pivot] and pivot - i >= 1:
            arr[i],arr[pivot] = arr[pivot],arr[i]
            pivot = i
        else:
            continue
    leftMerge = quickSort(arr[:pivot])
    rightMerge = quickSort(arr[pivot+1:])
    return leftMerge + [arr[pivot]] + rightMerge

    


arr = [1,2,8,0,9,5]
print(quickSort(arr))