# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        '''
        Given head of singly LL

        Reverse The List

        Return list in reversed order
        

        PSUEDO:

        
        
        previous = None
        current = Head

        while currrent is not None:

            next_node = current.next       //saving the next 
            current.next = previous        // reverse pointer
            previous = current             // move prev forward
            current = next_node            // move curr forward

        return previous                    // new head

        

        '''

        # 'prev' will end up as the new head of the reversed list
        prev = None
        # 'curr' is our pointer walking through the original list 
        curr = head  #initialy this points to 1 

        # iterate until we pass the tail (curr becomes None)
        while curr is not None:
            # 1) save the next node before we break the link
            next_node = curr.next

            # 2) reverse the link: point current node back to prev
            curr.next = prev

            # 3) advance both pointers forward
            prev = curr
            curr = next_node

        # 'prev' now points to the first node of the reversed list
        return prev
