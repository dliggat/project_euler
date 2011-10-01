#!/usr/bin/python


def collatz(value):
    """Returns the Collatz function value of value."""
    assert value >= 1
    if value % 2 == 0:
        return value/2
    else:
        return 3 * value + 1

        
collatz_len_dict = {}        
def collatz_length(val):
    """Returns the collatz length associated with val, building
    the collatz_len_dict as it goes."""
    assert val >= 1
    
    # Seed the dictionary with collatz_length(1) = 1.
    if val == 1:
        collatz_len_dict[1] = 1
        return collatz_len_dict[1]
    
    # Return the collatz length if it exists in the dictionary.
    if val in collatz_len_dict:
        return collatz_len_dict[val]
    
    # Make a recursive call to collatz_length() using mapped_val to find this
    # val's length.
    mapped_val = collatz(val)
    collatz_len_dict[val] = 1 + collatz_length(mapped_val)
    return collatz_len_dict[val]


def main():
    """Finds the number with the longest Collatz sequence under 1 million."""
    
    TOP_VAL = 1000000
    for i in xrange(1, TOP_VAL):
        _ = collatz_length(i)  # Seed each collatz length.
    
    # Find the key with largest value in the collatz length dictionary.
    value, collatz_len = max(collatz_len_dict.iteritems(),
                             key=lambda x:x[1])
    
    print 'Value %d has max collatz length: %d' % (value, collatz_len)


if __name__ == '__main__':
    main()