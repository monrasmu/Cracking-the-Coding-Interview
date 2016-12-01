# 1-1
# Algorithm to check if unique characters

import unittest

def unique(string):
	# if not in ASCII characters
	if len(string) > 128:
		return false

	# define array and set to false
	array_char = [False for _ in range(128)]

	for char in string:
		val = ord(char)
		if array_char[val]:
			return False
		array_char[val] = True
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
