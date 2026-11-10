import math

n = int(input("Enter number of points: "))

points = []

for i in range(n):
    x, y = map(int, input("Enter x and y: ").split())
    points.append((x, y, i))


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def closest_pair(px, py):

    if len(px) <= 3:
        minimum = float('inf')

        for i in range(len(px)):
            for j in range(i + 1, len(px)):
                minimum = min(minimum, distance(px[i], px[j]))

        return minimum

    mid = len(px) // 2
    mid_x = px[mid][0]

    left_x = px[:mid]
    right_x = px[mid:]

    left_ids = set(p[2] for p in left_x)

    left_y = [p for p in py if p[2] in left_ids]
    right_y = [p for p in py if p[2] not in left_ids]

    d1 = closest_pair(left_x, left_y)
    d2 = closest_pair(right_x, right_y)

    minimum = min(d1, d2)

    strip = [p for p in py if (p[0] - mid_x) ** 2 < minimum]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            minimum = min(minimum, distance(strip[i], strip[j]))

    return minimum


px = sorted(points, key=lambda p: p[0])
py = sorted(points, key=lambda p: p[1])

result = closest_pair(px, py)

print("Minimum Distance:", math.sqrt(result))