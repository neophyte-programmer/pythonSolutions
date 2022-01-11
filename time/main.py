# Given seconds, calculate the hours, minutes and seconds

secs_string = input("Input seconds: ")  # do not change this line
secs_int = int(secs_string)
hours = secs_int // 3600
remainder = secs_int % 3600
minutes = remainder // 60
remainder = remainder % 60
seconds = remainder

print(hours, ":", minutes, ":", seconds) # do not change this line
