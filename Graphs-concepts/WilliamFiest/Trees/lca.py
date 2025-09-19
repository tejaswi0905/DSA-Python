# Here I am doing the lca and lca with the twist
from cp_boiler_plate_codes import graphs_build
import random
from collections import defaultdict

def find_lca(n, edges, queries):
    g, _, _, _ = graphs_build.build_graph_non_weighted(n, edges, False, False, False) 
    print(g)
    LOG = 20
    up = [[-1] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)
    
    # Fill the depths and immediate parents in the up binary-lifting tree
    def dfs(node, p, d):
        depth[node] = d
        up[node][0] = p
        for ch in g[node]:
            if ch != p:
                dfs(ch, node, d + 1)
    dfs(1, -1, 0)

    # Now fill the binary lifting table(up)
    for k in range(1, LOG):
        for u in range(1, n + 1):
            if up[u][k - 1] != -1:
                up[u][k] = up[up[u][k - 1]][k - 1]
    
    def get_kth_parent(node, k):
        if node == -1 or k == 0:
            return node
        
        for i in range(LOG - 1, - 1, -1):
            if k >= (1 << i) and node != -1:
                node = up[node][i]
                k -= (1 << i)
        return node
    
    def get_lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            u = get_kth_parent(u, du - dv)
        if dv > du:
            v = get_kth_parent(v, dv - du)
        
        if u == v:
            return u
        
        for i in range(LOG - 1, - 1, - 1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]
    lcas = [get_lca(u, v) for u, v in queries]
    return lcas


def lca_with_twist(n, edges, queries):
    g, _, _, _ = graphs_build.build_graph_non_weighted(n, edges, False, False, False)
    #Assume 1 is the root and then build the binary lifting table and depths
    LOG = 20
    depth = [0] * (n + 1)
    up = [[-1] * LOG for i in range(n + 1)]
    def dfs(node, p, d):
        depth[node] = d
        up[node][0] = p
        for ch in g[node]:
            if ch != p:
                dfs(ch, node, d + 1)
    dfs(1, -1, 0)

    for k in range(1, LOG):
        for u in range(1, n + 1):
            if up[u][k - 1] != -1:
                up[u][k] = up[up[u][k - 1]][k - 1]
    
    def get_kt_parent(node, k):
        if node == -1 or k == 0:
            return node
        
        for i in range(LOG - 1, -1, -1):
            if k >= (1 << i) and node != -1:
                node = up[node][i]
                k -= (1 << i)
        return node
    
    def get_lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            u = get_kt_parent(u, du - dv)
        if dv > du:
            v = get_kt_parent(v, dv - du)
        
        if u == v:
            return u
        
        for i in range(LOG - 1, - 1, -1):
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]
    
    answer = []
    
    for u, v, w in queries:
        l = get_lca(u, v)
        lca_u_w = get_lca(u, w)
        lca_v_w = get_lca(v, w)
        max_depth = depth[l]
        ans_node = l
        if depth[lca_u_w] > max_depth:
            max_depth = depth[lca_u_w]
            ans_node = lca_u_w
        if depth[lca_v_w] > max_depth:
            max_depth = depth[lca_v_w]
            ans_node = lca_v_w
        answer.append(ans_node)
    return answer
        
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [5, 10], [6, 12], [8, 9], [10, 11]]
print("------")
print(find_lca(12, edges, [[10, 12], [10, 1], [5, 5]]))

def create_weighted_edges(edges):
    weighted_edges = []
    for u, v in edges:
        weight = random.randint(-10, 10)
        weighted_edges.append([u, v, weight])
    return weighted_edges

weighted_edges = [[1, 2, 4], [1, 3, 9], [2, 4, 0], [2, 5, 2], [2, 6, 5], [3, 7, 9], [3, 8, -5], [5, 10, 0], [6, 12, 3], [8, 9, 2], [10, 11, 2]]
print(weighted_edges)

queries = [[10, 12], [4, 5], [2, 2], [8, 9]]
queries2 = [[10, 12, 5], [10, 12, 1], [10, 12, 10]]
queries3 = [[4, 3], [3, 9], [11, 10], [2, 2]]





def lca_with_weighted(n, edges, queries):
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    
    LOG = 20
    depth = [0] * (n + 1)
    weight_from_root = [0] * (n + 1)

    up = [[-1] * LOG for _ in range(n + 1)]
    upWeight = [[0] * LOG for _ in range(n + 1)]
    maxEdge = [[0] * LOG for _ in range(n + 1)]

    # dfs for filling the depth, parent in up and parent's-weight in the upWeight and parent's weith as the maxEdge for now.

    def dfs(node, p, d, cur_weight):
        depth[node] = d
        weight_from_root[node] = cur_weight
        for ch, w in g[node]:
            if ch != p:
                up[ch][0] = node
                upWeight[ch][0] = w
                maxEdge[ch][0] = w
                dfs(ch, node, d + 1, cur_weight + w)
    
    dfs(1, -1, 0, 0)

    # build lifting talbes, the formulas are similar

    for k in range(1, LOG):
        for u in range(1, n + 1):
            if up[u][k - 1] != -1:
                ancestor = up[u][k - 1]
                up[u][k] = up[ancestor][k - 1]
                upWeight[u][k] = upWeight[u][k - 1] + upWeight[ancestor][k - 1]
                maxEdge[u][k] = max(maxEdge[u][k - 1], maxEdge[ancestor][k - 1])
    
    def get_kt_ancestor(node, k):
        if node == -1 or k == 0:
            return node
        
        for i in range(LOG - 1, -1, -1):
            if k >= (1 << i) and node != -1:
                node = up[node][i]
                k -= (1 << i)
        return node
    
    def find_lca(u, v):
        du, dv = depth[u], depth[v]
        if du > dv:
            u = get_kt_ancestor(u, du - dv)
        if dv > du:
            v = get_kt_ancestor(v, dv - du)
        
        if u == v:
            return u
        
        for k in range(LOG - 1, -1, -1):
            if up[u][k] != up[v][k]:
                u = up[u][k]
                v = up[u][k]
        return up[u][0]
    
    
    def get_weights_sum(u, v):
        lca = find_lca(u, v)
        weights_sum = weight_from_root[u] + weight_from_root[v] - 2 * weight_from_root[lca]
        return weights_sum
    
    def get_max_edge_on_path(u, v):
        du, dv = depth[u], depth[v]
        max_w = float("-inf")

        if du > dv:
            diff = du - dv
            for k in range(LOG - 1, -1, -1):
                if diff >= (1 << k):
                    max_w = max(max_w, maxEdge[u][k])
                    u = up[u][k]
                    diff -= (1 << k)

        if dv > du:
            diff = dv - du
            for k in range(LOG - 1, -1, -1):
                if diff >= (1 << k):
                    max_w = max(max_w, maxEdge[v][k])
                    v = up[v][k]
                    diff -= (1 << k)

        if u == v:
            return max_w

        for k in range(LOG - 1, -1, -1):
            if up[u][k] != up[v][k]:
                max_w = max(max_w, maxEdge[u][k], maxEdge[v][k])
                u = up[u][k]
                v = up[v][k]

        max_w = max(max_w, maxEdge[u][0], maxEdge[v][0])
        return max_w

    
    answer = []
    for u, v in queries:
        ans = get_weights_sum(u, v)
        answer.append(ans)
    return answer

print(lca_with_weighted(12, weighted_edges, queries3))