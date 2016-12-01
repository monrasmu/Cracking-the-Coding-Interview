# Implement an algorithm to delete a node; you are only 
# given access to that node

from LinkedList import LinkedList

def delete_middle_node(middle_node):
	# Replaces value at node with next
	middle_node.value = middle_node.next.value

	# Move us one forward
	middle_node.next = middle_node.next.next


ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)