height = list(map(int, input("Enter bar heights: ").split()))

n = len(height)
total_water = 0

for i in range(n):

    left_max = max(height[:i+1])
    right_max = max(height[i:])

    water = min(left_max, right_max) - height[i]

    total_water += water

print("Trapped water:", total_water)