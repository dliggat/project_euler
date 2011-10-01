#!/usr/bin/python

from project_euler_lib import factoring as f

def main():
	
	TOP_NUM = 10000
	pd_dict = {}
	
	# Build the dictionary mapping each value to its pd sum
	for num in xrange(2, TOP_NUM):
		num_f = f.IntFactor(num)
		pd_dict[num] = sum(num_f.proper_divisors)
		
		
	# Iterate over the dictionary and find amicable pairs.
	pairs = set()
	for val, image in pd_dict.iteritems():
	
		# We require that the two values are not equal, the pd_sum of val is in the dict and 
		# moreover, its pd_sum maps back to val.
		if val != image and image in pd_dict and pd_dict[image] == val:
		
			# We've found an amicable pair! Now create a sorted tuple which
			# represents the pair, and add to a set (to eliminate duplicates).
			pair = (min(val, image), max(val, image))
			pairs.add(pair)
	
	# Finally, iterate over the set, and generate the sum of all the values.
	amicable_sum = 0
	for p in pairs:
		amicable_sum += sum(p)
	
	print 'The amicable pair sum is %d.' % amicable_sum
			

if __name__ == '__main__':
	main()
	