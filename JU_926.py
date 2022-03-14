# 926 : 리스트 3 - 자가진단 6

list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[i][j] * list_b[i][j], end=" ")
    print()