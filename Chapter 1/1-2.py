# Given two strings, write a method to decide
# if one is a permutation of the other
import unittest
from collections import Counter

def perm(string):
	string1 = string[0]
	string2 = string[1]

	# must be same length
	if len(string1) != len(string2):
		return False

	# want to know if they contain same chars
	# make a counter
	count1 = Counter(string1)
	count2 = Counter(string2)
	if count1 == count2:
		return True
	return False


	# THEIR WAY
	"""
	counter = Counter()
	for c in string1:
		counter[c] += 1
	for c in string2:
		if counter[c] == 0:
			return False
		counter[c] -= 1
	return True
	"""



class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = perm(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = perm(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()