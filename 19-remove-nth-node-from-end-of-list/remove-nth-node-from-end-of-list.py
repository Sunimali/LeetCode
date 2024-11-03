# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        #need two pointer slow and fast
        slow = head
        fast = head

        #make a n gap between slow and fast one
        for i in range (n):
            fast = fast.next

        prev = None
        while fast is not None:
            prev = slow #store previous
            slow = slow.next
            fast = fast.next

        #now slow is n
        #prev is n + 1 from last

        if prev is None:
            return slow.next
        temp = slow.next # n -1 from last 
        prev.next = temp

        return head  

               



        


        