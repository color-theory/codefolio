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
	
	def __add__(self, value):
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

	def __radd__(self, other):
		return self.__add__(other)	
