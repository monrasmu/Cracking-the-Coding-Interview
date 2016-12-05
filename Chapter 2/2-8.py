# Given a circular linked list, implement an algorithm that returns the node
# at the beginning of the loop.
# EXAMPLE
# Input: A -> B -> C -> D -> E - > C [the same C as earlier]
# Output: C

from LinkedList import LinkedList


def loop_detection(ll):
	# Only works for even length LLs
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
        	break

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast