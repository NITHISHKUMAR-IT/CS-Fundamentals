cpu_usage = [45, 72, 91, 38, 67, 88, 95]

print("CPU USAGE: ", cpu_usage)

highest = cpu_usage[0]
lowest = cpu_usage[0]

for use in cpu_usage:
    if use > highest:
        highest = use
    if use < lowest:
        lowest = use

print("The highest CPU usage is:", highest)
print("the lowest cpu usage is:", lowest)

count = 0

for values in cpu_usage:
    if values > 80:
        count += 1
        
print("The number of CPU usages above 80 is:", count)

cpu_usage.append(76)
print(cpu_usage)
