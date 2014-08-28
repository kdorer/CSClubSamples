
class Node:

	def __init__(self):
		self.data = None
		self.next = None

	def __init__(self, value, node):
		self.data = value
		self.next = node

	def setData(self, value):
		self.data = value

	def setNext(self, node):
		self.next = node

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

