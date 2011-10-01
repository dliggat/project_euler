#!/usr/bin/python

from project_euler_lib import factoring


def main():
    """Find the sum of primes below 2 million."""
    pgen = factoring.PrimeGenerator()
    
    next = pgen.next_prime()
    sum = 0
    
    while next < 2000000:
        sum += next
        next = pgen.next_prime()
    
    print 'The sum of primes below 2000000 is: %d' % sum

    

if __name__ == "__main__":
    main()