# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    #without dummy node   
        # prev = None
        # current = head
        # if head is None: #emply list
        #     return head
        # head_dup = 0 #check whether head is duplicated or no

        # while current is not None: #iterate through whole list
        #     if(prev is None): #handle first node iteration
        #         prev = current
        #         current = current.next
        #     else:
        #         initial = current
        #         init_prev = prev #first occuorance of a node values
        #         count = 0 #keep occurance count
        #         while( current is not None and current.val == initial.val): #iterate same val
        #             if(current.val == head.val): #head has duplicates
        #                 head_dup = 1 #set head has duplicates
                   
        #             prev = current
        #             current = current.next
        #             count = count + 1 #increase the occurence count
        #         if(head_dup ): #if head is dupllicates change the head to new after removing
        #             head = current
        #             prev = None
        #             head_dup = 0 #reset flag
        #             continue
            
        #         #now current is not equal to initial
        #         #1 is not having same occurence since initail and current was same pointer    in the begining
        #         if count > 1: #Found more than once ocurence
        #             init_prev.next = current 
        #             prev = init_prev
        # return head

        #with dummy node

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy #prev node has initial value rather than noe
        current = head

        while current is not None: #no need to handle prev none sperately
            initial = current
            init_prev = prev #first occuorance of a node values
            count = 0

            while(current is not None and current.val == initial.val):
                prev = current
                current = current.next
                count = count + 1 #increase the occurence count

            if count > 1:
                init_prev.next = current
                prev = init_prev
        return dummy.next






   
