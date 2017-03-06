import unittest
from tdd import solution

class TestSolution(unittest.TestCase):
  def test_addition(self):
    self.assertTrue(solution(10,20, "+"),30)
  def test_subtraction(self):
    self.assertTrue(solution(20,10, "-"),10)
  def test_assert_input_is_not_string(self):
  	self.assertRaises(TypeError,(solution('a','b','-')))
  	def test_multiplication(self):
  		self.assertTrue(solution(10,20,"*"),200)
  	def test_power(self):
  		self.assertTrue(solution(5,2,"**"),25)
  		if__name__=="__main__"
  		unittest.main()
