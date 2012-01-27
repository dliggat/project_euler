#!/usr/bin/ruby


def main()
  int_val = 2 ** 1000
  str_val = int_val.to_s

  sum = 0
  str_val.split("").each do |v|  # This is how you iterate over each char.
    sum += v.to_i
  end
  puts "The sum is #{sum}."
end


if __FILE__ == $0
  main()
end
