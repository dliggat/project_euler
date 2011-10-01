#!/usr/bin/python

def main():
    """Find the sum of all multiples of 3 or 5 below 1000."""
    LIM = 1000
    sum = 0
    for i in range(LIM):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    
    print 'Sum:', sum


if __name__ == "__main__":
    main()