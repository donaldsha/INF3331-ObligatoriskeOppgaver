import inspect
import unittest 
from polynomials import Polynomial

class test_polynomials(unittest.TestCase):

	def setUp(self):
		self.p = Polynomial([2, 3, 1])
		self.q = Polynomial([0, 1, 2])

	def poly_ev(self):
		#evaluate a polynom
		corr_poly = dict({ 0: 2, 1: 6, 2: 12 })
		[self.assertEqual (self.q(i), j) for i, j in corr_poly.items()]
	
	def poly_add(self):
		#Add two polynoms
		add = Polynomial([2, 4, 3])
		res = self.p + self.q #Add 
		self.assertEqual(add, res)

	def poly_add(self):
		#Substitute two polynoms
		sub = Polynomial([-1, 2, -1])
		res = self.p - self.q #sub 
		self.assertEqual(sub, res)
 	
	def degree_exists(self):
		#verifying degree exist
		method = 'degree'#get a little hint from stack overflow
		self.asertTrue(hasattr(Polynomial, 'method') and callable(getattr(Polynomial, 'method')))
		#(if('method' in dir(Polynomial) and inspect.isfunction(Polynomial.method)))
		#check if it returns the degree of my poly
		self.assertEqual(self.p.degree(), 2)

	def repr_test(self):
		poly = 'x^2 + 3x + 2'
		self.assertEqual(repr(self.p), poly)#tests the method

	def mul_test():
		numb = 5
		poly = [0, 5, 10]
		mul = self.q * numb
		self.assertEqual(mul, Polynomial(poly))


if __name__ == '__main__':
    unittest.main()