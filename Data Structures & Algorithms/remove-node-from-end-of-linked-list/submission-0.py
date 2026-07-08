# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0;
        curr = head;
        while curr:
            counter += 1;
            curr = curr.next
        
        dummy = ListNode(0, head)
        index = counter - n
        prev = dummy
        curr = head;
        while index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        
        prev.next = curr.next
        return dummy.next
            

           
        

        

        

                

                


            
