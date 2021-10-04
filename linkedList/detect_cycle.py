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
        tor = head.next
        hare = head.next.next

        # First meet
        while hare != tor and tor and hare and hare.next:		
            tor = tor.next
            hare = hare.next.next

        if not hare:
            return None

        # Second meet
        tor = head
        while tor and hare:
            if tor == hare:
                return tor
            tor = tor.next
            hare = hare.next        