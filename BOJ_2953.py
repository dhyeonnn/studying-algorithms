# 2953번: 나는 요리사다

winner_score, winner_index = 0, 0

for i in range(5):
    score = sum(map(int, input().split()))

		# winner의 score값과 index를 동시에 갱신하는 과정
    if score > winner_score:
        winner_score, winner_index = score, i + 1

print(winner_index, winner_score)