# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

     
        
        l_prev = None #keep left prev
        r_prev = None #keep right prev
        prev = None


        if left == right: #no need of reversing
             return head

        current = head
        itr = 1

        while itr < left: #iterate untill left - 1
            l_prev = current
            current = current.next
            itr = itr + 1

        reverserd_head = current #set left as revered list head

        while itr <= right: #iterate through hit right
            temp = current.next
            current.next = prev

            prev = current
            current = temp
            itr = itr + 1

        #merge lists
        reverserd_head.next = current

        if l_prev:
            l_prev.next = prev
        else:
            head = prev  
        return head


