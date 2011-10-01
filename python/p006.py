#!/usr/bin/python


def main():
    """Compute the difference between the sum of the squares and the 
    square of the sums of the first 100 natural numbers."""
    
    MAX = 100
    sum_of_squares = sum([i*i for i in range(1, MAX + 1)])
    square_of_sums = sum([i for i in range(1, MAX + 1)])**2
    
    print "Result: ", square_of_sums - sum_of_squares
    
    

if __name__ == "__main__":
    main()