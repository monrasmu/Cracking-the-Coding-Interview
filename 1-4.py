# 1-4
# write a function to check if it is a permutation
# of a palindrome

import unittest
from collections import Counter

def palindromePerm(phrase):
    # function checks if a string is a permutation 
    # of a palindrome or not

    # populate array of zeros
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    
    countodd = 0
    for c in phrase:
        x = char_number(c)

        # First ensure that char is 1-26
        if x != -1:

        	# If so, populate table to count alphabet
            table[x] += 1

            # then count the number of odds
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1
                
    # return yes if only one odd
    return countodd <= 1

def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    # check if char is between a and z
    # change to numbers 1-26
    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = palindromePerm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()