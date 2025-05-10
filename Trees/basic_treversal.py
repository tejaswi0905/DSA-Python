from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(9)
node2 = Node(6)
node3 = Node(4)
node4 = Node(2)
node5 = Node(3)
node6 = Node(8)
node7 = Node(6)
node8 = Node(-3)
node9 = Node(10)
node10 = Node(11)
node11 = Node(17)
root.left = node2
root.right = node3
node2.left = node4
node4.left = node7
node4.right = node8
node3.left = node5
node3.right = node6
node5.left = node9
node5.right = node10
node6.right = node11

def bfs(node):
    # we need a queue
    
    # left most node is our main/current node, 
    # we pop the node from left side, after popping we do all the operations using the node
    # we add children to the right side
    
    
    pass

def bfs_treversal(root):
    q = deque()
    q.append(root)
    
    while q:
        cur_node = q.popleft()
        print(cur_node.val)
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)

bfs_treversal(root)

def each_level_array(root):
    q = deque()
    q.append(root)
    all_levels = []
    
    while q:
        cur_level = []
        cur_len = len(q)
        
        for _ in range(cur_len):
            cur_node = q.popleft()
            cur_level.append(cur_node.val)
            if (cur_node.left):
                q.append(cur_node.left)
            if (cur_node.right):
                q.append(cur_node.right)
        all_levels.append(cur_level)
    

def dfs(node):
    #base case
    
    #before call area you only have access to the current node 
    
    #call
    
    #after call area you have access to both the node and the return value.
    
    #return area
    pass

def size_of_tree(node):
    if (node is None):
        return 0
     
    cur_size = 1
    left_size = size_of_tree(node.left)
    right_size = size_of_tree(node.right)
    
    total_size = left_size + right_size + cur_size
    return total_size
    
        
print(size_of_tree(root))

def sum_of_all_node(node):
    if (node.left == None and node.right == None):
        return node.val 
    cur_val = node.val
    
    if(node.left):
        left_sum = sum_of_all_node(node.left)
    else:
        left_sum = 0
    
    if(node.right):
        right_sum = sum_of_all_node(node.right)
    else:
        right_sum = 0
    
    total_sum = cur_val + left_sum + right_sum
    return total_sum

def sum_of_tree(node):
    if node is None:
        return 0
    cur_val = node.val
    left_val = sum_of_tree(node.left)
    right_val = sum_of_tree(node.right)
    total_sum = cur_val + left_val + right_val
    return total_sum

print(sum_of_all_node(root))
print(sum_of_tree(root))