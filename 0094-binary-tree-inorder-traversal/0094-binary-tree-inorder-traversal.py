class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        while root:
            if not root.left:
                ans.append(root.val)
                root = root.right
            else:
                pre = root.left

                while pre.right and pre.right != root:
                    pre = pre.right

                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    ans.append(root.val)
                    root = root.right

        return ans