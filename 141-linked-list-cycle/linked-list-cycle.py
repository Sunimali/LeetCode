# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # dict_visited = {}

        # current = head
        

        # while current is not None:
        #     if current in dict_visited: # check nodes in dictionary or not
        #         return True #ther is a loop
        #     else:    
        #         dict_visited[current] = True #else add to dictionary
        #         current = current.next #move to next element
        # return False  #if last element doesnt have  pointer thne it is none   

        #lets try less momry need approach
        
        slow = head
        if(head is None or head.next is None) :
            return False
        fast = head.next.next #iterate faster by 2 steps

        while fast is not None and fast.next is not None: #fast one hit final:mean no cycle
            if(slow==fast): #if cycle apear to be then two gets ovelapped
                return True
            slow = slow.next #iterate
            fast = fast.next.next

        return False      

        