#!/usr/bin/python

import traceback

# A mapping of letters to the score for that letter.
score_map = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}


def read_in_sorted_order(path='/Users/daveliggat/Dropbox/Project_Euler'
                              '/inputs/p022_input.txt'):
    """Reads the input file and sorts. Returns the list."""
    
    # Do the file read operation in the standard way.
    try:
        f = open(path, 'r')
        try:
            text = f.read()
        finally:
            f.close()
    except IOError, e:
        traceback.print_exc()
        raise
    
    # Split on the comma, and remove the double-quotes. Sort on return.
    names = text.split(',')
    return sorted([name.replace('"', '') for name in names])


def name_score(name):
    """Given a name score, compute its score value.
    
    Args:
        name (str): Name to be scored.
    
    Returns:
        (int) A score based on the scoring function."""
    score = 0
    for letter in name:
        score += score_map[letter.lower()]
    
    return score
        

def main():
    names = read_in_sorted_order()
    
    # Iterate over the enumeration of the names, and on each loop, add the
    # product of the name_score and the list position. Note the +1 to the latter
    # as enumerate has zero-based indexes (scoring is 1-based).
    total_score = 0
    for score, name in enumerate(names):
        total_score += name_score(name) * (score + 1)
    
    print 'The total score of the names in the file is: %d' % total_score
    

if __name__ == '__main__':
    main()