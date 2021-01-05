import sys
input = sys.stdin.readline


def dfs(vertex, visited=[]):
    if vertex not in visited:
        visited.append(vertex)
        for i in range(n+1):
            if graph[vertex][i] and i not in visited:
                dfs(i, visited)
    return visited


def bfs(vertex, visited=[]):
    queue = [vertex]
    visited = [vertex]
    while queue:
        v = queue.pop(0)
        for i in range(n+1):
            if graph[v][i] and i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


n, m, v = map(int, input().split())
graph = dict()

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for item in dfs(v):
    print(item, end=' ')

print()

for item in bfs(v):
    print(item, end=' ')

