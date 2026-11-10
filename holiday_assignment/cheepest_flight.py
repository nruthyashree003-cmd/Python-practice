n = int(input("Enter number of cities: "))

m = int(input("Enter number of flights: "))
flights = []

for i in range(m):
    u, v, price = map(int, input().split())
    flights.append([u, v, price])

src = int(input("Enter source city: "))
dst = int(input("Enter destination city: "))
k = int(input("Enter maximum stops: "))

cost = [float('inf')] * n
cost[src] = 0

for i in range(k + 1):
    temp = cost.copy()

    for u, v, price in flights:
        if cost[u] != float('inf'):
            temp[v] = min(temp[v], cost[u] + price)

    cost = temp

if cost[dst] == float('inf'):
    print(-1)
else:
    print(cost[dst])