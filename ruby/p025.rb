#!/usr/bin/ruby


# A class to generate Fibonacci numbers.
# 
class FibGen

  # Start with the first two known Fibonacci numbers.
  #
  def initialize()
    @fibs = [1,1]
  end

  # Compute and yield the next number to the caller.
  def next_fib()
    while true
      @fibs << @fibs[-1] + @fibs[-2]  # Operator << is same as Array.push.
      yield @fibs[-1]
    end
  end

  def to_s()
    "#{@fibs.to_s}"  # Return statement unnecessary.
  end

  def largest()
    @fibs[-1]
  end

  def generated()
    @fibs.size
  end
end


if __FILE__ == $0

  fibgen = FibGen.new

  TARGET = 1000
  fibgen.next_fib do |fib|
    if fib.to_s.length >= TARGET
      break
    end  
  end

  puts "Fib #{fibgen.generated} = #{fibgen.largest} is the first " \
       "with #{TARGET} digits."


end

