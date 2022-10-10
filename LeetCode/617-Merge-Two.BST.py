from tree.BinaryTree import BinaryTree
import sys
sys.path.append('../tree')
class Solution:
    def mergeTrees(self, root1, root2):

            if root1 and root2:
                root = BinaryTree(root1.val + root2.val)
                root.left = self.mergeTrees(root1.left, root2.left)
                root.right = self.mergeTrees(root1.right, root2.right)
                return root
            
            return root1 or root2