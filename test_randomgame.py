import unittest
import randomgame
import numbers

class TestMain(unittest.TestCase):
	def setUp(self):
		print('testing in progress')

	def test_run_guess_good_input(self):
		start, end = 1,10
		for i in range(1,11):
			self.assertTrue(randomgame.run_guess(start,end, i, i))

	def test_run_guess_wrong_input(self):
		start, end = 1,10
		self.assertFalse(randomgame.run_guess(start,end, 5, 3))

	def test_run_guess_bad_input(self):
		self.assertFalse(randomgame.run_guess(1,10, 'a', 3))


	def tearDown(self):
		print('this test is now over')

if __name__ == '__main__':
	unittest.main()