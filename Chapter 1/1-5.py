# Given two strings,, write a function to check if they
# are one edit away
# ex: pale, ple -> true
# ex: pale, bake -> false

import unittest


# get characters into 1-26 format
def char_number(c):
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')

	val = ord(c)

	if a <= val <= z:
		return (val - a)
	elif A <= val <= Z:
		return (val - A)
	return -1 

def oneAway(string1, string2):
	table1 = [0 for _ in range(ord('z') - ord('a') + 1)]
	table2 = [0 for _ in range(ord('z') - ord('a') + 1)]

	print(string1, string2)

	for char in string1:
		x = char_number(char)

		if x != -1:
			table1[x] += 1

	for char in string2:
		x2 = char_number(char)

		if x2 != -1:
			table2[x2] += 1

	# One replacement
	if len(string1) == len(string2):
		diff = [0 for _ in range(ord('z') - ord('a') + 1)]
		for x in range(len(table1)):
			diff[x] = table1[x] - table2[x]
		if diff.count(1) > 1:
			return False
		elif diff.count(-1) > 1:
			return False
		elif sum(diff) == 0:
			return True
		return False

	# one insert
	if len(string1) == (len(string2) + 1):
		diff = [0 for _ in range(ord('z') - ord('a') + 1)]
		for x in range(len(table1)):
			diff[x] = table1[x] - table2[x]
		if diff.count(1) > 1:
			return False
		elif diff.count(-1) > 1:
			return False
		elif sum(diff) == 1:
			return True
		return True

	# one removal
	if len(string1) == (len(string2) - 1):
		diff = [0 for _ in range(ord('z') - ord('a') + 1)]
		for x in range(len(table1)):
			diff[x] = table1[x] - table2[x]
		if diff.count(1) > 1:
			return False
		#elif
		elif diff.count(-1) > 1:
			return False
		elif sum(diff) == 1:
			return True
		return True

	return False
	



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
        ]

    def test_oneAway(self):
        for [test_string1, test_string2, expected] in self.data:
            actual = oneAway(test_string1, test_string2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()