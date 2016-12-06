# Use a single array to implement three stacks

from Multistack import MultiStack
import unittest

def ThreeInOne():
    answers = []

    # Create a new stack of len 2 and number 3
    stack = MultiStack(2, 3)

    # Should be empty right now
    answers.append(stack.IsEmpty(1))

    # Push value 3 to top of stack 1
    stack.Push(3, 1)

    # Check value at end of stack 1
    answers.append(stack.Peek(1))

    # Now stack is not empty
    answers.append(stack.IsEmpty(1))

    # Stack 1 is now 3 -> 2
    stack.Push(2, 1)

    # Check value
    answers.append(stack.Peek(1))

    # Pop off 2
    answers.append(stack.Pop(1))

    # Check value
    answers.append(stack.Peek(1))

    stack.Push(3, 1)

    return answers


class TestingThreeInOne(unittest.TestCase):

    def test_ThreeInOne(self):
        data = [True, 3, False, 2, 2, 3]
        self.assertEqual(ThreeInOne(), data)



if __name__ == "__main__":
    unittest.main()