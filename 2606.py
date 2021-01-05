import sys
input = sys.stdin.readline


def dfs(vertex, visited=[]):
    if vertex not in visited:
        visited.append(vertex)
        for i in range(n+1):
            if graph[vertex][i] and i not in visited:
                dfs(i, visited)
    return visited


n = int(input().strip())
connect = int(input().strip())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(connect):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

print(len(dfs(1)) - 1)


