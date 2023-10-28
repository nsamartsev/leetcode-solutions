from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):

        # defining a blank res variable
        res = ""

        # initializing ptr to head
        ptr = self

        # traversing and adding it to res
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next

        # removing trailing commas
        res = res.strip(", ")

        # chen checking if
        # anything is present in res or not
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
