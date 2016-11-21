from LinkedList import LinkedList

def remove_dups(LinList):
	if LinList.head is None:
    	return 0

    current = LinList.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return LinList


def remove_dups_followup(LinList):
    if LinList.head is None:
        return

    current = LinList.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return LinList.head


LinList = LinkedList()
LinList.generate(100, 0, 9)
print(LinList)
remove_dups(LinList)
print(LinList)

LinList.generate(100, 0, 9)
print(LinList)
remove_dups_followup(LinList)
print(LinList)