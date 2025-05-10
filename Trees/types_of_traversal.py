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


postorder_arr = []

def inorderTraversal(root):
    inorder_arr = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        inorder_arr.append(node.val)
        inorder(node.right)
    inorder(root)
    return inorder_arr

def preorderTraversal(root):
    preorder_arr = []
    def preorder(node):
        if node is None:
            return
        preorder_arr.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return preorder_arr

print(preorderTraversal(root))

def postorderTraversal(root):
    postorder_arr = []
    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        postorder_arr.append(node.val)
    postorder(root)
    return postorder_arr

print(postorderTraversal(root))



def verticalorderTraversal(root):
    verticalorder_arr = []
    def verticalorder(node,minl,maxl):
        map = {}
        q = deque()
        q.append((node,0))
        while q:
            current,level = q.popleft()
            if level not in map:
                map[level] = [current.val]
            else:
                map[level].append(current.val)
            minl = min(minl,level)
            maxl = max(maxl,level)
            if current.left:
                q.append((current.left,level-1))
            if current.right:
                q.append((current.right,level+1))
        return map,minl,maxl
    map,minl,maxl = verticalorder(root,0,0)
    for i in range(minl,maxl+1):
        verticalorder_arr.append(map[i])
    return verticalorder_arr

print(verticalorderTraversal(root))

