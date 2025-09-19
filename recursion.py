def recursive_fn(num):
    if num==0:
        return 0

    prev_sum = recursive_fn(num - 1)
    answer = prev_sum + num
    return answer 

#num = int(input())
print(recursive_fn(5))
