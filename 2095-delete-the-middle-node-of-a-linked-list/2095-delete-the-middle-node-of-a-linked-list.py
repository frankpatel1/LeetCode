# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If there's only one node, deleting it makes the list empty
        if not head or not head.next:
            return None
        
        prev = None
        slow = head
        fast = head
        
        # Move fast by 2 steps and slow by 1 step
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' is now pointing to the middle node
        # 'prev' is pointing to the node before 'slow'
        prev.next = slow.next
        
        return head