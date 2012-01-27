#!/usr/bin/ruby

$TARGET = 1000000

def compute_cycle_len(d)
  d + 1
end


def main()

  cycle_len = 0
  best = nil  
  (1..1000).each do |d|
    result = compute_cycle_len(d)
    if result > cycle_len
      cycle_len = result
      best = d
    end 
  end

  puts "Value of d=#{best} has cycle length #{cycle_len}."
end


if __FILE__ == $0
  main()
end
