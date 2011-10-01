#!/usr/bin/python


def main():
    """Find the Pythagorean triplet, a + b + c = 1000."""
    LIMIT = 600
    GOAL = 1000
    for i in range(1, LIMIT + 1):
        for j in range(1, LIMIT + 1):
            for k in range(1, LIMIT + 1):
                if i + j + k == GOAL:
                    if i**2 == j**2 + k**2:
                        print "GOAL:", (i, j, k)
    

if __name__ == "__main__":
    main()