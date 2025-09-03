class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result = []
        def dfs(node): #node_start point here which is root
            if node:
                result.append(node.value)
                dfs(node.left) #calling the function recursively, this time start point is gonna be left node/child, then storing the value in result
                dfs(node.right)#calling the function recursively, this time start point is gonna be right node/child, then storing the value in result
        dfs(root)
        return result
            

Root= Node(1)  #creating the root node first 

Root.left = None
Root.right = Node(2)
Root.right.right = None
Root.right.left = Node(3)
Binary_Tree = Solution()
print(Binary_Tree.preorderTraversal(Root))

"""
   1
  /  \
NULL  2
     /  \
    3   NULL     
"""

