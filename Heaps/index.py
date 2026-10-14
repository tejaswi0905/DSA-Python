import heapq


# def get_all(nums):
#     n = len(nums)
#     ans = []
#     ans1 = []
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             sub_sum = sum(nums[i:j])
#             ans1.append(sub_sum)
#     ans1.sort()
#     min_heap = [(nums[i], i) for i in range(n)]
#     hq.heapify(min_heap)
#     while min_heap:
#         val, idx = hq.heappop(min_heap)
#         ans.append(val)
#         if idx < n - 1:
#             val += nums[idx + 1]
#             hq.heappush(min_heap, (val, idx + 1))
#     print(ans, ans1)


# nums = [3, 1, 2, 4]
# print(get_all(nums))
class Solution:
    def minimumDeviation(self, nums):
        minHeap, heapMax = [], 0

        for n in nums:
            tmp = n
            while n % 2 == 0:
                n //= 2
            minHeap.append((n, max(tmp, 2 * n)))
            heapMax = max(heapMax, n)

        res = float("inf")
        heapq.heapify(minHeap)

        while len(minHeap) == len(nums):
            n, nMax = heapq.heappop(minHeap)
            res = min(res, heapMax - n)

            if n < nMax:
                heapq.heappush(minHeap, (n * 2, nMax))
                heapMax = max(heapMax, n * 2)

        return res


nums = [4, 7, 8]
print(Solution().minimumDeviation(nums))
