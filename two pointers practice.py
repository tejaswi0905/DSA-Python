nums = ["!","b","#","c","*","d","!","e","f","$"]
print(nums)
i = 0
j = len(nums)-1
while(i<j):
    if nums[i].isalpha()==False:
        i+=1
    if nums[j].isalpha()==False:
        j-=1
    if nums[i].isalpha()== True and nums[j].isalpha()==True:
        nums[i],nums[j] = nums[j],nums[i]
        i += 1
        j -= 1
print(nums)