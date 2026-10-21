"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
                return None

        nodes = {}
        def subClone(node):
            if node in nodes:
                return nodes[node]
            new = Node(node.val)
            nodes[node] = new

            for neighbor in node.neighbors:
                new.neighbors.append(subClone(neighbor))
            return new

        return subClone(node)