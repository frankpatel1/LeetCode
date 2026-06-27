class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []

        first = second = prev = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev and prev.val > root.val:
                if first is None:
                    first = prev
                second = root

            prev = root
            root = root.right

        first.val, second.val = second.val, first.val