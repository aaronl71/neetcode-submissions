# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       #merge two lists together at a time iteratively
       if len(lists) == 0:
        return None
       l1 = lists[0]
       i = 1

       while i < len(lists):
        l2 = lists[i]
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        i += 1
        l1 = dummy.next
       return dummy.next
    
       



        
       
        
         