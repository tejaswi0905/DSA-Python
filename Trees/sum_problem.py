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
node8 = Node(3)
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


def sum_of_tree(root):
    count = [0]
    def dfs(prev, node):
        if node is None:
            return 
        if node.left is None and node.right is None:
            number = prev * 10 + node.val
            print(number)
            count[0] += number
            return

        number = prev * 10 + node.val
        if node.left:
            dfs(number, node.left)
        if node.right:
            dfs(number, node.right)
    
    dfs(0, root)
    return count[0]

print(sum_of_tree(root))      