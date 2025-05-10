

def merge(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge(arr[:mid])
        right = merge(arr[mid:])
        ans = []
        m,n = 0,0
        while m < len(left) and n < len(right):
            if left[m] < right[n]:
                ans.append(left[m])
                m += 1
            else:
                ans.append(right[n])
                n += 1
        ans += left[m:]
        ans += right[n:]
        return ans
    
    

'''The above one you see is where you create a new array and then merge the left
ones and right ones into this array but now the below code will be showing you how to manipulate
the given array itself instead of creating a new one'''




def merge2(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge2(arr[:mid])
        right = merge2(arr[mid:])
        x = 0
        m,n = 0,0
        while m < len(left) and n < len(right):
            if left[m] < right[n]:
                arr[x] = left[m]
                m += 1
            else:
                arr[x] = right[n]
                n += 1
            x += 1
        count = len(arr)
        while count > x:
            arr.pop()
            count -= 1  
        arr += left[m:]
        arr += right[n:]
        return arr




    
arr = [4,3,7,6,1,0]
merge2(arr)
print(arr)