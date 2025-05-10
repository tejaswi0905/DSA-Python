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




def longest_path_through_any_node(root):
    longest = [0]
 
    def dfs(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)
        height = max(left_height, right_height) + 1 #This needs to be returned
        path_count = 0
        if node.left != None and node.right!= None:
            path_count += 2
        elif node.left != None or node.right != None:
            path_count += 1
        longest[0] = max(longest[0], left_height + right_height + path_count)
        return height
    dfs(root)
    return longest[0]

print(longest_path_through_any_node(root))



    

    
    





    
    