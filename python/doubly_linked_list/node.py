
class Node:

	def __init__(self):
		self.data = None
		self.prev = None
		self.next = None

	def __init__(self, value, pnode, nnode):
		self.data = value
		self.prev = pnode
		self.next = nnode

	def setData(self, value):
		self.data = value

	def setPrev(self, node):
		self.prev = node

	def setNext(self, node):
		self.next = node

	def getData(self):
		return self.data

	def getPrev(self):
		return self.prev

	def getNext(self):
		return self.next