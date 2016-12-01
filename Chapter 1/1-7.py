# rotate an N x N matrix 90 degrees

import unittest
import numpy as np

def rotateMatrix(matrix):
	# ensure matrix is N X N
	array = np.array(matrix)
	size = array.shape
	if size[0] != size[1]:
		return False
	size = size[0]

	# populate new matrix
	newMatrix = [[0 for i in range(size)] for j in range(size)]

	# rotate matrix
	for x in range(size):
		for y in range(size):
			newMatrix[y][size - 1 - x] = matrix[x][y]
	return newMatrix




class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotateMatrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotateMatrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()