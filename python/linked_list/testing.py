import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):


	def setUp(self):
		self.testList = LinkedList()
		self.values = [1, 3, 4, 9, 2]
		for i in self.values:
			self.testList.append(i)


	def testAppend(self):
		self.assertEqual(self.testList.getPosition(0), 1)
		self.assertEqual(self.testList.getPosition(1), 3)
		self.assertEqual(self.testList.getPosition(2), 4)
		self.assertEqual(self.testList.getPosition(3), 9)
		self.assertEqual(self.testList.getPosition(4), 2)

	def testPrepend(self):
		self.testList.prepend(6)
		self.assertEqual(self.testList.getPosition(0), 6)
		self.assertEqual(self.testList.getPosition(1), 1)
		self.assertEqual(self.testList.getPosition(2), 3)
		self.assertEqual(self.testList.getPosition(3), 4)
		self.assertEqual(self.testList.getPosition(4), 9)
		self.assertEqual(self.testList.getPosition(5), 2)

	def testInsertAfter(self):
		self.testList.insertAfter(8, 3)
		self.testList.insertAfter(5, 5)
		self.assertEqual(self.testList.getPosition(0), 1)
		self.assertEqual(self.testList.getPosition(1), 3)
		self.assertEqual(self.testList.getPosition(2), 4)
		self.assertEqual(self.testList.getPosition(3), 9)
		self.assertEqual(self.testList.getPosition(4), 8)
		self.assertEqual(self.testList.getPosition(5), 2)
		self.assertEqual(self.testList.getPosition(6), 5)

	def testRemoveBeginning(self):
		self.testList.removeBeginning()
		self.assertEqual(self.testList.getPosition(0), 3)
		self.assertEqual(self.testList.getPosition(1), 4)
		self.assertEqual(self.testList.getPosition(2), 9)
		self.assertEqual(self.testList.getPosition(3), 2)

	def testRemoveAfter(self):
		self.testList.removeAfter(1)
		self.testList.removeAfter(2)
		self.assertEqual(self.testList.getPosition(0), 1)
		self.assertEqual(self.testList.getPosition(1), 3)
		self.assertEqual(self.testList.getPosition(2), 9)

	def testFind(self):
		self.testList.find(1)
		self.testList.find(3)
		self.testList.find(4)
		self.testList.find(9)
		self.testList.find(2)

if __name__ == '__main__':
	unittest.main()
