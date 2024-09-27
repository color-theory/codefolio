class Matrix:
	rows = 0
	columns = 0
	matrix = []
	matrixRow = []
	dataCount = 0
	tempMatrixList = []
	tempProduct = 0

	def __init__(self, rows, columns, data = []):
		self.matrix = []
		self.rows = rows
		self.columns = columns
		if( len(data) != rows * columns):
			raise ValueError("Data size does not match matrix size")
		for i in range(rows):
			self.matrixRow = []
			for j in range(columns):
				self.matrixRow.append(data[self.dataCount])
				self.dataCount += 1
			self.matrix.append(self.matrixRow)
	
	def add(self, value):
		if( type(value) == int):
			self.tempMatrixList = []
			for i in range(self.rows):
				for j in range(self.columns):
					self.tempMatrixList.append(self.matrix[i][j] + value)
		elif( type(value) == Matrix):
			self.tempMatrixList = []
			if self.rows != value.rows or self.columns != value.columns:
				raise ValueError("Matrices are not of the same size")
			for i in range(self.rows):
				for j in range(self.columns):
					self.tempMatrixList.append(self.matrix[i][j] + value.matrix[i][j])
		else:
			return NotImplemented
		return Matrix(self.rows, self.columns, self.tempMatrixList)

	def __add__(self, value):
		return self.add(value)
	
	def __radd__(self, other):
		return self.add(other)

	def multiply(self, value):
		if( type(value) == int):
			self.tempMatrixList = []
			for i in range(self.rows):
				for j in range(self.columns):
					self.tempMatrixList.append(self.matrix[i][j] * value)
		elif( type(value) == Matrix):
			self.tempMatrixList = []
			if self.columns != value.columns or self.rows != value.rows:
				raise ValueError("Matrices are not of the same size")
			for i in range(self.rows):
				for j in range(value.columns):
					self.tempMatrixList.append(self.matrix[i][j] * value.matrix[i][j])
		else:
			return NotImplemented
		return Matrix(self.rows, self.columns, self.tempMatrixList)
	
	def __mul__(self, value):
		return self.multiply(value)
	
	def __rmul__(self, other):
		return self.multiply(other)
	
	def dot(self, value):
		if( type(value) == Matrix):
			if self.columns != value.rows:
				raise ValueError("Matrices are not of compatible size")
			self.tempMatrixList = []
			for i in range(self.rows):
				for j in range(value.columns):
					self.tempProduct = 0
					for k in range(self.columns):
						self.tempProduct += self.matrix[i][k] * value.matrix[k][j]
					self.tempMatrixList.append(self.tempProduct)
		else:
			return NotImplemented
		return Matrix(self.rows, value.columns, self.tempMatrixList)
	
	def transpose(self):
		self.tempMatrixList = []
		for i in range(self.columns):
			for j in range(self.rows):
				self.tempMatrixList.append(self.matrix[j][i])
		return Matrix(self.columns, self.rows, self.tempMatrixList)
	
	def flatten(self):
		self.tempMatrixList = []
		for r in range(self.rows):
			for c in range(self.columns):
				self.tempMatrixList.append(self.matrix[r][c])
		return self.tempMatrixList
	
	def copy(self):
		return Matrix(self.rows, self.columns, self.flatten())
	
	def determinant(self):
		if self.rows != self.columns:
			raise ValueError("Matrix is not square")
		if self.rows == 2:
			return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
		
		result = 0
		rows = list(range(len(self.matrix)))
		for focus in rows:
			tempMatrix = self.copy()
			tempMatrix.matrix = tempMatrix.matrix[1:]
			subrows = len(tempMatrix.matrix)
			for j in range(subrows):
				tempMatrix.matrix[j] = tempMatrix.matrix[j][0:focus] + tempMatrix.matrix[j][focus+1:]
			sign = (-1) ** (focus % 2)
			tempMatrix.rows -= 1
			tempMatrix.columns -= 1
			subdeterminant = tempMatrix.determinant()

			result += sign * self.matrix[0][focus] * subdeterminant
		return result