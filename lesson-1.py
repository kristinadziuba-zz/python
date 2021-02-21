
time = int(input('Duration: '))
second = time % 60
print('duration in seconds = ', second, "sec")

time = int(input('Duration: '))
second = time % 60
minutes = (time % 3600) // 60
print("duration in minutes and seconds = ", minutes, "min", second, "sec")

time = int(input('Duration: '))
second = time % 60
hour = (time // 3600) % 24
minutes = (time % 3600) // 60
print('duration in hours, minutes and seconds = ', hour, "h", minutes, "min", second, "sec")

time = int(input('Duration: '))
second = time % 60
hour = (time // 3600) % 24
minutes = (time % 3600) // 60
day = (time // 3600) // 24
print('duration in days, hours, minutes and seconds = ', day, "days", hour, "h", minutes, "min", second, "sec")


