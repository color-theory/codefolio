class Matrix:
	rows = 0
	columns = 0
	matrix = []
	matrixRow = []
	dataCount = 0
	tempMatrixList = []
	tempProduct = 0

	def __init__(self, rows, columns, data = []):
		if data == []:
			data = [None] * (rows * columns)
		self.matrix = []
		self.rows = rows
		self.columns = columns
		if( len(data) < rows * columns):
			data += [None] * (rows * columns - len(data))
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
	