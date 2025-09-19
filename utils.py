import math
def but_stops(nums):
    total = sum(nums)
    min_num = max(nums)

    def find_factors(num, min_num):
        factors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if (i >= min_num):
                    factors.append(i)
                if (num // i >= min_num):
                    factors.append(num//i)
        return sorted(factors)
    factors = find_factors(total, min_num)

    def canDivideIntoGroups(nums, k):
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum == k:
                cur_sum = 0
            if cur_sum > k:
                return False
        return cur_sum == 0
    
    answer = []
    for fact in factors:
        if canDivideIntoGroups(nums, fact):
            answer.append(fact)
    return answer


ans = but_stops([1, 2, 1, 1, 1, 2, 1, 3])
print(ans)


    
                
