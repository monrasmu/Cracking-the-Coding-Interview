# Remove duplicates from a linked list

from LinkedList import LinkedList

def remove_dups(LinList):
    val = LinList.head
    vals_seen = set([val.value])
    while val.next:
        if val.next.value in vals_seen:
            val.next = val.next.next
        else:
            vals_seen.add(val.next.value)
            val = val.next
    return LinList


LinList = LinkedList()
LinList.generate(100, 0, 9)
print(LinList)
remove_dups(LinList)
print '\n'
print(LinList)
