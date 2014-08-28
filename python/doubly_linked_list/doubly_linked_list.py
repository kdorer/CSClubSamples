from node import Node

class DoublyLinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def prepend(self, value):
		if self.head is None:
			newNode = Node(value, None, None)
			self.head = self.tail = newNode

		elif self.head is self.tail:
			newNode = Node(value, None, self.head)
			self.head.setPrev(newNode)
			self.head = newNode
		
		else:
			newNode = Node(value, None, self.head)
			self.head.setPrev(newNode)
			self.head = newNode

	def append(self, value):
		if self.head is None:
			newNode = Node(value, None, None)
			self.head = self.tail = newNode

		elif self.head is self.tail:
			newNode = Node(value, self.tail, None)
			self.tail.setNext(newNode)
			self.tail = newNode
		
		else:
			newNode = Node(value, None, self.head)
			self.tail.setNext(newNode)
			self.tail = newNode

	def insertAfter(self, value, position):
		if self.head is None:
			return None

		elif self.head is self.tail:
			if position is not 0:
				return None
			else:
				newNode = Node(value, self.head, None)
				self.head.setNext(newNode)
				self.tail = newNode

		else:
			counter = 0
			current = self.head
			while True:
				if position is counter:
					if current is self.tail:
						newNode = Node(value, current, None)
						current.setNext(newNode)
						self.tail = newNode
						break

					else:
						newNode = Node(value, current, current.getNext())
						current.getNext().setPrev(newNode)
						current.setNext(newNode)
						break

				elif current is self.tail:
					return None

				else:
					current = current.getNext()
					counter = counter + 1


		return True


	def removeBeginning(self):
		if self.head is None:
			return None

		elif self.head is self.tail:
			self.head = self.tail = None

		else:
			self.head = self.head.getNext()
			self.head.setPrev(None)

		return True

	def removeEnd(self):
		if self.tail is None:
			return None

		elif self.head is self.tail:
			self.head = self.tail = None

		else:
			self.tail = self.tail.getPrev()
			self.tail.setNext(None)

		return True

	def removeAfter(self, position):
		if self.head is None:
			return None

		elif self.head is self.tail:
			return None

		else:
			counter = 0
			current = self.head
			while True:
				if position is counter:
					if current is self.tail:
						return None

					elif current.getNext() is self.tail:
						current.setNext(None)
						self.tail = current

					else:
						current.getNext().getNext().setPrev(current)
						current.setNext(current.getNext().getNext())
						break

				elif current is self.tail:
					return None

				else:
					current = current.getNext()
					counter = counter + 1

		return True

	def traverse(self):
		current = self.head
		while True:
			print (current.data)
			if current is not self.tail:
				current = current.getNext()
			else:
				break

	def getPosition(self, position):
		if self.head is None:
			return None

		elif self.head is self.tail:
			if position is not 0:
				return None
			else:
				return self.head.getData()

		else:
			counter = 0
			current = self.head
			while True:
				if position is counter:
					return current.getData()

				elif current is self.tail:
					return None

				else:
					current = current.getNext()
					counter = counter + 1

		return True

	def find(self, value):
		if self.head is None:
			return None

		current = self.head
		while True:
			if current.getData() is value:
				break

			elif current is self.tail:
				return None

			else:
				current = current.getNext()

		return True
