def search(arr, s, e, target):
    if s>e:
        return -1
    mid = (e-s) + s//2
    if arr[mid] == target:
        return mid
    if arr[s] <= arr[mid]:
        if target >= arr[s] and target <= arr[mid]:
            return search(arr,s,mid-1,target)
        else:
            return search(arr,mid+1,e,target)
    if target >= arr[mid] and target <= arr[e]:
        return search(arr,mid+1,e,target)
    
    return search(arr,s,mid-1,target)
        
        
print(search([5,6,7,8,9,1,2,3],0,7,6))