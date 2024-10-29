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
        dict_visited = {}

        current = head
        

        while current is not None:
            if current in dict_visited: # check nodes in dictionary or not
                return True #ther is a loop
            else:    
                dict_visited[current] = True #else add to dictionary
                current = current.next #move to next element
        return False  #if last element doesnt have  pointer thne it is none      

        