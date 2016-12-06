# How would you design a stack which, inaddition to push and pop,
# has a function min which returns the minimum element

from Multistack import MultiStack
import unittest

def callMin():
	# Create one stack
	stack = MultiStack(6, 1)
	stack.Push(1, 0)
	stack.Push(3, 0)
	stack.Push(1, 0)
	stack.Push(2, 0)
	stack.Push(2, 0)
	stack.Push(4, 0)
	print stack.Min(0)

class TestingMin(unittest.TestCase):

    def test_Min(self):
        data = [1, 3, 1, 2, 2, 4]
        self.assertEqual(callMin(), min(data))



if __name__ == "__main__":
	callMin()
    #unittest.main()