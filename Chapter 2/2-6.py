# Implement a function to check if a linked list is a palindrome
"""
See: 
https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter%202/6_Palindrome.py
They have a more "linked list" approach than I do
"""


from LinkedList import LinkedList
from collections import Counter

def is_palindrome(ll):
	counter = []
	val = ll.head
	counter.append(val.value)
	count_steps = 1

	if count_length(ll) % 2 == 0:
		middle = count_length(ll) / 2
	else: 
		middle = count_length(ll) / 2 + 1

	while val.next != None:
		counter.append(val.next.value)
		count_steps += 1
		if count_steps == middle:
			middle_value = val.next.value
		val = val.next
	counter = Counter(counter)

	if all(counter[val] % 2 == 0 for val in counter):
		return True
	elif all(counter[val] % 2 == 0 for val in counter if val != middle_value):
		return True
	else:
		return False


def count_length(ll):
	val = ll.head
	length = 1
	while val.next != None:
		length += 1
		val = val.next
	return length


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
print 'Should be true', '\n'

ll_true2 = LinkedList([1, 4, 6, 6, 4, 1])
print(is_palindrome(ll_true2))
print 'Should be true', '\n'

ll_true3 = LinkedList([1, 4, 6, 2, 6, 4, 1])
print(is_palindrome(ll_true3))
print 'Should be true', '\n'

ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
print 'Should be false', '\n'