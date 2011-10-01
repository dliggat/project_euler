#!/usr/bin/python

import logging as log
import optparse
import traceback

# Logging levels to parse from the command line.
LOGGING_LEVELS = {'critical': log.CRITICAL,
                  'error': log.ERROR,
                  'warning': log.WARNING,
                  'info': log.INFO,
                  'debug': log.DEBUG}


def parse_file(file_path='/Users/daveliggat/Dropbox/Project_Euler/inputs/p011_input.txt'):
    """Parses the input file.
    
    Args:
        file_path: (str) path to the input list.
    Returns:
        (list) of lists, which represents the parsed grid.
    """
    try:
        f = open(file_path, 'r')
        try:
            lines = f.readlines()
        finally:
            f.close()
    except IOError:
        log.error('Problem opening input file: %s', traceback.format_exc())
        raise

    # Transform the read file into a list of lists.
    nums = []
    for line in lines:
        num_list = [int(_) for _ in line.split(' ') if len(line) > 1]
        if num_list:
            nums.append(num_list)
  
    return nums


def do_walk(nums):
    """Takes the matrix, walks over it, and finds the largest product.
    
    Args:
        nums: (list) of lists of numbers which represents the problem matrix.
    Returns:
        (int) the single result which represents the max product sequence.
    """
    # Error checking.
    ROWS = len(nums)
    COLS = len(nums[0])
    for row in nums:
        assert len(row) == COLS, 'Mismatch between row and col length!'

    SEQ_LEN = 4
    list_product = lambda x,y: x*y  # Anonymous function used with list reduce().
    
    # Best is a storage location for the best result found so far. Start off 
    # with the top left corner and horizontal sublist.
    best = reduce(list_product, [nums[0][i] for i in xrange(0, SEQ_LEN)])

    for row in xrange(0, ROWS):
        for col in xrange(0, COLS):
            # This gives us all the valid starting positions. Now find the 4 values.
            log.debug('Starting matrix[%d][%d]', row, col)

            # From a single position, build a dictionary of the possible lists
            # that may result from that position.  There are four directions:
            # up, down, negative (slope) diagonal, and positive diagonal.
            lists = {'h': None, 'v': None, 'd_neg': None, 'd_pos': None}

            # Check for valid horizontal.
            if col <= COLS - SEQ_LEN:      
                lists['h'] = nums[row][col:col+SEQ_LEN]
                log.debug('Horizontal candidate: %s', str(lists['h']))
            
            # Check for valid vertical.
            if row <= ROWS - SEQ_LEN:
                lists['v'] = [nums[row + i][col] for i in xrange(0, SEQ_LEN)]
                log.debug('Vertical candidate: %s', str(lists['v']))

            # Check for valid diagonal negative.
            if col <= COLS - SEQ_LEN and row <= ROWS - SEQ_LEN:
                lists['d_neg'] = [nums[row+i][col+i] for i in xrange(0, SEQ_LEN)]
                log.debug('Diagonal neg candidate: %s', str(lists['d_neg']))
            
            # Check for valid diagonal positive.
            if row >= SEQ_LEN - 1 and col <= COLS - SEQ_LEN:
                lists['d_pos'] = [nums[row-i][col+i] for i in xrange(0, SEQ_LEN)]
                log.debug('Diagonal pos candidate: %s', str(lists['d_pos']))

            # Iterate over the lists that have been generated.
            for key, li in lists.iteritems():
            
                # The list needs to exist; for some positions, some keys won't
                # have lists.
                if li:
                    # Reduce the list to a single product.  
                    product = reduce(list_product, li)
                    log.debug('%s product: %d', key, product)
                    
                    # If we have found a product that is better than the current
                    # best, log the location and update the 'best' variable.
                    if product > best:
                        log.info('New best found: %d. List: %s', product, str(li))
                        log.info('%s list based at matrix[%d][%d]', key, row, col)
                        best = product

    # The solution is the resulting value in best.
    return best
            

def main():
    """Sets up a opt-parser to configure logging options, then starts.
    """
    parser = optparse.OptionParser()
    parser.add_option('-l', '--logging-level', help='Logging level')
    (options, args) = parser.parse_args()
    
    # Get the logging level from the dictionary defined above, or NOTSET
    # if the value given is not present.
    logging_level = LOGGING_LEVELS.get(options.logging_level, log.NOTSET)
    log.basicConfig(level=logging_level,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Run the actual program.
    log.info('Starting the program...')
    nums = parse_file()
    best = do_walk(nums)
    print 'The best result found was: %d' % best
    log.info('Program complete.')


if __name__ == '__main__':
    main()    
