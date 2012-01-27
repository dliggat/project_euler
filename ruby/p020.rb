#!/usr/bin/ruby

=begin
Finds the sum of digits of 100!.
=end

# Computes factorial function.
#
def factorial(n)
  base = 1
  n.downto(1) { |val| base *= val }
  return base
end

# Here we extend the Array class so that [...].sum works!
# Once this is added, it is possible to run this statement: [1,2,3].sum => 6. 
#
class Array
  def sum
    self.inject{|sum,x| sum + x }
  end
end


if __FILE__ == $0
  fact = factorial(100)

  # Convert the result to a string, split to an array of characters, then
  # collect into a new array of integers.
  digits = fact.to_s.each_char.collect {|c| c.to_i}

  sum = 0
  digits.each {|a| sum += a}
  puts "The result is: #{sum} via traditional loop."

  # Call the extended sum method on the Array class.
  puts "Otherwise, we can be really fancy and " \
       "extend Array to get #{digits.sum}."

end

