# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        # Ensure that a tree exists        
        if not root:
            return result
        
        # Add current node to stack to begin
        stack = []
        stack.append(root)
        
        # Loop as long as we have nodes to process
        while stack:
            # Fetch current node
            curr = stack.pop()
            
            # Add to stack if children present            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
            # Append root value            
            result.insert(0, curr.val)
        
        return result
    