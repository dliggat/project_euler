#!/usr/bin/python

import itertools
import logging
import math
import operator
import re


class PrimeGenerator(object):
    """A class to generate primes.  Starting with the largest known prime, add
    two to that prime and test divisibility with every other prime in the
    list.  If we make it to the end, we know that this is itself a prime.
    
    This class generates primes from the first for client classes which need a 
    stream of prime numbers, but maintains its own class-level list of primes
    as new ones are discovered."""
    
    known_primes = [2,3]  # This is a class level attribute.
    
    def __init__(self):
        # The counter for the position in the list that we are returning to the
        # clients of this class.
        self.counter = 0
    
    @classmethod
    def _generate_next(cls):
        """Generates the next prime and adds to the known prime list."""
        # Start with the largest known prime.
        candidate = cls.known_primes[-1]
        
        # Loop until one is found.
        while True:
            is_candidate = True
            candidate += 2  # Inc by 2 each time; no prime is even so skip them.
            for prime in cls.known_primes:
                if candidate % prime == 0:
                    is_candidate = False
                    break
                
                # IMPORTANT: Compare the current prime to sqrt(candidate).
                # Rationale: If we're wondering if 17 is prime, by the time 
                # we've passed sqrt(17) with no divisors, we don't need to check
                # anything else. Why? - sqrt(17) = 4.1ish; after checking [2,3],
                # and then encountering 5, we can be confident that 17 is prime 
                # without bothering to check [5,7,11,13], because 5*5 = 25 > 17.
                if math.floor(math.sqrt(candidate)) < prime:
                    break
            
            # Add two to this candidate and try again.
            if not is_candidate:
                continue
                
            # If we've made it this far, we must have a prime.
            logging.debug('Adding prime #%d to known prime list: %d', 
                          len(cls.known_primes) + 1, candidate)
            cls.known_primes.append(candidate)
            return
        
    def next_prime(self):
        """Return the next prime in the list to the client, invoking the 
        generation ability if necessary
        
        Returns:
            (int) The next integer in sequence."""
        if self.counter == len(self.__class__.known_primes):
            self._generate_next()
        ret_val = self.__class__.known_primes[self.counter]
        self.counter += 1
        return ret_val


class IntFactor(object):
    """This class represents an integer's unique prime factorization."""
    
    def __init__(self, num):
        """Initialize the object.
        
        Args:
            num: (int) The integer to factor."""
        assert isinstance(num, int), 'Must be an integer input!'    
        assert num >= 2, 'Integer must be greater than 1!'
        
        self.num = num
        self._pfactor_dict = {}
        self.factored = False
        
        # The largest value we need to check as a factor.
        self.square_root = int(math.floor(math.sqrt(self.num)))
        
    def __add_to_dict(self, factor):
        """Add the given factor to the dictionary, with logging.
        
        Args:
            factor: (int) The prime factor to add."""
        logging.info('Determined factor of %d: %d', self.num, factor)
        self.pfactor_dict[factor] = self.pfactor_dict.get(factor, 0) + 1
          
    def _pfactorization(self):
        """Computes the unique factorization of the integer.
        
        Returns:
            (dict) The mapping of primes to count in the factorization."""
        pgen = PrimeGenerator()
        self.factored = True
        divisor = pgen.next_prime()
        dividend = self.num
        done = False
        
        while not done:
            # We found a prime divisor.  Add to the dictionary, and continue
            # looping based on divisor.  Create a new PrimeDivisor as we need
            # to start again from 2.
            if dividend % divisor == 0:
                self.__add_to_dict(divisor)
                dividend = dividend / divisor
                pgen = PrimeGenerator()
            
            # TODO(dave): Look into this in future.  Is this even needed?
            elif divisor > self.square_root:
                if dividend > 1:
                    self.__add_to_dict(dividend)
                done = True
            
            # Fun fact: the lack of this line was the source of the fact that
            # my Project Euler code did not terminate quickly.
            elif dividend == 1:
                done = True
            
            # Try the next prime up in the list.
            else:
                divisor = pgen.next_prime()  
        
        return self.pfactor_dict
    
    @property
    def divisors(self):
        """Returns the list of divisors for the underlying integer.
        
        For example: 28 has divisor list [1,2,4,7,14,28]."""      
        # Add the identity and self to the divisor set.
        divs = set()
        divs.add(1)
        divs.add(self.num)
        
        # Expand the factor dictionary to a list, where repeated factors
        # are repeated the appropriate number of times.
        expanded = []
        for prime, count in self.pfactor_dict.iteritems():
            expanded.extend([prime]*count)
            
        # Generate all subsets of the expanded list.
        for subset_size in xrange(1, len(expanded)):
            for subset in itertools.combinations(expanded, subset_size):
            
                # Add the product of the subset to the set, as well as the
                # result of num/product.
                set_divisor = reduce(operator.mul, subset)
                divs.add(set_divisor)
                divs.add(self.num/set_divisor)
        
        return sorted(list(divs))
        
    @property
    def proper_divisors(self):
        """Returns the set of proper divisors; all divisors except self."""
        
        # Returns a slice from the beginning to the last element. Since the last
        # operand is exclusive, the largest divisor, self, will be excluded.
        # Note: this works <=> the divisors property returns a sorted list.
        return self.divisors[:-1] 


    
    @property
    def is_prime(self):
        """Returns True if num is prime, else False."""
        # Only one factor in the dictionary, and that factor exists only once.
        return (len(self.pfactor_dict) == 1 and 
                self.pfactor_dict.values()[0] == 1)
                
    @property
    def pfactor_dict(self):
        """Returns the prime factor dictionary, lazily initializing if needed.
        
        Returns:
            (dict): mapping of prime factors to their count."""
        if not self.factored:
            self._pfactorization()
        return self._pfactor_dict
        
    def __str__(self):
        """Return the string representation."""
        # Put together a product of parentheses.    
        decom = ''.join(['(%d^%d)' % (k,v) for k,v in 
                                           sorted(self.pfactor_dict.items())])
                                           
        # Use a basic regex to strip out the instances of '^1)' and replace with
        # ')' as the unitary exponents are not necessary.
        decom = re.sub('\^1\)', ')', decom)     
        return '%d = %s' % (self.num, decom)