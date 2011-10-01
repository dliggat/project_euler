#!/usr/bin/python

from project_euler_lib import discrete as d
from project_euler_lib import factoring as f



def main():
    """Calculates what is the value of the first triangle number to have over
    500 divisors.
    """
    tri_gen = d.make_tri_generator()
    DIVISOR_COUNT = 500
    
    # This is a NOP to skip over the first triangular number (1) as IntFactor
    # will complain about this as an input (neither prime nor composite).
    _ = next(tri_gen)
    
    while True:
        test_value = next(tri_gen)
        
        factor = f.IntFactor(test_value)
        if len(factor.divisors) > DIVISOR_COUNT:
            print '%d is triangular and has > %d factors.' % (test_value, 
                                                              DIVISOR_COUNT)
            break
        
    print 'Done.'
    

if __name__ == "__main__":
    main()