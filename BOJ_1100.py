# 1100번: 하얀 칸

board = [list(input()) for _ in range(8)]
white_board = 0

for i in range(8):
    for j in range(8):
        if i%2 == j%2 and board[i][j] == 'F':
            white_board += 1
        
print(white_board)
