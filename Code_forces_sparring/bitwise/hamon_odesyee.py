'''
1847B, In this problem, I used a property that lets say we have a vaule x = a1 & a2 & a3, then if we extend this with a4 say y = a1 & a2 & a3 & a4, then y <= x. This is because when we do a bitwise "and" &, Lets say the first number is 13 = 1101, no matter the second number, the 1's in the 13 either remain or they become 0, but there is no way the 0's of 13 to become 1. Hence the resulting number of any x,  13 & x <= 13.

So Now in an array of numbers, we see how to split the array into max number of sub-arrays so that the sum of & values of each sub-array will be minimum. 

Firt we understood by adding new numbers to the current & processes, we can only reduce the value, so the smallest we can get is using the entire array. 

Lets say we anded the entire array and we got some a value x. i.e., x = a0 & a1 & a2 & ....
if x is not zero, then we can't split the array. lets say we have 5 elements in the array and their combined & values is 15. Then 15 = a0 & a1 & a2 & a3 & a4 & a5, if we split the array into 2 parts, (a1, a2, a3) and (a4, a5) As for the property of the & operator (a1 & a2 & a3) if >= 15 and 
(a4 & a5) >= 15 and by adding them we get 30. But if we took the entire array as a single group then we only get 15. Hence we can't split.

If the entire array's ended value is 0. Then we can look for continuous sub arrays with 0 as thier & value.
'''

# non-weighted graphs
from collections import defaultdict, deque
import math
import heapq as hq

from sys import setrecursionlimit
setrecursionlimit(10**6)

def print_adv(text, func, *args, **kwargs):
    print(text, end = ' ')
    result = func(*args, **kwargs)
    print(result)

def ainp():
    return list(map(int, input().split()))

def iinp():
    return int(input())



def build_graph_non_weighted(n, edges, is_directed = False, need_degree = False, zero_to_n = False):
    g = defaultdict(list)
    degree = None
    in_degree = None
    out_degree = None

    if not is_directed:
        if need_degree:
            if zero_to_n:
                degree = [0] * n
            else:
                degree = [0] * (n + 1)
            for u, v in edges:
                g[u].append(v)
                degree[u] += 1
                g[v].append(u)
                degree[v] += 1
        else:
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
    
            
    
    else:
        if need_degree:
            if zero_to_n:
                in_degree = [0] * n
                out_degree = [0] * n
            
            else:
                in_degree = [0] * (n + 1)
                out_degree = [0] * (n + 1)
            
            for u, v in edges:
                g[u].append(v)
                in_degree[v] += 1
                out_degree[u] += 1
        else:
            for u, v in edges:
                g[u].append(v)
    return (g, degree, in_degree, out_degree)

def solve(n, arr):
    if n == 1:
        return 1
    
    and_value = arr[0]
    for i in range(1, n):
        ele = arr[i]
        and_value = and_value & ele
    if and_value > 0:
        return 1
    
    answer = 0
    cur_and = arr[0]
    for i in range(n):
        ele = arr[i]
        cur_and = cur_and & ele
        if cur_and == 0:
            answer += 1
            if i < n - 1:
                cur_and = arr[i + 1]
            continue
    return answer

def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        arr = ainp()
        # print_adv("The answer is ", solve, n, arr)
        print(solve(n, arr))
main()