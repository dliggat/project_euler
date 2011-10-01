#!/usr/bin/python

def fib(N=4000000):
    """Return the list of Fibonaccis <= N."""
    li = [1,1]
    while True:
        new = li[-1] + li[-2]
        if new > N:
            break
        else:
            li.append(new) 
    return li
    
    
def make_tri_generator():
    """Returns a generator object which produces triangle numbers.
    
    A triangle number results from adding the natural numbers.  The sequence
    is {1,3,6,10,15,21,28,..}. e.g. the 7th triangle number, 28 = 1+2+3+4+5+6+7.
    Note that we call next() on the return of this function to get these."""
    current_tri = 1
    next_to_add = 2
    yield current_tri
    while True:
        current_tri += next_to_add
        next_to_add += 1
        yield current_tri