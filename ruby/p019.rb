#!/usr/bin/ruby


def main()
  start = Time.utc(1901,1,1)
  target = Time.utc(2000,12,31)

  date = start
  first_sunday_count = 0
  while date < target
    
    if date.wday == 0 and date.day == 1
      first_sunday_count += 1
    end

    date += 60*60*24
  end
  puts "There are #{first_sunday_count} Sundays on the 1st of the month " \
       "between #{start} and #{target}"

end


if __FILE__ == $0
  main()
end
