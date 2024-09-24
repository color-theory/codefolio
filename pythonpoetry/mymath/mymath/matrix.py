class Matrix:
	rows = 0
	columns = 0
	matrix = []
	matrixRow = []
	dataCount = 0
	matrixList = []
	tempProduct = 0

	def __init__(self, rows, columns, data = []):
		if data == []:
			data = [None] * (rows * columns)
		self.matrix = []
		self.rows = rows
		self.columns = columns
		for i in range(rows):
			self.matrixRow = []
			for j in range(columns):
				self.matrixRow.append(data[self.dataCount])
				self.dataCount += 1
			self.matrix.append(self.matrixRow)