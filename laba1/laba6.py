n = int(input())
#calculate the time in hours, minutes, and seconds
h = n // 3600
m = n // 60 % 60
s = n % 60
#result
print(f"{h}:{m:02d}:{s:02d}")