# https://leetcode.com/problems/root-equals-sum-of-children/

from tree.BinaryTree import BinaryTree
import sys
sys.path.append('../tree')


class Solution:
    def checkTree(self, root: BinaryTree) -> bool:
        return root.val == root.left.val + root.right.val
