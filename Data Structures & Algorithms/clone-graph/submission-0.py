"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        nodes = {}
        def subClone(node):
            if not node:
                return None
            new = Node(node.val)
            nodes[new.val] = new
            if not node.neighbors:
                return new
            
            for neighbor in node.neighbors:
                if neighbor.val in nodes:
                    new.neighbors.append(nodes[neighbor.val])
                else:
                    new.neighbors.append(subClone(neighbor))
            return new

        return subClone(node)