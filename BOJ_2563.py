# 2563번: 색종이

paper = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

print(sum(sum(line) for line in paper))
