# # code to findout the diameter of a n-ary tree
# from collections import defaultdict, deque

# def find_diameter(edges, n):
#     adj_graph = defaultdict(list)
#     for u, v in edges:
#         adj_graph[u].append(v)
#         adj_graph[v].append(u)
    
    
#     def dfs(start):
#         q = deque()
#         max_dist = 0
#         q.append(start)
#         dist = [-1] * (n + 1)
#         dist[start] = 0
#         farthest_node = start
#         while q:
#             node = q.popleft()
#             cur_dist = dist[node]
#             for ch in adj_graph[node]:
#                 if dist[ch] > -1:
#                     continue
#                 dist[ch] = cur_dist + 1
#                 if dist[ch] > max_dist:
#                     farthest_node = ch
#                     max_dist = dist[ch]
#                 q.append(ch)
                
#         return farthest_node, max_dist, dist
    
#     u, _, _ = dfs(1)
#     v, d, dist_u = dfs(u)
#     _, _, dist_v = dfs(v)
#     centers = []
#     endpoints = set()
#     for node in range(1, n + 1):
#         if dist_u[node] == d or dist_v[node] == d:
#             endpoints.add(node)
#     print(list(endpoints))
#     for node in range(1, n + 1):
#         if (dist_u[node] + dist_v[node] == d) and (abs(dist_u[node] - dist_v[node]) <= 1):
#             centers.append(node)
#     return centers

# edges = [
#     (1, 2), (1, 3), (1, 4),
#     (2, 5), (2, 6), (2, 7),
#     (3, 8), (3, 9), (3, 10),
#     (4, 11), (4, 12), (4, 13),
#     (5, 14), (8, 15), (11, 16)
# ]
# print(find_diameter(edges, 16))

# def find_lca(edges, n):
#     adj_list = defaultdict(list)
#     for u, v in edges:
#         adj_list[u].append(v)
#         adj_list[v].append(u)
    
#     LOG = 20
#     up = [[-1] * LOG for _ in range(n + 1)]
#     depths = [0] * (n + 1)

#     def dfs(node, parent, depth):
#         depths[node] = depth
#         up[node][0] = parent
#         for ch in adj_list[node]:
#             if ch == parent:
#                 continue
#             dfs(ch, node, depth + 1)
#     dfs(1, -1, 0)
#     for k in range(1, LOG):
#         for u in range(1, n + 1):
#             if up[u][k - 1] != -1:
#                 up[u][k] = up[up[u][k - 1]][k - 1]
#     def get_kt_ancestor(node, k):
#         if node == -1 or k == 0:
#             return node
#         for i in range(LOG - 1, - 1, -1):
#             if k >= (1 << i) and node != -1:
#                 node = up[node][i]
#                 k = k - (1 << i)
#         return node
    
#     def lca(u, v):
#         if depths[u] > depths[v]:
#             u = get_kt_ancestor(u, depths[u] - depths[v])
#         elif depths[v] > depths[u]:
#             v = get_kt_ancestor(v, depths[v] - depths[u])
#         if u == v:
#             return u
#         for i in range(LOG - 1, -1, -1):
#             if up[u][i] != up[v][i]:
#                 u = up[u][i]
#                 v = up[v][i]
#         return up[u][0]
    
#     print(lca(15, 10))
#     print(lca(9, 3))
#     print(lca(6, 14))
#     print(lca(8, 8))

# print(find_lca(edges, 16))

# # for class based tree representatio so that the nodes have very different values

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# root = Node(9)
# node2 = Node(6)
# node3 = Node(4)
# node4 = Node(2)
# node5 = Node(3)
# node6 = Node(8)
# node7 = Node(5)
# node8 = Node(-3)
# node9 = Node(10)
# node10 = Node(11)
# node11 = Node(17)
# root.left = node2
# root.right = node3
# node2.left = node4
# node4.left = node7
# node4.right = node8
# node3.left = node5
# node3.right = node6
# node5.left = node9
# node5.right = node10
# node6.right = node11

# def find_lca2(root, n = None):
#     def size_of_tree(node):
#         if not node:
#             return 0
#         left = size_of_tree(node.left)
#         right = size_of_tree(node.right)
#         return left + right + 1
#     if not n:
#         n = size_of_tree(root)
    
