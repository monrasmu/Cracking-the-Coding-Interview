# 1-3
# Write a method to replace all spaces in a string with '%20'

import unittest

def urlify(string, length):
	# populate a new string of len(string)
	newstring = [None] * length

	# replace values in new string with values needed
	for m in range(length):
		if (ord(string[m]) == 32):
			newstring[m] = '%20'
		else:
			newstring[m] = string[m]
	newstring2 = ''.join(newstring)

	return newstring2

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [('much ado about nothing      ', 22, 
    	     'much%20ado%20about%20nothing'),
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()