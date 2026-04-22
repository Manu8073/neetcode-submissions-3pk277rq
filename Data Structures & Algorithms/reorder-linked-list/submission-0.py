# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next :
            return 
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        prev=None
        slow.next=None


        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        first,second=head,prev

        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
