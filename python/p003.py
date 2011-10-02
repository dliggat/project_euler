#!/usr/bin/python

import logging

from project_euler_lib import factoring


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    a = factoring.IntFactor(600851475143)
    print a
    print 'The largest factor is: %d' % max(a.pfactor_dict.keys())


if __name__ == '__main__':
    main()
