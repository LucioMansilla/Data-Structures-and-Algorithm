# https://leetcode.com/problems/root-equals-sum-of-children/

import sys
sys.path.append('../tree')
from tree.BinaryTree import BinaryTree

class Solution:
    def checkTree(self, root: BinaryTree) -> bool:
        return root.val == root.left.val + root.right.val