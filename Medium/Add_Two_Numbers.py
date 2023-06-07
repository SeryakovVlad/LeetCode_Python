class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)  # Initialize the head of the result list.
        current = head  # Current node in new list.
        carry = 0  # Initialize carry 

        while l1 or l2 or carry:  # while there are still digits to process in l1, l2, or carry
            sum_value = carry
            # Add the values from l1 and l2 if they are not None.
            if l1:
                sum_value += l1.val
                l1 = l1.next
            if l2:
                sum_value += l2.val
                l2 = l2.next

            # Determine the carry and the digit for the current place.
            carry, digit = divmod(sum_value, 10)
            current.next = ListNode(digit)
            current = current.next

        return head.next