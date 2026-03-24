# Second Middle Node of a Singly Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        """
        Return the middle node of a singly linked list. If the list has an even number of nodes,
        return the second middle node.

        :param head: The head ListNode of the linked list (or None for empty list).
        :return: The middle ListNode, or None if the list is empty.
        """
        if head is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next  # type: ignore[assignment]
            fast = fast.next.next
        return slow
