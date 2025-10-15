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


def solve(q, arr):
    answer = []
    new_arr = []

    okay = False
    
    for ele in arr:
        if len(answer) == 0:
            new_arr.append(ele)
            answer.append("1")
            continue
        if (ele >= new_arr[-1]) and (not okay):
            new_arr.append(ele)
            answer.append("1")
            continue
        if (ele <= new_arr[0]) and (not okay):
            okay = True
            new_arr.append(ele)
            answer.append("1")
            continue
        if (okay == True and (ele >= new_arr[-1] and ele <= new_arr[0])):
            new_arr.append(ele)
            answer.append("1")
            continue
        answer.append("0")
    return "".join(answer)


def main():
    t = iinp()
    for _ in range(t):
        q = iinp()
        arr = ainp()
        # print_adv("The answer is ", solve, q, arr)
        print(solve(q, arr))

main()