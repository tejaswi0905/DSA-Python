# # non-weighted graphs
# from collections import defaultdict, deque
# import math
# import heapq as hq

# from sys import setrecursionlimit
# setrecursionlimit(10**6)

# def print_adv(text, func, *args, **kwargs):
#     print(text, end = ' ')
#     result = func(*args, **kwargs)
#     print(result)

# def ainp():
#     return list(map(int, input().split()))

# def iinp():
#     return int(input())



# def build_graph_non_weighted(n, edges, is_directed = False, need_degree = False, zero_to_n = False):
#     g = defaultdict(list)
#     degree = None
#     in_degree = None
#     out_degree = None

#     if not is_directed:
#         if need_degree:
#             if zero_to_n:
#                 degree = [0] * n
#             else:
#                 degree = [0] * (n + 1)
#             for u, v in edges:
#                 g[u].append(v)
#                 degree[u] += 1
#                 g[v].append(u)
#                 degree[v] += 1
#         else:
#             for u, v in edges:
#                 g[u].append(v)
#                 g[v].append(u)
    
            
    
#     else:
#         if need_degree:
#             if zero_to_n:
#                 in_degree = [0] * n
#                 out_degree = [0] * n
            
#             else:
#                 in_degree = [0] * (n + 1)
#                 out_degree = [0] * (n + 1)
            
#             for u, v in edges:
#                 g[u].append(v)
#                 in_degree[v] += 1
#                 out_degree[u] += 1
#         else:
#             for u, v in edges:
#                 g[u].append(v)
#     return (g, degree, in_degree, out_degree)


# def solve(n, que):
#     par = [i for i in range(n + 1)]
#     meta = {i:1 for i in range(1, n + 1)}
#     answer = []

#     def find(x):
#         if x != par[x]:
#             par[x] = find(par[x])
#         return par[x]
#     def union(n1, n2):
#         p1, p2 = find(n1), find(n2)
#         if p1 == p2:
#             return False
#         if meta[p1] < meta[p2]:
#             p1, p2 = p2, p1
#         meta[p1] += meta[p2]
#         par[p2] = p1
#         return True
#     for query in que:
#         if query[0] == "M":
#             n1, n2 = int(query[1]), int(query[2])
#             union(n1, n2)
#         if query[0] == "Q":
#             n = int(query[1])
#             p = find(n)
#             answer.append(meta[p])
#     return answer
            

# def main():
#     n, q = ainp()
#     que = []
#     for _ in range(q):
#         query = list(input().split())
#         que.append(query)
    
#     answer = solve(n, que)
#     for val in answer:
#         print(val)


# main()

# non-weighted graphs
# from collections import defaultdict, deque
# import math
# import heapq as hq

# from sys import setrecursionlimit
# setrecursionlimit(10**6)

# def print_adv(text, func, *args, **kwargs):
#     print(text, end = ' ')
#     result = func(*args, **kwargs)
#     print(result)

# def ainp():
#     return list(map(int, input().split()))

# def iinp():
#     return int(input())



# def build_graph_non_weighted(n, edges, is_directed = False, need_degree = False, zero_to_n = False):
#     g = defaultdict(list)
#     degree = None
#     in_degree = None
#     out_degree = None

#     if not is_directed:
#         if need_degree:
#             if zero_to_n:
#                 degree = [0] * n
#             else:
#                 degree = [0] * (n + 1)
#             for u, v in edges:
#                 g[u].append(v)
#                 degree[u] += 1
#                 g[v].append(u)
#                 degree[v] += 1
#         else:
#             for u, v in edges:
#                 g[u].append(v)
#                 g[v].append(u)
    
            
    
#     else:
#         if need_degree:
#             if zero_to_n:
#                 in_degree = [0] * n
#                 out_degree = [0] * n
            
#             else:
#                 in_degree = [0] * (n + 1)
#                 out_degree = [0] * (n + 1)
            
#             for u, v in edges:
#                 g[u].append(v)
#                 in_degree[v] += 1
#                 out_degree[u] += 1
#         else:
#             for u, v in edges:
#                 g[u].append(v)
#     return (g, degree, in_degree, out_degree)

# def solve(n, m, edges):
#     par = [i for i in range(n + 1)]
#     meta = {i:1 for i in range(1, n + 1)}
    
#     def find(x):
#         if x != par[x]:
#             par[x] = find(par[x])
#         return par[x]
    
#     def find_size(x):
#         return (x * (x - 1)) // 2
    
#     initial_total = find_size(n)
#     answer = []
    
#     #This union function should tell us the number of paris that got connected by adding an edge betwee n1 and n2
#     def union(n1, n2):
#         p1, p2 = find(n1), find(n2)
#         if p1 == p2:
#             return 0
#         if meta[p1] < meta[p2]:
#             p1, p2 = p2, p1
#         total = find_size(meta[p1] + meta[p2])
#         removed = find_size(meta[p1]) + find_size(meta[p2])
#         diff = total - removed
#         par[p2] = p1
#         meta[p1] += meta[p2]
#         return diff
    
#     for u, v in edges:
#         answer.append(initial_total)
#         initial_total -= union(u, v)
#     return answer[::-1]

# def main():
#     n, m = ainp()
#     edges = []
#     for _ in range(m):
#         edge = ainp()
#         edges.append(edge)
#     print_adv("The answer is ", solve, n, m, edges)

# main()

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


def solve(n, arr, permu):

    par = [i for i in range(n)]
    meta = {i:arr[i] for i in range(n)}

    is_active = [False] * n

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]
    
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        meta[p1] += meta[p2]
        par[p2] = p1

    cur_max = 0
    answer = []
    for i in range(n):
        answer.append(cur_max)
        idx = permu[i] - 1
        is_active[idx] = True
        if idx - 1 >= 0 and is_active[idx - 1]:
            union(idx, idx - 1)
        if idx + 1 < n and is_active[idx + 1]:
            union(idx, idx + 1)
        p = find(idx)
        cur_sum = meta[p]
        if cur_sum > cur_max:
            cur_max = cur_sum
    return answer[::-1]
        



def main():
    n = iinp()
    arr = ainp()
    permu = ainp()
    permu = permu[::-1]
    print_adv("the answer is ", solve, n, arr, permu)

main()