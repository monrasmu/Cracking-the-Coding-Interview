# Write code to remove duplicates from an unsorted linked list
# Couldn't figure out--taken from solutions

from LinkedList import LinkedList

def remove_dups(ll):
    # start at head
    val = ll.head
    vals_seen = set([val.value])

    while val.next:
        if val.next.value in vals_seen:
            # if next value has already been seen
            # skip value and assign to one after
            # then start over with this value
            val.next = val.next.next
        else:
            # else add to the seen values
            vals_seen.add(val.next.value)
            # start with next value
            val = val.next
    return vals_seen


ll = LinkedList()

# Test 1--generates random LL
ll.generate(10, 0, 9)
print(ll)
print '\n'
remove_dups(ll)
print(ll)
print '\n'
print '\n'

# Test 2
ll.generate(100, 0, 9)
print(ll)
print '\n'
remove_dups(ll)
print(ll)