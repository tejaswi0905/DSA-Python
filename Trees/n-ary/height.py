from collections import defaultdict

# Step 1: Build adjacency list
def build_tree(edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    return tree

# Step 2: Height of tree (in terms of edges)
def tree_height(tree, root=0):
    def dfs(node, parent):
        max_h = 0
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            h = dfs(neighbor, node) + 1
            max_h = max(max_h, h)
        return max_h
    return dfs(root, -1)

# Step 3: Max path through root
def max_path_through_root(tree, root=0):
     
    def height(node, parent):
        ch_count = 0
        max1, max2 = 0, 0
        for neighbor in tree[node]:
            if node == 0:
                ch_count += 1
            if neighbor == parent:
                continue
            h = height(neighbor, node) + 1
            if h > max1:
                max2 = max1
                max1 = h
            elif h > max2:
                max2 = h
        
        if node == 0:
            if ch_count >= 2:
                return max1 + max2
            elif ch_count == 1:
                return max1
            else:
                return 0        
        return max1
    return height(0, -1)

def my_diameter(tree, root=0):
    diameter = [0]
    def height(node, parent):
        ch_count = 0
        max1, max2 = 0, 0
        for neighbor in tree[node]:
            if neighbor == parent:
                continue
            ch_count += 1
            h = height(neighbor, node) + 1
            if h > max1:
                max2 = max1
                max1 = h
            elif h > max2:
                max2 = h
        
        if ch_count >= 2:
            diameter[0] = max(diameter[0], max1 + max2)
        elif ch_count == 1:
            diameter[0] = max(diameter[0], max1)        
        return max1
    height(0, -1)
    return diameter[0]

from collections import deque

def dfs(tree, start):
    dist = [-1] * len(tree)
    dist[start] = 0
    max_dist  = 0
    q = deque()
    q.append(start)
    max_node = start

    while q:
        node = q.popleft()
        for ch in tree[node]:
            if dist[ch] == -1:
                dist[ch] = dist[node] + 1
                if dist[ch] > max_dist:
                    max_dist = dist[ch]
                    max_node = ch
                q.append(ch)
    return max_node, max_dist, dist

def diameter2(tree):
    u, _, _ = dfs(tree, 0)
    v, d, dist_v = dfs(tree, u)
    return d

def find_max_height_nodes(tree):
    n = len(tree)
    u, _, _ = dfs(tree, 0)
    v, d, dist_u = dfs(tree, u)
    _, _, dist_v = dfs(tree, v)
    res = []
    for node in range(n):
        if dist_u[node] == d or dist_v[node] == d:
            res.append(node)
    return res

def get_all_diameter_pairs(tree):
    n = len(tree)
    u, _, _ = dfs(tree, 0)
    v, d, dist_u = dfs(tree, u)
    _, _, dist_v = dfs(tree, v)

    
    diameter_nodes = [x for x in range(n) if (dist_u[x] + dist_v[x] == d) or (dist_u[x] == d) or (dist_v[x] ==d)]
    print(diameter_nodes)
    result = []

    for i in range(len(diameter_nodes)):
        for j in range(i + 1, len(diameter_nodes)):
            x = diameter_nodes[i]
            y = diameter_nodes[j]
            if abs(dist_u[x] - dist_u[y]) == d or abs(dist_u[x] - dist_u[y]) == 0:
                result.append((x, y))

    return result


tree2 = build_tree([[0, 1], [0, 2], [1, 3], [3, 4], [3, 5], [2, 6], [4, 7], [7, 8]])

tree3 = build_tree([[0,1], [1, 2], [2, 3], [3, 4]])
tree4 = build_tree([[0, 1], [0, 2], [2, 3], [1, 4], [1, 5], [4, 6], [6, 8], [8, 10], [5, 7], [7, 9], [9, 11]])
tree5 = build_tree([[0, 1], [0, 2], [0, 3], [0, 4]])

# print(my_diameter(tree5, 0))
# print(diameter2(tree5))
# print(find_max_height_nodes(tree5))
print(get_all_diameter_pairs(tree4))
print(get_all_diameter_pairs(tree5))
