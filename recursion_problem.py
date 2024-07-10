n = 16

def rec(nums):
    if nums>n:
        return False
    if nums==n:
        return True
    val = 2*nums
    rec(nums)
    
    

print(rec(2))