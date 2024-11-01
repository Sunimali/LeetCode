# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 is None):
            return list2
        elif(list2 is None):
            return list1
        else:
            c1 = list1
            c2 = list2
            c2_prev = None

            while(c1 is not None):
                while(c2 is not None and c1.val>c2.val  ):
                    print("no")
                    c2_prev = c2
                    c2 = c2.next
                node = ListNode(c1.val)
                
                if c2_prev is None:
                    node.next = c2
                    list2 = node #change the header
                
                else:
                    c2_prev.next = node
                    node.next = c2 
                    c2_prev = node 

                c1 = c1.next
                c2 = c2_prev.next if c2_prev is not None else list2
            return list2
             

