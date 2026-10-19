# 1
graph3 = [
    [0, 20, 0, 0, 0, 34, 0, 0, 9],
    [20, 0, 11, 0, 0, 0, 3, 0, 0],
    [0, 11, 0, 7, 0, 0, 3, 0, 0],
    [0, 0, 7, 0, 3, 0, 0, 0, 9],
    [0, 0, 0, 3, 0, 26, 0, 0, 5],
    [34, 0, 0, 0, 24, 0, 0, 0, 5],
    [0, 3, 3, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [9, 0, 0, 9, 5, 5, 0, 1, 0]
]

# 2
count_v = 0
for i in graph3:
    count_v += 1
print(f"2) вершин: {count_v}")

# 3
count_3 = 0
for i in graph3:
    deg = 0
    for j in i:
        if j > 0:
            deg += 1
    if deg == 3:
        count_3 += 1
print(f"3) степень 3 у: {count_3} вершин")

# 4
count = 0
for i in range(len(graph3)):
    for j in range(len(graph3[i])):
        if graph3[i][j] > 0:
            count += 1
edges = count // 2
print(f"4) ребер: {edges}")

# 5
s = 0
for i in range(len(graph3)):
    for j in range(len(graph3[i])):
        s += graph3[i][j]
total_s = s // 2
print(f"5) сумма: {total_s}")

# 6
neighbors = 0
for i in graph3[5]:
    if i > 0:
        neighbors += 1
print(f"6) соседей у F: {neighbors}")