# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def inorder(node, nodes):
            if node is None:
                return None
            else:
                left = inorder(node.left, nodes)
                nodes.append(node)
                right = inorder(node.right, nodes)
        
        inorder(root, nodes)
        if not nodes:
            return []
       
        def build(nodes):
            if not nodes:
                return None
            mid = (len(nodes)-1)//2
            root = nodes[mid]
            
            root.left = build(nodes[:mid])
            root.right = build(nodes[mid+1:])

            return root
        
        return build(nodes)
        



        

        de
                
            