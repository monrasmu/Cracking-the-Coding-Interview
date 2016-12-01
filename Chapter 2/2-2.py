# Implement an algorithm to find the kth to last element
# of a singly linked list

from LinkedList import LinkedList

def kth_to_last(ll, k):
	num_seen = 1
	length_list = count_length(ll)

	# Start at head
	val = ll.head
	# While we haven't reached the end, keep running
	while num_seen < (length_list - k):
		val = val.next
		num_seen += 1
	return val


# Counts length of LL
def count_length(ll):
	val = ll.head
	# Start count at 1 for head
	count = 1
	# While we haven't reached the end of the list
	while val.next != None:
		count += 1
		val = val.next
	return count


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))