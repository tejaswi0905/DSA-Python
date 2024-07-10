class Node: 
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

def treversal(head):
    current = head
    while current != None:
        print(current.val)
        current = current.next

def reverse_k_at_a_time(head,k):
    current = head
    first = head
    main = head
    secondary = head
    count = k
    while current!=None:
        if count==0:
            count = k
        current = current.next
        current.next = first
        first = current.next
        count-=1
        if count == 0:
            main = current
            secondary.next = main.next
    return main

def reverse(head):
    prev = head
    start = head
    if head == None:
        return None
    if head.next == None:
        return head
    current = prev.next
    next_node = current.next
    while next_node:
        temp = current
        current.next = prev
        prev = temp
        current = next_node
        next_node = next_node.next
    current.next = prev
    start.next = None
    return current

treversal(reverse(node1))






