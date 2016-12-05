# Partition a linked list around a value x, such that all nodes less than
# x come before all nodes greater than or equal to x
# EX: input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
#    output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from LinkedList import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head
    print current

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode
        
    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)