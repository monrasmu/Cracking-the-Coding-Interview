# Write an algorithm such that if an element in an MxN matrix is 0
# then it's entire row and column are set to 0

import unittest

def zero_matrix(matrix):
	row = []
	sizex = len(matrix[0])
	sizey = len(matrix[1])

	for i in range(sizex):
		if matrix[i] != 0:
			row.append(matrix[i])
		else:
			row.append(0)
		print row

	"""
	newMatrix = [[1 for i in range(len(matrix))] for j in range(len(matrix))]
	for i in range(len(matrix[0])):
		for j in range(len(matrix[1])):
			if matrix[i][j] != 0:
				newMatrix[i][j] = matrix[i][j]
			elif matrix[i][j] == 0:
				newMatrix = rowZero(i, matrix)
				newMatrix = colZero(j, matrix)
			print newMatrix
	return newMatrix

def rowZero(row, matrix1):
	for j in range(len(matrix1[0])):
		matrix1[row][j] = 0
	return matrix1

def colZero(col, matrix2):
	for i in range(len(matrix2[1])):
		matrix2[i][col] = 0
	return matrix2
	"""


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()