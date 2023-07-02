from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def main():
    list = ListNode(2,
                    ListNode(1,
                             ListNode(3,
                                      None)))
    print(Solution.reverseList(Solution(), list))


if __name__ == "__main__":
    main()
