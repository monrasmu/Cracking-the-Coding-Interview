# Given a circular linked list, implement an algorithm that returns the node
# at the beginning of the loop.
# EXAMPLE
# Input: A -> B -> C -> D -> E - > C [the same C as earlier]
# Output: C

from LinkedList import LinkedList

def detect_loop(ll):
	# start both at head
	val = ll.head
	seen = [val.value]
	while val is not None:
		val = val.next
		seen.append(val.value)
		if val.value in seen:
			return val

ll = LinkedList([1, 2, 3, 4, 2])
print ll
print(detect_loop(ll))

