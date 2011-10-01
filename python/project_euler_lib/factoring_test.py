#!/usr/bin/python

import unittest
import factoring as f


class TestPrimeGenerator(unittest.TestCase):
    
    def setUp(self):
        self.pgen = f.PrimeGenerator()
        
    def testFirstTwoPrimes(self):
        """Ensure the start of the list of primes is correct."""
        li = [self.pgen.next_prime() for _ in xrange(0, 2)]
        self.assertEqual(li, [2,3])
        
    def testFirstTenPrimes(self):
        """Ensure the start of the list of primes is correct."""            
        li = [self.pgen.next_prime() for _ in xrange(0, 10)]
        self.assertEqual(li, [2,3,5,7,11,13,17,19,23,29])
    

class TestIntFactor(unittest.TestCase):

    def testInit(self):
        """The factored variable should not be set on construction."""
        num = f.IntFactor(5)
        self.assertFalse(num.factored)
        
    def testSetFactoredVar(self):
        """The factored variable should be set once the dict is accessed."""
        num = f.IntFactor(5)
        _ = num.pfactor_dict
        self.assertTrue(num.factored)

    def testAssertIfInvalidInput(self):
        """Raise on erroneous input."""
        self.failUnlessRaises(AssertionError, f.IntFactor, 3.0)
        self.failUnlessRaises(AssertionError, f.IntFactor, 1)
        self.failUnlessRaises(AssertionError, f.IntFactor, -5)
           
    def testPrimeInput(self):
        """Test cases where the input is itself prime."""
        d = {2: 1}
        num = f.IntFactor(2)
        self.assertEqual(num.pfactor_dict, d)
        self.assertTrue(num.is_prime)
        
        d = {19: 1}
        num = f.IntFactor(19)
        self.assertEqual(num.pfactor_dict, d)
        self.assertTrue(num.is_prime)

        d = {6628403: 1}
        self.assertEqual(f.IntFactor(6628403).pfactor_dict, d)    
        self.assertTrue(num.is_prime)        
      
    def testSmallComposite(self):
        """Test trivial instances of composite numbers."""
        d = {2: 1, 3: 1}
        num = f.IntFactor(6)
        self.assertEqual(num.pfactor_dict, d)
        self.assertFalse(num.is_prime)

        d = {5: 1, 7: 1, 11: 1, 13: 1}
        num = f.IntFactor(5005)
        self.assertEqual(num.pfactor_dict, d)
        self.assertFalse(num.is_prime)
        
    def testLargeComposites(self):
        """Test large instances of composite numbers."""
        d = {71: 1, 839: 1, 1471: 1, 6857: 1}  # The actual problem 3 number.
        num = f.IntFactor(600851475143)
        self.assertEqual(num.pfactor_dict, d)
        self.assertFalse(num.is_prime)
        
        d = {2: 3, 3: 1, 226189: 1}
        num = f.IntFactor(5428536)
        self.assertEqual(num.pfactor_dict, d)
        self.assertFalse(num.is_prime)
    
    def testDivisors(self):
        """Test that divisors are represented correctly."""
        num = f.IntFactor(19)
        divisors = [1,19]
        proper_divisors = [1,]
        self.assertEqual(divisors, num.divisors)
        self.assertEqual(proper_divisors, num.proper_divisors)
        
        num = f.IntFactor(28)
        divisors = [1,2,4,7,14,28]
        proper_divisors = [1,2,4,7,14]
        self.assertEqual(divisors, num.divisors)
        self.assertEqual(proper_divisors, num.proper_divisors)
        
        num = f.IntFactor(5005)
        divisors = [1,5,7,11,13,35,55,65,77,91,143,385,455,715,1001,5005]
        proper_divisors = [1,5,7,11,13,35,55,65,77,91,143,385,455,715,1001]
        self.assertEqual(divisors, num.divisors)
        self.assertEqual(proper_divisors, num.proper_divisors)
    
    def testStringRepresentation(self):
        """Test the string representation."""
        rep = '600851475143 = (71)(839)(1471)(6857)'
        self.assertEqual(str(f.IntFactor(600851475143)), rep)
        
        rep = '12 = (2^2)(3)'
        self.assertEqual(str(f.IntFactor(12)), rep)
     
     
if __name__ == '__main__':
    unittest.main()