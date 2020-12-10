import sys

#Formats the inputed exuation to a matrix row
def Format(*eq):
	eq = list(eq)[0]

	for e in range(len(eq)):
		eq[e] = eq[e].strip().split(' ')

	for i in range(len(eq)):		
		for j in range(1, len(eq[i])-1):
		
			if j != 0:
				eq[i][j] = str(eq[i][j])[1:-1]

		eq[i][0] = str(eq[i][0])[:-1]
		eq[i][-1] =str(eq[i][-1])[1:]
	
	for i in range(len(eq)):
		for j in range(len(eq[i])):
			eq[i][j] = float(eq[i][j])
	
	return eq




#Multiplies a vector or matrix row with a scalar
def mult(vector, k):
	for i in range(len(vector)):
		vector[i] *= k
	return vector

#Adds two matrix rows, or vectors, together
def add(vector1, vector2):
	for i in range(len(vector1)):
		vector1[i] += vector2[i]
	return vector1




#Performs Gaussian elimination on a matrix
def gaussianElimination(matrix):
	col = 0

	while col < len(matrix[0]) -1:

		for row in range(0, len(matrix)):
			#Handles if col,col is zero to avoid ZeroDivisionError later
			if matrix[col][col] ==0:

				#Checks for which rows to switch
				if col !=  len(matrix):
					index = col+1
					index %= len(matrix)
					reps = 0

					#Makes sure that the row it switches with is not zeor in the same position
					while True:
						if matrix[col][index] !=0:
							r = matrix[index]
							break
						else:
							index +=1
							index %= len(matrix)
							reps +=1
						if	reps == len(matrix):
							print('There exists no solutions to the gives set of equations')
							sys.exit()

					#Performs the actual swtich		
					matrix[index] = matrix[col]
					matrix[col] = r


			#The actual gaussian elimination
			if row != col and matrix[row][col] != 0:
				k = matrix[row][col]/matrix[col][col]
				r = mult(matrix[col], -1*k)
								
				add(matrix[row], r)
				
		col +=1

	#Make all values for the vars in the matrix 1
	for i in range(0, len(matrix[0]) -1):
		k = 1/matrix[i][i]
		r = mult(matrix[i], k)
	
	return matrix




with open('equations.txt', 'r') as f:
	s = f.readlines()

matrix = s.copy()
matrix = Format(matrix)
gaussianElimination(matrix)


#Prints the system of equations followed by the values for the variables
for eq in s:
	print(eq)
print('\n')
for i in range(len(s)):
	print(f'x{i} = {matrix[i][-1]}')
