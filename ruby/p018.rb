#!/usr/bin/ruby

=begin
Finds the longest path from top to bottom in a triangle. Solves Project Euler
problems 18 and 67.
=end

# Read the triangle file into an array of arrays.  Note that we run collect on
# each line in order to transform each string integer into an actual integer. 
#
def read_file(file = "inputs/bigtriangle.txt")
  tri = []
  # Read the file line by line.
  File.open(file, 'r') do |f1|
    while line = f1.gets

      # Represent each line as an array of integers.
      tri.push line.split(" ").collect {|i| i.to_i}
    end
  end

  return tri
end

# Finds the maximum valued path by traversing the triangle top to bottom.
#
def find_max(tri)

  max_list = []
  bottom_row = true

  # Iterate through the triangle backwards building the max_list for each line.
  tri.reverse.each do |line|

    # Treat the bottom row differently - it is already trivially the max_list.
    if bottom_row
      max_list = line
      bottom_row = false
      next  # Apparently equivalent to continue.
    end

    
    new_max = []
    # For each value, set its max value to be the sum of itself and the max of
    # its two descendants.
    for index in 0 ... line.size
      # Note Ruby max() syntax: place into an anonymous array.
      new_max.push [max_list[index], max_list[index+1]].max + line[index]
    end
    max_list = new_max
    puts max_list.inspect
    puts "....."

  end
  return max_list.first
end


if __FILE__ == $0
  tri = read_file
  result = find_max(tri)
  puts "The max list value is: #{result}"
end

