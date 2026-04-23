# week09-3.py (使用「函式呼叫函式」Recursion)
# week09-2.py (先變陣列、再變成 Linked List)
# LeetCode 75: Linked List Q3 206. Reverse Linked List
# 把它反過來

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head # 終止條件(最簡單的狀況)
        head2 = head.next
        ans = self.reverseList(head.next) # 函式呼叫函式
        head2.next, head.next = head, None
        return ans

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
