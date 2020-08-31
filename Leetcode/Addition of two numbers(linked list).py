# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1=l1
        cur2=l2
        temp=None
        prev=None
        _carry=0
        while(cur1!=None and cur2!=None):
            _sum=(cur1.val+cur2.val+_carry)%10
            _carry=(cur1.val+cur2.val+_carry)//10

            if temp is None:
                temp=ListNode(_sum)
                prev=temp
            else:
                prev.next=ListNode(_sum)
                prev=prev.next
            cur1=cur1.next
            cur2=cur2.next
            
        while(cur1!=None):
            _sum=(cur1.val+_carry)%10
            _carry=(cur1.val+_carry)//10
            if temp is None:
                temp=ListNode(_sum)
                prev=temp
            else:
                prev.next=ListNode(_sum)
                prev=prev.next
            cur1=cur1.next
            
        while(cur2!=None):
            _sum=(cur2.val+_carry)%10
            _carry=(cur2.val+_carry)//10
            if temp is None:
                temp=ListNode(_sum)
                prev=temp
            else:
                prev.next=ListNode(_sum)
                prev=prev.next
            cur2=cur2.next
            
        if _carry:
            prev.next=ListNode(_carry)
            prev=prev.next
        return temp
