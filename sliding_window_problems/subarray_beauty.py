#Leetcode 2653
def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
    ans = []
    arr = []
    dic = {}
    l = 0
    for i in range(-50,0):
        arr.append(i)
    for i in range(k):
        dic[nums[i]] = dic.get(nums[i], 0) + 1
    count = 0
    c = 0
    for j in arr:
        if j in dic:
            count += dic[j]
            if count>=x:
                c = j
                break
    ans.append(c)
    for r in range(k,len(nums)):
        dic[nums[r]] = dic.get(nums[r], 0) + 1
        dic[nums[l]] -= 1
        if dic[nums[l]] == 0:
            del dic[nums[l]]
        l += 1
        count = 0
        c = 0
        for j in arr:
            if j in dic:
                count += dic[j]
                if count>=x:
                    c = j
                    break
        ans.append(c)
    return ans