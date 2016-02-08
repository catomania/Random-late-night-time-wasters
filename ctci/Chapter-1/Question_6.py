# reverse a matrix 90 degrees clockwise

class MatrixProcessor:
	
	def __init__(self, matrix):
		self.n = len(matrix) # how many rows within the matrix
		self.m = len(matrix[0]) # how many 'columns' within the matrix
		self.matrix = matrix # why so many selves??? 

	def print_me(self): # why do functions need self? 
		print self.n
		print self.m
		print self.matrix

	#def __str__(self):
		# iterate over rows and matrix by generator (why generator?)
		# join cell and row into final string output hmmm hmmm


	def reverse_me(self):
		# create empty list to place my rotated matrix
		actual_matrix = []

		# using the zip method, not sure if allowed or not :)
		zipped_matrix = zip(*self.matrix)

		# reverse elements in my zipped matrix to complete rotation 
		for x in zipped_matrix:
			reversed_element = reversed(x)
			reversed_list = []
			for i in reversed_element:
				reversed_list.append(i)
			actual_matrix.append(reversed_list)
			
		print actual_matrix


		# build a new matrix by splitting out elements backwards

	def rotate90CW(self):
		# make an empty list for each iterable in matrix
		columnlist = [[] for i in range(len(self.matrix))] 

		# take first row and assign 1st element to first col, and so on
		# do that with the rest of the rows

		[[columnlist[i].append(row[i]) for i in range(len(row))] for row in self.matrix]

		#[[columnlist[i].append(row[i]) for i in range(len(row))] for row in self.matrix]	
		print columnlist
		print len(self.matrix)
		print len(row)

		for row in self.matrix:
			print row
			for i in range(len(row)):
				print str(row[i]) + " " + str(i)


#matrix_input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix_input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
testing_me = MatrixProcessor(matrix_input)
#testing_me.reverse_me()

testing_me.rotate90CW()



##M by N matrix has dimensions 4 by 4
##Visual representation of contents:
##[ 1  2  3  4 ]
##[ 5  6  7  8 ]
##[ 9  10  11  12 ]
##[ 13  14  15  16 ]
##
##Visual representation of contents after rotating 90 degrees clockwise:
##[ 13  9  5  1 ]
##[ 14  10  6  2 ]
##[ 15  11  7  3 ]
##[ 16  12  8  4 ]

