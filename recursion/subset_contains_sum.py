def contains_sum(arr,target):
    n = len(arr)

    memory_set = [[-1] * (target + 1) for _ in range(len(arr) + 1)]

    def rec(l, sum_left):
        if sum_left < 0:
            return False
        if l == n:
            if sum_left == 0:
                return True
            return False

        if memory_set[l][sum_left] != -1:
            return memory_set[l][sum_left]
        
        answer = rec(l + 1, sum_left - arr[l]) or rec(l + 1, sum_left)

        memory_set[l][sum_left] = answer
        return answer
    
    answer = rec(0, target)
    print(memory_set)
    return answer





arr = [1,2,5,9]
target = 8

print(contains_sum(arr,target))