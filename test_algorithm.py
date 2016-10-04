import unittest
from algorithm import concat

class ConcatTest(unittest.TestCase):
	def test_Concat(self):
		self.assertEqual(concat(['a','b','c'], 0, 2), 'abc')

	def test_ConcatSublist(self):
		self.assertEqual(concat(['a','b','c', 'a'], 1, 2), 'bc')

	def test_ConcatStartIndexGreaterThanEndIndex(self):
		self.assertEqual(concat(['a','b','c'], 1, 0), '')

	def test_ConcatOutOfBoundIndex(self):
		self.assertEqual(concat(['a','b','c'], -1, 3), '')

	def test_ConcatNoneArray(self):
		self.assertEqual(concat(None, 0, 2), '')

	def test_ConcatEmptyArray(self):
		self.assertEqual(concat([], 0, 2), '')

	
if __name__ == '__main__':
	unittest.main()



