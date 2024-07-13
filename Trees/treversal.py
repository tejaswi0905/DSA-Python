class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

'''
The dfs call is recursive in nature.
* You can pass any number of varilbes/data-structures to the dfs fuction based on the problem requirment.
dfs(node):
   // We proces the ndoe before the call. Pruning state.
      -> Base case check. 
      -> any other operations based on problem requirment.
    
    // 2 function calls. One for left and one for right.
       -> You get two values from left call and right call.
       -> use those values to compute the current answer for the node
    // Return the answer for this node.
'''

def treversal_dfs(root):
    def dfs(node):

        if node.left == None and node.right == None:
            return 1
        if node is None:
            return 0
        
        left_sub_tree_size = dfs(node.left)
        right_sub_tree_size = dfs(node.right)
        current_size = left_sub_tree_size + right_sub_tree_size + 1
        return current_size
    return dfs(root)


'''
import deque, we use deque for this. from collections import deque.

append root to the deque. we use append to append right to deque.
run a loop as long as deque is non-empty. The way to do that is while q:
 -> pop element from the left
 -> process that node according to the problem.
 -> append the left and right children of the node to the deque in the right.
at the end retrun the answer.
'''

from collections import deque

def treversal_bfs(root):
    q = deque()
    q.append(root)
    size = 0
    while q:
        current_node = q.popleft()
        if current_node is None:
            continue
        size += 1
        q.append(current_node.left)
        q.append(current_node.right)
    return size




print(treversal_dfs(root))
print(treversal_bfs(root))
