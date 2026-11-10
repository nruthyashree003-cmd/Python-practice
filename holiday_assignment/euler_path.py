def find_euler_path(n, edges):

    graph = [[] for i in range(n)]
    degree = [0] * n

    # Step 1: Build graph and calculate degrees
    for edge_id, (u, v) in enumerate(edges):

        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))

        degree[u] += 1
        degree[v] += 1

    # Step 2: Find odd-degree nodes
    odd_nodes = []

    for i in range(n):
        if degree[i] % 2 != 0:
            odd_nodes.append(i)

    # Step 3: Check connectivity
    start = 0

    for i in range(n):
        if degree[i] > 0:
            start = i
            break

    visited = [False] * n
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()

        for neighbor, edge_id in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    connected = True

    for i in range(n):
        if degree[i] > 0 and not visited[i]:
            connected = False

    # Step 4: Check Euler Path conditions
    if not connected or len(odd_nodes) not in [0, 2]:
        print("Euler Path Exists: False")
        print("Node Degrees:", degree)
        print("Odd Degree Nodes:", odd_nodes)
        return

    # Step 5: Select starting node
    if len(odd_nodes) == 2:
        start = odd_nodes[0]
    else:
        for i in range(n):
            if degree[i] > 0:
                start = i
                break

    # Step 6: Find Euler Path
    used = [False] * len(edges)

    stack = [start]
    path = []

    while stack:

        node = stack[-1]

        found = False

        while graph[node]:

            neighbor, edge_id = graph[node].pop()

            if not used[edge_id]:

                used[edge_id] = True
                stack.append(neighbor)
                found = True
                break

        if not found:
            path.append(stack.pop())

    path.reverse()

    # Step 7: Print result
    print("Euler Path Exists: True")

    print("\nNode Degrees:")

    for i in range(n):
        print(i, "->", degree[i])

    print("\nOdd Degree Nodes:", odd_nodes)
    print("Start Node:", start)
    print("Euler Path:", " -> ".join(map(str, path)))


# Take input
n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter the edges:")
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])

find_euler_path(n, edges)