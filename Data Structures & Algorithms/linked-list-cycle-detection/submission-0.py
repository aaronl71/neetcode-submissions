# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict = {} #mapping val to freq
        curr = head
        if curr is None:
            return False 
        while curr:
            dict[curr] = dict.get(curr, 0) + 1
            if dict[curr] > 1:
                return True
            curr = curr.next
        return False