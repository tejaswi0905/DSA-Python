'''1847A, In this problem there is a cool idea, we are going to take the difference between two adj-elements, and if we make a division in them, their sum won't be in the final answer, that is the key idea, lets say we have an array of a1, a2, a3 and a4. Now the sum is |a1 - a2| + |a2 - a3| + |a3 - a4| + |a4 - a5|, Now if we had a division between 2 and 3 then then |a2 - a3| will no longer contribute to the actual answer. Since we have to minimize the sum, we look at all the avaliable adj-differences, sort them, and since we have to make k partitions we can make k - 1 divisions, so we remove the largest k - 1 elements. Initially there are n - 1 adj-elements, so we can add the first (n - 1) - (k - 1) elements. 

lets dry run a test case
                arr = 1   9   12   4   7   2 and k = 3
the differences are     8   3    8   3   5 so if we sort the differences we get = 3 3 5 8 8 so 
now we need to take the (n - 1) - (k - 1) differences, so n - 1 = 5 and k - 1 = 2 so we need to take the first 3 differences in the answer, hence the answer is 3 + 3 + 5 = 11

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


def solve(n, k, arr):
    if n == 1:
        return 0
    diff_arr = []
    for i in range(1, n):
        diff_arr.append(abs(arr[i] - arr[i - 1]))
    diff_arr.sort()
    count_needed = (n - 1) - (k - 1)
    answer = 0
    for i in range(count_needed):
        answer += diff_arr[i]
    return answer



def main():
    t = iinp()
    for _ in range(t):
        n, k = ainp()
        arr = ainp()
        # print_adv("The answer if ", solve, n, k, arr)
        print(solve(n, k, arr))
main()