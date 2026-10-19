# 1
graph = [
    [0, 4, 0, 0, 7, 0, 0],
    [4, 0, 1, 8, 8, 0, 0],
    [0, 1, 0, 0, 0, 3, 0],
    [0, 8, 0, 0, 13, 16, 0],
    [7, 8, 0, 13, 0, 0, 0],
    [0, 0, 3, 16, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
]

# 2
count_v = 0
for i in graph:
    count_v += 1
print(f"2) вершин: {count_v}")

# 3
count_3 = 0
for i in graph:
    deg = 0
    for j in i:
        if j > 0:
            deg += 1
    if deg == 3:
        count_3 += 1
print(f"3) степень 3 у: {count_3} вершин")

# 4
count = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] > 0:
            count += 1
edges = count // 2
print(f"4) ребер: {edges}")

# 5
s = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        s += graph[i][j]
total_s = s // 2
print(f"5) сумма: {total_s}")

# 6
neighbors = 0
for i in graph[5]:
    if i > 0:
        neighbors += 1
print(f"6) соседей у F: {neighbors}")