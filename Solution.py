# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = []
        n = l1
        while n != None:
            num.append(n.val)
            n = n.next
        num1 = int("".join(str(i) for i in reversed(num)))
        n = l2
        num = []
        while n != None:
            num.append(n.val)
            n = n.next
        num2 = int("".join(str(i) for i in reversed(num)))
        result = str(num1+num2)
        l = ListNode()
        for i in result: 
            l.next = ListNode(int(i),l.next)        
        return l.next
        
        

        
