# Given two singly linked lists, determine if the two lists intersect
# Return the intersecting node
# Note that the intersection is defined based on reference, not value
# That is, if the kth node of the first linked list is the exact same node
# (by reference) as the jth node of the second linked list, then they are 
# intersecting

from LinkedList import LinkedList

def intersecting(ll1, ll2):
	# If tails aren't the same, return False as they aren't linked
	if ll1.tail.value != ll2.tail.value:
		return False

	val1, val2 = ll1.head, ll2.head
	# if LL1 is longer, start moving through it first
	if len(ll1) > len(ll2):
		seen = []
		while val1 != None:
			seen.append(val1.value)
			val1 = val1.next

	# if LL2 is longer, move through it first instead
	else:
		while val2 != None:
			val2 = val2.next
			print val2
	return False



ll1 = LinkedList()
ll1.add_multiple([1, 2, 3, 4, 5, 6, 7])
ll2 = LinkedList()
ll2.add_multiple([9, 4, 5, 6, 7])
print intersecting(ll1, ll2)
print 'Should be 4'
print '\n'

ll3 = LinkedList()
ll3.add_multiple([1, 2, 3, 4, 5, 6, 7])
ll4 = LinkedList()
ll4.add_multiple([9, 8, 7])
print intersecting(ll3, ll4)
print 'Should be 7'
print '\n'

ll5 = LinkedList()
ll5.add_multiple([1, 2, 3, 4, 5])
ll6 = LinkedList()
ll6.add_multiple([9, 8, 7])
print intersecting(ll5, ll6)
print 'Should be False'