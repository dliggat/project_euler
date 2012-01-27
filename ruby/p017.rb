#!/usr/bin/ruby

# A class to represent the English language expression of a number.
# 
class WordNumber
  attr_reader :number  # Gives getter access to @number.

  VALID_RANGE = (1..1000)

  WORD_DICT = {
    1  => 'one',
    2  => 'two',
    3  => 'three',
    4  => 'four',
    5  => 'five',
    6  => 'six',
    7  => 'seven',
    8  => 'eight',
    9  => 'nine',
    10 => 'ten',
    11 => 'eleven',
    12 => 'twelve',
    13 => 'thirteen',
    14 => 'fourteen',
    15 => 'fifteen',
    16 => 'sixteen',
    17 => 'seventeen',
    18 => 'eighteen',
    19 => 'nineteen',
    20 => 'twenty',
    30 => 'thirty',
    40 => 'forty',
    50 => 'fifty',
    60 => 'sixty',
    70 => 'seventy',
    80 => 'eighty',
    90 => 'ninety',  
  }

  def initialize(number)
    unless VALID_RANGE.include?(number)
      raise ArgumentError.new("Number must be within valid range") 
    end
    @number = number
  end

  # Returns the string representation. 
  #
  def to_s()
    result = nil
   
    if @number < 10
      result = WORD_DICT[@number]

    elsif number <= 99
      result = two_least_sig
 
    elsif number == 1000
      result = "one thousand"

    elsif number % 100 == 0
      result = hundreds_component

    elsif number <= 999
      result = "#{hundreds_component} and #{two_least_sig}"
    end

    return result
  end

  # Returns the size of the to_s string.
  # 
  def length()
    return to_s.size
  end


  private  # Methods following are private.

    # Return the representation of the two least significant digits.
    # e.g. for 426, this would return 'twenty-six'.
    # 
    def two_least_sig()
      tens_map = @number.to_s[-2,2].to_i  # Take the last 2 cols, and to_i.

      # If the word is in the dictionary (i.e. <= 20, or == 0 % 10), use that.
      if WORD_DICT.member?(tens_map)
        return WORD_DICT[tens_map]
      end

      # Otherwise, handle each column individually and join with a hyphen.
      tens_map = @number.to_s[-2,1].to_i * 10
      units_map = @number.to_s[-1,1].to_i      

      tens_str = "#{WORD_DICT[tens_map]}"
      units_str = "#{WORD_DICT[units_map]}"
      return "#{tens_str}-#{units_str}"
    end

    # Return the representation of the hundreds column.
    # e.g. for 426, this would return 'four hundred'. 
    #
    def hundreds_component()
      hunds_map = @number.to_s[-3,1].to_i
      hunds_str = "#{WORD_DICT[hunds_map]} hundred"
    end
end

# A class to represent the WordNumber constraints of Project Euler problem 17.
# 
class EulerWordNumber < WordNumber

  def initialize(number)
    super(number)
  end

  # Project Euler problem 17 defines the length of the word number as not 
  # including spaces or hyphens.  Remove and return the resulting length.
  # 
  def length()
    return to_s.gsub(" ", "").gsub("-", "").length
  end

end


if __FILE__ == $0

  sum = 0
  (1..1000).each do |val|
    a = EulerWordNumber.new(val)
    sum += a.length
    puts a
  end

  puts "The sum of letters is: #{sum}"
    
end
