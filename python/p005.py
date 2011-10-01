#!/usr/bin/python


def test_divisors(num):
    """Returns True if num is divisible by all numbers from 1..20 inclusive, 
    else returns False."""
    
    # Don't need to include lower divisors because divisibility by these implies
    # divisibility by the lower numbers.
    # e.g. divisibility by 14 implies divisibility by 7.
    divisors = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    
    for divisor in divisors:
        if num % divisor != 0:
            return False
    
    # If we make it through the list, return True.
    return True
    

def main():
    """Returns the smallest integer divisible by all of 1...20 inclusive."""
    num = 40
    while not test_divisors(num):
        num = num + 1
    
    print 'Num:', num


if __name__ == '__main__':
    main()