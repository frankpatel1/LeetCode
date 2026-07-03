# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # Helper function to find the path from root to a target value using backtracking
        def find_path(node: TreeNode, target: int, path: list) -> bool:
            if not node:
                return False
            if node.val == target:
                return True
            
            # Try Left
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop() # Backtrack
            
            # Try Right
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop() # Backtrack
            
            return False
        
        start_path = []
        dest_path = []
        
        # Find paths from root to both nodes
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)
        
        # Find the point of divergence (LCA)
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
            
        # For the remaining start path, convert every step to 'U'
        u_steps = 'U' * (len(start_path) - i)
        
        # For the remaining dest path, keep the directions as they are
        dir_steps = "".join(dest_path[i:])
        
        return u_steps + dir_steps