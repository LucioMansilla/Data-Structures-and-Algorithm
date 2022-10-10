# https://leetcode.com/problems/range-sum-of-bst/

from tree.BinaryTree import BinaryTree
import sys
sys.path.append('../tree')


#T(n) is O(n) where n is the number of nodes in the tree, since we visit each node once.

# First approach: 
class Solution:
    def rangeSumBST(self, root: BinaryTree, low: int, high: int) -> int:
        if root:
            if root.val >= low and root.val <= high:
                return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
            else:
                return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        else:
            return 0


# Second approach:
class Solution:
   def rangeSumBST(self, root: BinaryTree, low: int, right: int) -> int:
        if not root:
            return 0
        return self.rangeSumBST(root.left, low, right) + \
                self.rangeSumBST(root.right, low, right) + \
                (root.val if low <= root.val <= right else 0)
