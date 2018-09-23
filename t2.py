import unittest
import connpy

class ConnpyTest(unittest.TestCase):
	def test_mean(self):
		self.assertEqual(connpy.mean_val(), 0.4714999999999999)

if __name__ == '__main__':
	unittest.main()
