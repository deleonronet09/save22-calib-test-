import calculator
import unittest

class TestCalculator(unittest.TestCase):
  def test_Add(self):
    self.assertEqual(calculator.add(1,1),2)
  def test_Subtract(self):
  	self.assertEqual(calculator.subtract(15,10),5)
  def test_Multiply(self):
  	self.assertEqual(calculator.multiply(1,1),1)
  def test_Divide(self):
  	with self.assertRaises(ZeroDivisionError):
  		self.assertEqual(calculator.divide(10,0))
  def test_None(self):
  	self.assertEqual(calculator.operator(1,'A',1),None)

  def test_operator(self):
  	self.assertEqual(calculator.add(13,11),24)
  	self.assertEqual(calculator.subtract(15,-10),25)
  	self.assertEqual(calculator.divide(16,2),8)
  	self.assertEqual(calculator.multiply(7,-3),-21)

  def test_Output(self):
  	self.assertEqual(calculator.output(10,'/',10,1),'10 / 10 = 1')

if __name__ == "__main__":
   unittest.main()