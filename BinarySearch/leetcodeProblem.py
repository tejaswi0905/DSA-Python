class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()

        pf_sum_array = []
        current_sum = 0
        for ele in nums:
            current_sum += ele
            pf_sum_array.append(current_sum)
        n = len(nums)
        answer_array = []

        for ele in queries:
            idx = self.binary_search(pf_sum_array, ele, 0, n - 1)
            answer_array.append(idx + 1)
        return answer_array

    def binary_search(self, arr, key, l, r):
        while (r - l) > 1:
            mid = (r + l) // 2
            print(f"{r}, {l}, {mid}, ", end = ' ')
            print(arr[mid])
            if arr[mid] > key:
                r = mid - 1
            else:
                l = mid
        if arr[r] <= key:
            return r
        if arr[l] <= key:
            return l
        return -1

nums = [4,5,2,1]
queries = [3,10,21]
solutionObject = Solution()
answer_array = solutionObject.answerQueries(nums, queries)
print(answer_array)