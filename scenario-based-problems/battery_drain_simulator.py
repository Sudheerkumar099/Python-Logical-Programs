battery_percent = 100
minutes = 0
drain_per_minute = int(input("Enter the battery percentage drain per minute: "))

while battery_percent>0:
    battery_percent = battery_percent - drain_per_minute
    minutes = minutes + 1
print(battery_percent)
print(minutes)