x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter second point (x2 y2): ").split())

mx = (x1 + x2) / 2
my = (y1 + y2) / 2

print("Midpoint:", (mx, my))