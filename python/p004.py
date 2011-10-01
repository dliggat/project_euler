#!/usr/bin/python


def is_palindrome(num):
    """Returns True if num is a palindromic number, else False."""
    str_num = str(num)
    
    # Use the reversed generator to reverse the string-cast integer, then
    # use a join() to revert the list comprehension back into a string.
    if str_num == ''.join([char for char in reversed(str_num)]):
        return True
    else:
        return False


def main():
    """Find the largest palindromic number that is a product of two 3
    digit integers."""
    LOWER = 100
    UPPER = 999
    max = 1
    for i in range(LOWER, UPPER + 1):
        for j in range(LOWER, UPPER + 1):
            current = i * j
            if is_palindrome(current):
                if current > max:
                    max = current
    print 'Max:', max
            

if __name__ == '__main__':
    main()
