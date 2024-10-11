class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        current = head
        while current:
            length += 1
            current = current.next


        if n == length:
            return head.next

        current = head
        for i in range(length - n - 1):
            print(i, current.val)
            current = current.next

        current.next = current.next.next

        return head
