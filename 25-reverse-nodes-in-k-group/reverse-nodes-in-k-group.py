# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy  = ListNode(0)
        dummy.next = head
        prev = dummy

        slow = head
        prev = dummy
        fast = head

        #first move fast to k steps
        rnd = 0
        for i in range(k): #list is smaller than k
            if fast is not None:
                rnd = rnd + 1
                fast = fast.next
            else:
                return dummy.next  
      
        #now fast is at k steps ahead from slow
        
        while fast is not None:
            initial = slow
            initial_prev = prev
            rnd = 0
            for i in range(k):
                # if(fast is None):
                #     return dummy.next
                temp = slow.next
                slow.next = prev

                prev = slow
                slow = temp
                if fast is not None:
                    rnd = rnd + 1
                    fast = fast.next
            initial.next = slow
            initial_prev.next = prev

            prev = initial
    
        if(rnd == k):
            #need to reverse remaing part also
            initial = slow
            initial_prev = prev

            while slow is not None:
                temp = slow.next
                slow.next = prev

                prev = slow
                slow = temp

            initial.next = slow
            initial_prev.next = prev    

        return dummy.next

            






            
                
                    


        