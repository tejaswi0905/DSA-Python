

# def selection(arr,index):
#     if index == 0:
#         return
#     maxi = 0
#     maxi_index = 0
#     for i in range(index+1):
#         if arr[i] > maxi:
#             maxi = arr[i]
#             maxi_index = i
#     arr[maxi_index],arr[index] = arr[index],arr[maxi_index]
#     selection(arr,index-1)
    

def selection2(arr,last,c,maxi):
    if last == 0:
        return
    
    if c > last:
        arr[c-1],arr[maxi] = arr[maxi],arr[c-1]
        selection2(arr,last-1,0,0)
    else:
        if arr[c] > arr[maxi]:
            selection2(arr,last,c+1,c)
        else:
            selection2(arr,last,c+1,maxi)
    
    
arr = [8,3,2,1,9,7]
arr2 = [4,3,2,1]
selection2(arr,len(arr)-1,0,0)
print(arr)
    

    
    