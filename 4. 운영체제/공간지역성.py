from time import time
BOARD_LENGTH = 10000

board = [[0 for _ in range(BOARD_LENGTH)] for _ in range(BOARD_LENGTH)]

start1 = time()

for i in range(BOARD_LENGTH):
    for j in range(BOARD_LENGTH):
        board[i][j] = 1

end1 = time()

start2 = time()

for i in range(BOARD_LENGTH):
    for j in range(BOARD_LENGTH):
        board[j][i] = 2

end2 = time()

print("board[i][j] 처리 시간 : ", end1 - start1)
print("board[j][i] 처리 시간 : ", end2 - start2)