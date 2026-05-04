# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def findkth(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr
        dummy=ListNode(0)
        dummy.next=head
        gprev=dummy

        while True:
            kth=findkth(gprev,k)
            if not kth:
                break
            
            gnext=kth.next

            prev, curr =kth.next ,gprev.next

            while curr!=gnext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=gprev.next
            gprev.next=kth
            gprev=temp
        return dummy.next
