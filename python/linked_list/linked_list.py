from node import Node

class LinkedList:
	
	def __init__(self):

		self.head = None

	def append(self, newValue):
		newNode = Node(newValue, None)

		if self.head is None:
			self.head  = newNode

		elif self.head is not None and self.head.getNext() is None:
			self.head.setNext(newNode)

		else:
			current = self.head
			while current.getNext() is not None:
				current = current.getNext()
			current.setNext(newNode)

	def prepend(self, newValue):
		newNode = Node(newValue, self.head)
		self.head = newNode

	def insertAfter(self, newValue, position):
		counter = 0
		if self.head is not None:
			current = self.head
			while True:
				if counter is position:
					if current.getNext() is None:
						newNode = Node(newValue, None)
						current.setNext(newNode)

					else:
						newNode = Node(newValue, current.getNext())
						current.setNext(newNode)

					return True

				elif current.getNext() is None:
					return None

				elif counter < position:
					counter += 1
					current = current.getNext()

	def removeBeginning(self):
		self.head = self.head.getNext()

	def removeAfter(self, position):
		counter = 0
		if self.head is not None:
			current = self.head
			while True:
				if counter is position:
					if current.getNext() is None:
						return None

					elif current.getNext().getNext() is None:
						current.setNext(None)
						return True
					
					else:
						current.setNext(current.getNext().getNext())
						return True
						
				elif current.getNext() is None:
					return None

				elif counter < position:
					counter += 1
					current = current.getNext()


	def traverse(self):
		if self.head is not None:
			current = self.head
			while True:
				if current.getNext() is None:
					break
				else:
					current = current.getNext()

	def getPosition(self, position):
		counter = 0
		if self.head is not None:
			current = self.head
			while True:
				if counter is position:
					return current.getData()

				elif current.getNext() is None:
					return None

				elif counter < position:
					counter += 1
					current = current.getNext()

	def find(self, value):
		if self.head is None:
			return None
		else:
			current = self.head
			while True:
				if current.getData() is value:
					return True
				elif current.getNext() is None:
					return None
				else:
					current = current.getNext()

