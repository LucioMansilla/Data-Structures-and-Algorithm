# https://leetcode.com/problems/search-in-a-binary-search-tree/

from ..tree import BinaryTree

class Solution:

    def searchBST(self, root: BinaryTree, val: int) -> BinaryTree:
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
