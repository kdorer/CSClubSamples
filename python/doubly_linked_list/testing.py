import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):


	def setUp(self):
		self.emptyList = DoublyLinkedList()
		self.oneItemList = DoublyLinkedList()
		self.twoItemList = DoublyLinkedList()
		self.fiveItemList = DoublyLinkedList()

		self.one = [3]
		self.two = [2, 9]
		self.five = [6, 1, 0, 5, 8]

		for i in self.one:
			self.oneItemList.append(i)

		for i in self.two:
			self.twoItemList.append(i)

		for i in self.five:
			self.fiveItemList.append(i)


	def testEmptyAppend(self):
		self.emptyList.append(4)
		self.assertEqual(self.emptyList.getPosition(0), 4)

	def testOneAppend(self):
		self.oneItemList.append(1)
		self.assertEqual(self.oneItemList.getPosition(0), 3)
		self.assertEqual(self.oneItemList.getPosition(1), 1)

	def testTwoAppend(self):
		self.twoItemList.append(6)
		self.assertEqual(self.twoItemList.getPosition(0), 2)
		self.assertEqual(self.twoItemList.getPosition(1), 9)
		self.assertEqual(self.twoItemList.getPosition(2), 6)

	def testEmptyPrepend(self):
		self.emptyList.prepend(4)
		self.assertEqual(self.emptyList.getPosition(0), 4)

	def testOnePrepend(self):
		self.oneItemList.prepend(1)
		self.assertEqual(self.oneItemList.getPosition(0), 1)

	def testTwoPrepend(self):
		self.twoItemList.prepend(6)
		self.assertEqual(self.twoItemList.getPosition(0), 6)
		self.assertEqual(self.twoItemList.getPosition(1), 2)
		self.assertEqual(self.twoItemList.getPosition(2), 9)

	def testEmptyInsertAfter(self):
		self.assertFalse(self.emptyList.insertAfter(1, 3))

	def testOneInsertAfter(self):
		self.assertTrue(self.oneItemList.insertAfter(2, 0))
		self.assertEqual(self.oneItemList.getPosition(1), 2)
		self.assertFalse(self.oneItemList.find(7))

	def testTwoInsertAfter(self):
		self.assertTrue(self.twoItemList.insertAfter(7, 0))
		self.assertEqual(self.twoItemList.getPosition(1), 7)
		self.assertFalse(self.twoItemList.find(3))

	def testEmptyRemoveBeginning(self):
		self.assertFalse(self.emptyList.removeBeginning())

	def testOneRemoveBeginning(self):
		self.assertTrue(self.oneItemList.removeBeginning())
		self.assertFalse(self.oneItemList.getPosition(0))

	def testTwoRemoveBeginning(self):
		self.assertTrue(self.twoItemList.removeBeginning())
		self.assertEqual(self.twoItemList.getPosition(0), 9)

	def testEmptyRemoveEnd(self):
		self.assertFalse(self.emptyList.removeEnd())

	def testOneRemoveEnd(self):
		self.assertTrue(self.oneItemList.removeEnd())
		self.assertFalse(self.oneItemList.getPosition(0))

	def testTwoRemoveEnd(self):
		self.assertTrue(self.twoItemList.removeEnd())
		self.assertEqual(self.twoItemList.getPosition(0), 2)

	#def testRemoveAfter(self):

	def testEmptyFind(self):
		self.assertFalse(self.emptyList.find(0))

	def testOneFind(self):
		self.assertFalse(self.oneItemList.find(0))
		self.assertTrue(self.oneItemList.find(3))

	def testTwoFind(self):
		self.assertTrue(self.fiveItemList.find(8))
		self.assertFalse(self.fiveItemList.find(3))

	def testFiveFind(self):
		self.assertTrue(self.fiveItemList.find(0))
		self.assertFalse(self.fiveItemList.find(2))

if __name__ == '__main__':
	unittest.main()
