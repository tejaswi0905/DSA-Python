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

def left_view(root):
    arr = []
    arr.append(root.val)
    def left_view_function(node):
        if node.left is None:
            return node.val
        left = left_view_function(node.left)
        arr.append(left)
        return node.val
    left_view_function(root)
    return arr



def level_order_arrays(root):
    levels = []
    q = deque()
    q.append(root)

    while q:
        cur_level_size = len(q)
        cur_level = []
        for i in range(cur_level_size):
            cur_node = q.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        levels.append(cur_level)
    return levels

# print(level_order_arrays(root))

def left_and_right_views(root):
    left_view_array = []
    right_view_array = []
    q = deque()
    q.append(root)

    while q:
        cur_size = len(q)
        for i in range(cur_size):
            cur_node = q.popleft()
            if i == 0:
                left_view_array.append(cur_node.val)
            if i == cur_size - 1:
                right_view_array.append(cur_node.val)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
    return left_view_array, right_view_array

# print(left_and_right_views(root))


    
            


    
