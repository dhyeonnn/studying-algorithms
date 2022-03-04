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