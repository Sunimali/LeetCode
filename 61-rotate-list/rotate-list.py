# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        #slow and fast pointers
        slow = head
        fast = head

        dummy  = ListNode(0) #dummy node
        dummy.next = head
        
        count = 0
        while fast is not None: #find the length
            fast = fast.next
            count = count + 1
               
        if count == 0 or count == 1: #no element or only one element
            return dummy.next        
        if count <= k: #k >= length of the list
            k = k % count #find new k
        if k == 0:
            return dummy.next    
        fast = head
        for i in range(k): #move fast pointer by k
            fast = fast.next         
        #else do the rotation
        fast_prev = None
        slow_prev = None
        while fast is not None: #find the fotation portion
            slow_prev = slow
            slow = slow.next
            fast_prev = fast
            fast = fast.next 
        temp = slow_prev.next
        slow_prev.next = None
        fast_prev.next = dummy.next
        head = temp

        return head
               



        