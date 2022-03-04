# 953 : 기타 자료형 - 형성평가 6

record = input().split()
foul = {}

for name in record:
    foul[name] = record.count(name)

min_foul = min(foul.values())

for name in foul:
    if foul[name] == min_foul:
        print(name)

print(min_foul)

'''
# 1. 딕셔너리 만들기
players = input().split()
fouls = {}

for player in players:
    # 1) 이미 선수가 있어요?
    if player in fouls:
        fouls[player] += 1
    # 2) 선수가 없어요?
    else:
        fouls[player] = 1

# 2. 최소 파울 갯수 찾기
min_foul = min(fouls.values())

# 3. 가장 파울 적게한 선수 출력
for player, foul in fouls.items():
    if foul == min_foul:
        print(player)

# 4. 최소 파울 갯수 출력
print(min_foul)
'''