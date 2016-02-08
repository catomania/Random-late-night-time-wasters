#Write an algorithm such that if an element in an MxN matrixis 0, its entire row
#and column are set to 0.

def grab_dimensions(matrix):
	row_length = len(matrix)

	col_length = len(matrix[0])

	row_count = 0
	elem_count = 0

	zero_storage = []

	# crawl elements for zero:
	for row in matrix:
		for element in row:

			if element == 0:
				zero_storage.append([[int(row_count)] + [int(elem_count)]])
			if elem_count == col_length - 1:
				elem_count = 0
			else:
				elem_count += 1
		row_count += 1
	
	for pair in zero_storage:
		for x in pair:

			# set zero's for all rows that contain 0
			for row in range(0, int(row_length)):
				matrix[int(row)][int(x[1])] = 0

			# set zero's for all cols that contain 0	
			for col in range(0, int(col_length)):
				matrix[int(x[0])][int(col)] = 0

	print matrix

sample_matrix = [[1, 2, 3], [4, 5, 0], [7, 8, 9], [0, 11, 12]]
grab_dimensions(sample_matrix)




##[ 1  2  3 ]
##[ 4  5  0 ]
##[ 7  8  9 ]
##[ 0  11  12 ]
##
##Visual representation of contents after zeroing all rows/columns containing a zero:
##[ 0  2  0 ]
##[ 0  0  0 ]
##[ 0  8  0 ]
##[ 0  0  0 ]



