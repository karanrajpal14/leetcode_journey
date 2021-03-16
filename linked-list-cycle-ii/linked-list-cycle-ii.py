# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        ptr1 = head
        visited = set()
        
        while ptr1:
            if ptr1 not in visited:
                visited.add(ptr1)
                ptr1 = ptr1.next
            else:
                return ptr1
        
        return None