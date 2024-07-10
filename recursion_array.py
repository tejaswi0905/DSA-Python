def recursive_fn(nums):
    if len(nums)==1:
        return nums
    reversed_array = recursive_fn(nums[1:])
    current_ele = nums[0]
    answer_array = reversed_array + [current_ele]
    return answer_array

    


def fib(n):
    memo = {0:0, 1:1}

    def rec_func(n, memo):
        if n in memo:
            return memo[n]
        answer = rec_func(n - 1, memo) + rec_func(n - 2, memo)
        memo[n] = answer
        return answer
    rec_func(n, memo)
    print(memo)
    return memo[n]



print(fib(100))

