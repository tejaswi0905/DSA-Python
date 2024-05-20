nums = ["a", "b", "c", "d", "e","f"]
# i = 0
# j = len(nums)-1
# while i<j:
#     nums[i],nums[j] = nums[j],nums[i]
#     i+=1
#     j-=1
# print(nums)
# a = nums
# b = []
# for i in a:
#     if i.isalpha():
#         b.append(i)
# b = b[::-1] // we are using an extra array of size n in the solution.
# k = 0
# for i in range(len(nums)):
#     if nums[i].isalpha():
#         nums[i]=b[k]
#         k+=1

# print(nums)

# Space, if we use any extra data-structure with unlimited or n enteries, then we are using o(n) space.
# In-place, use only the input array. We have a const space.

# Do it in o(n) time and constant space.



