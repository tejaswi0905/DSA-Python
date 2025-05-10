def sum_of_digits(n):
    if n<10:
        return n
    digit = n%10
    remaining = n//10
    answer = digit + sum_of_digits(remaining)
    return answer

print(sum_of_digits(505))