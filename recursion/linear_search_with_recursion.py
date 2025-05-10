def search(arr, index, target):
    if index == len(arr) - 1:
        if arr[index] != target:
            return False
        else:
            return True
    
    if arr[index] == target:
        return True
    else:
        return search(arr, index + 1, target)
    
    
    
def search2(arr, index, target):
    if index == len(arr):
        return []
    
    if arr[index] == target:
        ans = []
        ans.append(index)
        another = search2(arr, index+1, target)
        for i in another:
            ans.append(i)
        return ans
    else:
        return search2(arr, index+1, target)
        

print(search2([1,2,4,4,7,4,4,4,11], 0, 4))
    
    
    
'''
There are multiple ways to do a problem and I am going to put them down here for your future reference:

def search(arr, index, target):
    if index == len(arr) - 1:
        if arr[index] != target:
            return -1
        else:
            return index
    
    if arr[index] == target:
        return index
    else:
        return search(arr, index + 1, target)
        
    --> The above method directly returns index without any difficulties and processes in the body
        
        
def search(arr, index, target):
    if index == len(arr) - 1:
        if arr[index] != target:
            return -1
        else:
            return index
    
    return arr[index] == target & search(arr, index + 1, target)
   
   --> This returns the index as well but uses bitwise operation with future recursive calls
   
   

def search(arr, index, target):
    if index == len(arr) - 1:
        if arr[index] != target:
            return False
        else:
            return True
    
    return arr[index] == target or search(arr, index + 1, target)
    
  --> Returns the boolean part but uses logical operation of or with future recursive calls
  
  
=> If you want multiple indices for the repeated target elements in the array, you can simply create an array in the global and 
just add the indices in the new array whenever you find the target and in the end you can simply return.

'''


