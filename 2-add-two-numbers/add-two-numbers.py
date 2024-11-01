# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        l1_stack = []
        l2_stack = []

        c1 = l1
        c2 = l2
        longest = l1_stack
        shortest = l2_stack
        ans = None
        current = None
        
        while not(c1 is None and c2 is None):
            
            if(c1 is not None):
                l1_stack.append(c1.val)
                c1 = c1.next
                longest = l1_stack
                shortest = l2_stack
            if(c2 is not None):
                l2_stack.append(c2.val)
                c2 = c2.next
                longest = l2_stack
                shortest = l1_stack   
        r = 0
        s = 0
        while shortest:
            a = longest.pop(0) 
            b = shortest.pop(0)
            s = a+ b+ r
            m = (s) % 10
            r = (s)//10
            temp = ListNode(m)

            if(ans is None):
                ans = temp
                current = temp
            else:
                current.next = temp
                current = current.next

        while longest:
            a = longest.pop(0)
            s = a + r
            m = (s) % 10
            r = (s)//10
            temp = ListNode(m)
            if(ans is None):
                ans = temp
                current = temp
            else:
                current.next = temp
                current = current.next
        if r == 0:
            return ans 
        else:
            temp = ListNode(r)  
            current.next = temp
            return ans       

