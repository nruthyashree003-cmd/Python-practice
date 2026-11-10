n = int(input("Enter number of intervals: "))

intervals = []

for i in range(n):
    start, end = map(int, input("Enter start and end: ").split())
    intervals.append([start, end])

# Sort intervals based on starting values
intervals.sort()

merged = []

for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

print("Merged intervals:", merged)