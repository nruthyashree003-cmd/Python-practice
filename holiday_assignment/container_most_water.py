height = list(map(int, input("Enter heights: ").split()))

left = 0
right = len(height) - 1

max_area = 0

while left < right:

    width = right - left

    water_height = min(height[left], height[right])

    area = width * water_height

    max_area = max(max_area, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print("Maximum water area:", max_area)