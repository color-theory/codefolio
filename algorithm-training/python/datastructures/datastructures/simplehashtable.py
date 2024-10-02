class SimpleHashTable:
	def __init__(self, size):
		self.size = size
		self.table = [None] * size

	def insert(self, key, value):
		if key < 0 or key >= self.size:
			raise ValueError("Key out of range for this hash table")
		self.table[key] = value

	def __setitem__(self, key, value):
		self.insert(key,value)

	def lookup(self, key):
		if key < 0 or key >= self.size:
			return None
		return self.table[key]

	def __getitem__(self, key):
		return self.lookup(key)