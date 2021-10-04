# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    # O(n) time | O(1) space
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next and head.next.next):
            return None
        
        # Floyd's cycle-finding algorithm
        fast = head.next
        slow = head.next.next

        # First meet
        while fast != slow and fast and slow and slow.next:		
            fast = fast.next
            slow = slow.next.next

        if not slow:
            return None

        # Second meet
        slow = head
        while fast and slow:
            if fast == slow:
                return fast
            fast = fast.next
            slow = slow.next