#     LOG = 20
#     depth = [-1] * (n + 1)
#     up = [[-1] * (LOG) for _ in range(n + 1)]
#     id_to_node = {}
#     node_to_id = {}
#     node_id = 1

#     def dfs(node, p_id, d):
#         if not node:
#             return 
#         nonlocal node_id
#         cur = node_id
#         node_id += 1
#         id_to_node[cur] = node
#         node_to_id[node] = cur

#         depth[cur] = d
#         up[cur][0] = p_id

#         if node.left:
#             dfs(node.left, cur, d + 1)
#         if node.right:
#             dfs(node.right, cur, d + 1)
#     dfs(root, -1, 0)
#     for k in range(1, LOG):
#         for i in range(1, n + 1):
#             if up[i][k - 1] != -1:
#                 up[i][k] = up[up[i][k - 1]][k - 1]
    
#     def get_kth_ancestor(node_id, k):
#         if node_id == -1 or k == 0:
#             return node_id
        
#         for i in range(LOG - 1, -1, -1):
#             if k >= (1 << i) and node_id != -1:
#                 node_id = up[node_id][i]
#                 k = k - (1 << i)
#         return node_id
    
#     def lca(u_node, v_node):
#         uid = node_to_id[u_node]
#         vid = node_to_id[v_node]

#         if depth[uid] > depth[vid]:
#             uid = get_kth_ancestor(uid, depth[uid] - depth[vid])
#         if depth[vid] > depth[uid]:
#             vid = get_kth_ancestor(vid, depth[vid] - depth[uid])

#         if uid == vid:
#             return id_to_node[uid].val
        
#         for i in range(LOG - 1, -1, -1):
#             if up[uid][i] != up[vid][i]:
#                 uid = up[uid][i]
#                 vid = up[vid][i]
#         lca_id = up[uid][0]
#         if lca_id == -1:
#             return id_to_node[uid].val
#         return id_to_node[lca_id].val

#     print(lca(node4, node3))
#     print(lca(node9, node3))
#     print(lca(node10, node10))
#     print(lca(node2, node8))

# print(find_lca2(root))


# '''
# Merge sort and problems related to merge sort
# '''

# def merge_in_arr(arr, l, y, r):
#     i = l
#     j = y
#     k = 0

#     c = [0] * (r - l + 1)

#     while (i < y) and (j <= r):
#         if arr[i] < arr[j]:
#             c[k] = arr[i]
#             i += 1
#         else:
#             c[k] = arr[j]
#             j += 1
#         k += 1
#     while i < y:
#         c[k] = arr[i]
#         i += 1
#         k += 1
#     while j <= r:
#         c[k] = arr[j]
#         j += 1
#         k += 1
    
#     for i in range(l, r + 1):
#         arr[i] = c[i - l]
#     return arr

# arr = [8, 1, 3, 6, 11, 2, 4, 9, 7, 6]

# modified_arr = [1, 2, 6, 8, 11,  2, 4, 6, 7, 9]

# '''
# do this before every merge step. Then we get the answer.
# count = 0
# i = l
# j = m

# while (i < m and j <= r):
#     if arr[i] > arr[j]:
#         count += m - i
#         j += 1
#     else:
#         i += 1

# '''
# def count_pairs(arr):

#     inversion_count = [0]
#     def count(arr, l, m, r):
#         i = l
#         j = m
#         while (i < m and j <= r):
#             if arr[i] > arr[j]:
#                 inversion_count[0] += m - i
#                 j += 1
#             else:
#                 i += 1
        
#     def merge(arr, l, r):
#         if r <= l:
#             return arr
        
#         m = (l + r) // 2
#         merge(arr, l, m)
#         merge(arr, m + 1, r)
#         count(arr, l, m + 1, r)
#         merge_in_arr(arr, l, m + 1, r)
    
#     l = 0
#     r = len(arr) - 1
#     merge(arr, l, r)
#     return inversion_count[0]

# print(count_pairs(arr))

'''
The unique elements problem
'''

def unique_elements(arr):
    arr.sort()
    steps = 0
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            steps += 1
            arr[i] += 1
        elif arr[i - 1] > arr[i]:
            cur_steps = arr[i - 1] - arr[i] + 1
            steps += cur_steps
            arr[i] += steps
    return steps

print(unique_elements([4,1,2,4,3,4])) 