class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# root = Node(9)
# node2 = Node(6)
# node3 = Node(4)
# node4 = Node(2)
# node5 = Node(3)
# node6 = Node(8)
# node7 = Node(6)
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

root = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
root.left = node1
node1.left = node2
node2.left = node3
node3.left = node4

def longest_path_through_root(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 0
    left_height = longest_path_through_root(node.left)
    right_height = longest_path_through_root(node.right)
    if node == root:
        ch_count = 0
        if node.left:
            ch_count += 1
        if node.right:
            ch_count += 1
        if ch_count == 2:
            return left_height + right_height + 2
        elif ch_count == 1:
            return left_height + right_height + 1
        else:
            return 0
    height = max(left_height , right_height) + 1
    return height


def longest_path_through_root2(root):
    def height(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        return max(lh, rh) + 1
    
    h1 = height(root.left)
    h2 = height(root.right)
    if root.left is not None and root.right is not None:
        return h1 + h2 + 2
    elif root.left is not None or root.right is not None:
        return h1 + h2 + 1
    else:
        return 0

print(longest_path_through_root(root))
print(longest_path_through_root2(root))