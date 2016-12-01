# 1.1
# Implement an algorithm to determine if a string has all
# unique characters

import unittest


def unique(string1):
	# Check first if in ASCII character set
	if len(string1) > 128:
		return False

	# _ as throwaway variable
	# declare array and set to false
	char_set = [False for _ in range(128)]


	for char in string1:
		# Returns integer ASCII value 
		val = ord(char)

		if char_set[val]:
			# char is found in string
			return False

		# else return true
		char_set[val] = True

	return True

class Test(unittest.TestCase):
	testT = [('abcd'), ('s4fad'), ('')]
	testF = [('23ds2'), ('hb 627jh=j')]

	def test_unique(self):
		# check true
		for test_string in self.testT:
			actual = unique(test_string)
			# will return message if not true
			self.assertTrue(actual)

		# check false
		for test_string in self.testF:
			actual = unique(test_string)
			# will return message if not false
			self.assertFalse(actual)


if __name__ == "__main__":
	unittest.main()