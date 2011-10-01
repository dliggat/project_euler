#!/usr/bin/python


class WordNumber(object):
    """A class to generate the english representation of a number."""
    
    LOWER = 1
    UPPER = 1000
    
    def __init__(self, num):
        assert (num >= self.__class__.LOWER 
            and num <= self.__class__.UPPER), 'Parameter exceeded bounds!'
        self.num = num


def main():
    a = WordNumber(4)


if __name__ == '__main__':
    main()