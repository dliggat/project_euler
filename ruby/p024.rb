#!/usr/bin/ruby

$TARGET = 1000000

def main()
  
  counter = 0
  (0..9).to_a.permutation.each do |perm|
    counter += 1
    if counter == $TARGET
      puts "The #{$TARGET}th permutation is #{perm}."
      break
    end
  end
end


if __FILE__ == $0
  main()
end
