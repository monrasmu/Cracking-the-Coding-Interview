# compress string
# ex: aabcccccaaa -> a2b1c5a2

import unittest
from collections import Counter


def compressString(string):
	compress = []
	counter = 0
	
	# count up number of each
	for c in range(len(string)):
		# as soon as they stop being equal we want to append and reset counter
		if c != 0 and string[c] != string[c - 1]:
			compress.append(string[c - 1] + str(counter))
			counter = 0
		counter += 1

	# add the last character
	compress.append(string[-1] + str(counter))

	# fix spacing
	compress = ''.join(compress)

	# checks to see if compressed string is smaller
	string1 = min(string, compress, key=len)
	return string1



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_compressString(self):
        for [test_string, expected] in self.data:
            actual = compressString(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()