#!/usr/bin/python

COLS = 20
ROWS = 20


def main():
    """Calculates the number of paths from the top left to the bottom
    right in a ROWS*COLS grid. It is only possible to move down or right."""
    
    # Start out with a list. Turn it into a list of lists.
    grid = []
    for _ in xrange(ROWS + 1):
        grid.append([])
    
    # Initialize each value in the grid to zero.  We view this structure as a
    # grid in the second quadrant: top left is grid[ROWS][COLS]; bottom right
    # is grid[0][0]. The value at each slot is the number of paths from there.
    # The final solution is the value at grid[ROWS][COLS].
    for row in xrange(ROWS + 1):
        for col in xrange(COLS + 1):
            grid[row].append(0)
    
    # There is only one path along the bottom boundary.
    for col in xrange(COLS + 1):
        grid[0][col] = 1
        
    # There is only one path along the right boundary.
    for row in xrange(ROWS + 1):
        grid[row][0] = 1
        
    # Iterate by column, then by row.
    for col in xrange(1, COLS + 1):
        for row in xrange(1, ROWS + 1):
            grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
    
    # Print the result.
    print 'In a %d*%d grid, there are %d paths.' % (ROWS, 
                                                    COLS, 
                                                    grid[ROWS][COLS])


if __name__ == '__main__':
    main()