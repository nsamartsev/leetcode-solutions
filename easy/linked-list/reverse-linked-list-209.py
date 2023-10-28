from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = ""
        ptr = self
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
        res = res.strip(", ")
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


class Solution:
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


list = ListNode(1,
                ListNode(2,
                         ListNode(3,
                                  None)))

print(Solution.reverseList(list))
