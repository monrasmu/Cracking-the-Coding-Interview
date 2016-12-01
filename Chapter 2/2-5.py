"""
You have two numbers represented by a linked list, where each node 
contains a single digit. The digits are stored in reverse order, 
such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2) That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
"""

from LinkedList import LinkedList
import unittest

def sum_lists(ll_1, ll_2):
	val1, val2 = ll_1.head, ll_2.head
	sum1, sum2 = val1.value, val2.value
	count1, count2 = 1, 1

	# While going through linked list, assign values of val.next
	# in correct position (aka use 10^count) into sum
	while val1.next != None:
		sum1 += (val1.next.value * (10 ** count1))
		count1 += 1
		val1 = val1.next
	while val2.next != None:
		sum2 += (val2.next.value * (10 ** count2))
		count2 += 1
		val2 = val2.next
		
	# Reverse the total sum
	sumTotal = reverse(sum1 + sum2)

	# Populate a new linked list
	ll_new = LinkedList()
	ll_new.add_multiple(sumTotal)
	return ll_new

def reverse(num):
	# Reverses number and returns as string
	return (str(num)[::-1])



ll_1 = LinkedList()
ll_1.add_multiple([1, 2, 3])
ll_2 = LinkedList()
ll_2. add_multiple([4, 5, 6])
print 'Actual:', sum_lists(ll_1, ll_2)
print 'Expected: 5 -> 7 -> 9'

print '\n'

ll_3 = LinkedList()
ll_3.add_multiple([3, 2, 1])
ll_4 = LinkedList()
ll_4. add_multiple([5, 5, 5])
print 'Actual:', sum_lists(ll_3, ll_4)
print 'Expected: 8 -> 7 -> 6'

print '\n'

ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))