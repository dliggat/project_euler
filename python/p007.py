#!/usr/bin/python

from project_euler_lib import factoring


def main():
    """Find the 10001st prime."""
    pgen = factoring.PrimeGenerator()
    for _ in range(1, 10001 + 1):
        prime = pgen.next_prime()
    
    print '10001st prime: %d' % prime

    

if __name__ == "__main__":
    main()