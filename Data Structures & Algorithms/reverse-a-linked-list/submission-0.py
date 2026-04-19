# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        curr=head
        pri=None

        while curr:
            temp=curr.next
            curr.next=pri
            pri=curr
            curr=temp
        return pri