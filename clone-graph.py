"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 1's neighbors [2,4], 2's neighbors [1,3] etc
        if node:
            print(node.val)
        oldToNew={}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy 
        
        
        return dfs(node) if node else None
# {1: 1copy, 2: 2copy, 3: 3copy, 4: 4copy}
# dfs(1)
#    1copy.neighbors.append(dfs(2))
#         2copy.neighbors.append(dfs(1)) -> returns 1copy from oldToNew. 2copy.neighbors is now [1copy]
#         2copy.neighbors.append(dfs(3)) 
#              3copy.neighbors.append(dfs(2)) -> returns 2copy from oldToNew. 3copy.neighbors is now [2copy]
#              3copy.neighbors.append(dfs(4)) 
#                   4copy.neighbors.append(dfs(1)) -> returns 1copy from oldToNew.
#                   4copy.neighbors.append(dfs(3)) -> returns 3copy from oldToNew.
#                   4copy finishes. 4copy.neighbors is now [1copy, 3copy]. Returns 4copy to Node 3.
#              3copy finishes. 3copy.neighbors is now [2copy, 4copy]. Returns 3copy to Node 2.
#         2copy finishes. 2copy.neighbors is now [1copy, 3copy]. Returns 2copy to Node 1.
#    1copy.neighbors.append(dfs(4)) -> returns 4copy from oldToNew instantly (no deep recursion needed!)
# 1copy finishes. 1copy.neighbors is now [2copy, 4copy].
# RETURN 1copy

# This is what 1copy looks like internally:
# {
#     'val': 1,
#     'neighbors': [
#         {
#             'val': 2,
#             'neighbors': [
#                 <reference to 1copy>, 
#                 {
#                     'val': 3,
#                     'neighbors': [
#                         <reference to 2copy>,
#                         {
#                             'val': 4,
#                             'neighbors': [<reference to 1copy>, <reference to 3copy>]
#                         }
#                     ]
#                 }
#             ]
#         },
#         <reference to 4copy>
#     ]
# }


# {
#             'val': 2,
#             'neighbors': [
#                 <reference to 1copy>, 
#                 {                       # <-- THIS WHOLE OBJECT IS 3copy!
#                     'val': 3,           # It was "returned to Node 2" and placed here.
#                     'neighbors': [
#                         <reference to 2copy>,
#                         { 'val': 4, ... }
#                     ]
#                 }                       # <-- End of 3copy
#             ]
#         },
        