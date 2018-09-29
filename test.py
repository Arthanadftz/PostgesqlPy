import unittest as ut
import funct_mean

class meanTest(ut.TestCase):
	def test_mean(self):
		self.assertEqual(funct_mean.mean_val(df_mean, 'val'), 0.4714999999999999)

if __name__ == '__main__':
	unittest.main()