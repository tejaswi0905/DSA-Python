# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, x):
#         self.val = x
#         self.next = None

"""question 160 in leetcode, look for the reference. Finding the intersection node of the two linkedlists that can connect somewhere in the middle or not."""

def intersection_node(headA,headB):
    if headA == headB:
        return headA
    cur1,cur2 = headA,headB
    n1,n2 = 0,0
    while cur1:
        n1+=1
        cur1 = cur1.next
    while cur2:
        n2+=1
        cur2 = cur2.next
    if n1>=n2:
        cur1 = headA
        cur2 = headB
        while(n1>0 and cur1 is not None):
            if(n1==n2):
                if cur1==cur2:
                    return cur1
                cur2 = cur2.next
                n2-=1
            n1-=1
            cur1 = cur1.next
    else:
        cur1 = headA
        cur2 = headB
        while(n2>0 and cur2 is not None):
            if(n1==n2):
                if cur1==cur2:
                    return cur1
                cur1 = cur1.next
                n1-=1
            n2-=1
            cur2 = cur2.next
    return None