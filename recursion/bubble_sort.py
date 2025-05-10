

def bubble(arr, index, counter):
    if counter == 1:
        return
    if index + 1 == counter:
        bubble(arr, 0, counter - 1)
    else:
        if arr[index] > arr[index + 1]:
            arr[index],arr[index+1] = arr[index + 1], arr[index]
            bubble(arr, index + 1,counter)
        else:
            bubble(arr, index + 1, counter)
    
    
arr = [3,2,7,8,5]    
bubble(arr,0,len(arr))
print(arr)
        