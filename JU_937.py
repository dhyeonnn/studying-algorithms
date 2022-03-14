# 리스트 937 : 리스트 3 - 형성평가 9
list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]
list_c = []

for i in range(2):
    list_1 = []
    for j in range(3):
        mul = (list_a[i][j] * list_b[i][j])
        list_1.append(mul)
    list_c.append(list_1)
        
for i in range(2):
    for j in range(3):
        print(list_c[i][j], end='')
    print()