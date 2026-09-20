"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_copy = {None : None}

        cur = head
        while cur:
            old_copy[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy_node = old_copy[cur]
            copy_node.next = old_copy[cur.next]
            copy_node.random = old_copy[cur.random]
            cur = cur.next
            
        return old_copy[head]